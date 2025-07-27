from utils.image_provider import provide_image
from utils.food_information import find_food_information
from utils.get_recipe import get_recipe
from utils.get_makros import get_makros

import argparse

def demo():
    print("This Demo ignores your input! Bear, with me")
    print("""\nIf you are coding and your foodie buddy tells you about this dish called 'Nam Tok'
you could use this CLI and search for an image about the topic as follows:
    
    python BiteWise.py --img or -i "Nam Tok"
    """)
    input("\nPress Enter to see a Demo\n")
    provide_image("https://thai-foodie.com/wp-content/uploads/2024/09/moo-nam-tok-redo-1-1024x1024.jpg")
    print("""
Now I know there are strong opinions about coriander / celantro which is why we will now continue with some more programmer friendly food.

Our BEAREST friend Boots loves his "Backed Salmon", but from time to time it is hard to remember how the dish is produced. Fear no more, this CLI got you covered.

    python BiteWise.py --recipe or -r "Backed Salmon"
    """)
    input("\nPress Enter to see a Demo\n")
    steps, ingredients = get_recipe("https://www.lecremedelacrumb.com/best-easy-healthy-baked-salmon/")

    print("These are the cooking Steps:")
    print(steps)
    
    input("\nPress Enter to see the ingredients aswell\n")
    
    print("These are the used ingredients:")
    print(ingredients)

    print("""We can also get Nutrional Values for these Recipies to ensure we enjoy our food but keep it calorie friendly
    
    python BiteWise.py --nutrition or -n "Backed Salom" 
    """)
    input("\nPress Enter to see a Demo\n")





def name_recipe(name):
    print("Placeholder: NAME-Way")



def main():
    parser = argparse.ArgumentParser(
        prog = "bitewise",
        description = "BiteWise: Your command-line sous-chef for recipes & more."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--poc", "-p", action="store_true", help="A Demo for our friend Boots the Bear")
    group.add_argument("--test", "-t", action="store_true", help="A Demo for our friend Boots the Bear")
    group.add_argument("--recipe", "-r" ,type=str, help="Get a recipe for the dish you are looking for")
    group.add_argument("--nutrition","-n", type=str, help="Get Nutritonal information about your dish")


    
    group.add_argument("--name", type=str, help="Name of a recipe to search for")
    group.add_argument("-n", type=str, help="Name of a recipe to search for")

    args = parser.parse_args()

    if args.poc or args.p or args.test or args.t:
        demo()
    elif args.name or args.n:
        name_recipe(args.name)


"""
Before Refactoring Area
"""


def test():
    
    """
    title, recipes = find_food_information("Bannanen brot")
    print(title)
    print(recipes)
    """
    recipe, ingredients = get_recipe("https://ifoodreal.com/baked-salmon-recipe/")
    """print(recipe)"""

    print("\n\n\n")
    print(ingredients)
    
    
    
    """
    makros = get_makros(ingredients)
    print(makros)
    """
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
      