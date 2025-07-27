import os
import requests
from google import genai
from dotenv import load_dotenv

def find_food_information(food):
    """
    find food based on name.
    """
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    proper_food_name = client.models.generate_content(
        model ="gemini-2.0-flash-001",
        contents = f"Can you find a food that is called {food} and return the correct spelling, no extra information needed."
    )
    
    """
    find food recipies on google
    """
    food_name = proper_food_name.text
    url_text_clean = food_name.replace("\n","")
    request_url = f"https://www.google.com/search?q={url_text_clean.replace(' ','+')}+recipe"
    recipes_html = requests.get(request_url)
    recipies = client.models.generate_content(
        model ="gemini-2.0-flash-001",
        contents = f"Return only the first 5 recipie urls about {food_name} seperate them by comma no additional information needed, from the following text: {recipes_html.text}"
    )

    return proper_food_name.text, recipies.text 
