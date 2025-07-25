from utils.image_provider import provide_image

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
        description = "BiteWise: Your command-line sous-chef for recipies & more."
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



import requests 
from bs4 import BeautifulSoup

def url_parser(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
    except:
        ConnectionError("Not able to fetch any data")
        exit(1)

    title = soup.find("h1").text

    ingredients = []
    ing_list = soup.find_all("li", class_="ingredient")
    for li in ing_list:
        ingredients.append(li.text)

    img_tag = soup.find("img")
    if img_tag:
        img_url = img_tag.get("src")

        print(ingredients,title)
        return img_url
    
    else:
        print(ingredients,title)
        return "123.com"

def test():
    url = "https://hot-thai-kitchen.com/laab-gai/"
    img_url = url_parser(url)
    
    provide_image(img_url)
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