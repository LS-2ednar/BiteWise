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
    
    def ask_gemini_for_recipe_page(dish_name):
    # Gemini prompt: find a real, reputable recipe webpage for the dish
        prompt = f"Find a real, reputable English-language recipe webpage for '{dish_name}'. Respond ONLY with the direct URL, nothing else."
        api_key = os.environ.get("GEMINI_API_KEY")  # Or however you store your key

        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [{"parts": [{"text": prompt}]}]
        }

        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key,
            headers=headers,
            json=data,
            timeout=30
        )
        url = response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
        return url
    try:
        recipes_urls = ask_gemini_for_recipe_page(proper_food_name.text)
    except:
        print("Faild to find a real URL :-(")
        recipes_urls = "www.noURL.cry"

    return proper_food_name.text, recipes_urls
