import os
import requests
from google import genai
from dotenv import load_dotenv

def get_makros(ingredients):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    nutrion_table = ["Ingredient - amount - kcal - protein - carbs - fatts"]

    for ingredient in ingredients.split("\n"):

        makros = client.models.generate_content(
            model ="gemini-2.0-flash-001",
            contents = f"Return the Makro nutrients for {ingredient}. if you have not recived anything return "". It is mandatory that you only return kcal, protein, carbs and fatts. MANDATORY!!! Use this format for your output 'kcal - protein - carbs - fatts' NO additonal text please."
        )

        nutrion_table.append(f"{ingredient} - {makros.text}")

    for entry in nutrion_table:
        print(entry)
        
    return  nutrion_table
    