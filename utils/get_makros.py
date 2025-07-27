import os
import requests
from google import genai
from dotenv import load_dotenv

def get_makros(ingredients):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    makros = client.models.generate_content(
        model ="gemini-2.0-flash-001",
        contents = f"Return the Makro nutrients (kcal, Protein, Carbs, Fatts) of the listed ingredients combined. Make sure to just return the makro nutriens not more. I do not want to see any explanation on why the estimate was created. {ingredients}"
    )

    return makros.text
    