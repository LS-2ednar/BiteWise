import os
import requests
from google import genai
from dotenv import load_dotenv


def get_recipe(url, recipe_name="Baked Salmon",unit_type="metric"):
    """
    get a recipe from a url
    """

    recipe = requests.get(url)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    recipe_steps = client.models.generate_content(

            model ="gemini-2.0-flash-001",
            contents = f"Summarize the Steps one by line to provide this dish mentioned (enusre that you use {unit_type} units) in the text following: {recipe.text}"
        )
    
    recipe_ingredients = client.models.generate_content(

            model ="gemini-2.0-flash-001",
            contents = f"Summarize the Ingredients needed to prepare the dish mentioned (ensure that you use {unit_type} units) in the follwing text: {recipe.text}"
        )


    check = client.models.generate_content(

            model ="gemini-2.0-flash-001",
            contents = f"Return True if the following text is a recipe {recipe_steps}" 
        )

    if check.text != True:
        recipe_steps = client.models.generate_content(

            model ="gemini-2.0-flash-001",
            contents = f"Write a Step by Step Guide on how to prepare a {recipe_name} using {unit_type} units."
        )

        recipe_ingredients = client.models.generate_content(

            model ="gemini-2.0-flash-001",
            contents = f"Write a list of all ingredients needed for the following recipie steps {recipe_steps} using {unit_type} units."
        )
    
    return recipe_steps.text, recipe_ingredients.text