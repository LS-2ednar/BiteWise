from utils.image_provider import provide_image
from utils.food_information import find_food_information

import argparse

def example():
    print("Placeholder: Example-Way")

def url_recipe(url):
    print("Placehodler: URL-Way")

def name_recipe(name):
    print("Placeholder: NAME-Way")

def main():
    parser = argparse.ArgumentParser(
        prog = "bitewise",
        description = "BiteWise: Your command-line sous-chef for recipes & more."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--poc" ,type=str, help="A Demo for our friend Boots the Bear")
    group.add_argument("-p" ,type=str, help="A Demo for our friend Boots the Bear")
    group.add_argument("--url" ,type=str, help="URL to a recipie")
    group.add_argument("-u" ,type=str, help="URL to a recipie")
    group.add_argument("--name", type=str, help="Name of a recipe to search for")
    group.add_argument("-n", type=str, help="Name of a recipe to search for")

    args = parser.parse_args()

    if args.poc or args.p:
        example()
    elif args.url or args.u:
        url_recipe(args.url)
    elif args.name or args.n:
        name_recipe(args.name)


"""
Before Refactoring Area
"""
import os
import requests
from google import genai
from dotenv import load_dotenv

def get_cooking(recipes):
    """
    check if input is of type string and transform it to a list if possible. Otherwise return boots favorit food.
    """
    if isinstance(recipes,str):
        try:
            individual_recipes = recipes.split(",")
        except:
            Exception("recipes format was wrong, providing information about Baked Salmon instead.")
            individual_recipes = ["https://www.lecremedelacrumb.com/best-easy-healthy-baked-salmon/"]

 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    

    """
    determin recipies & ingreedients
    """
    recipes, ingreedients = {}, ""
    for url in individual_recipes:
        html = requests.get(url)
        if html.status_code != 404:
            recipies[url] = html.text
            recipe_ingredients = client.models.generate_content(
                model ="gemini-2.0-flash-001",
                contents = f"Create a list word by word seperated by comma off all ingredients mentioned in the following text: {html.text} "
            )
            ingredients += recipe_ingredients.text

def test():
    
    """
    title, recipes = find_food_information("Bannanen brot")
    print(title)
    print(recipes)
    """

    recipes ="https://einfachbacken.de/rezepte/bananenbrot-einfaches-rezept,https://www.lidl-kochen.de/rezeptwelt/bananenbrot-rezept-zum-backen-1453,https://www.koch-mit.de/rezepte/bananenbrot,https://www.gutekueche.at/bananenbrot-rezept-1946,https://www.springlane.de/magazin/ratgeber/bananenbrot-rezept/"

    get_cooking(recipes)
    
    """
    provide_image(img_url)
    """
    print("NUTRITION INFO")
    print("Protionsize")
    print("Cooking Instructions")

    return



"""
End of Before Refactoring Area
"""


if __name__ == "__main__":
    """
    main()
    """
    test()