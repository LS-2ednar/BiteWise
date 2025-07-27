from utils.image_provider import provide_image
from utils.food_information import find_food_information
from utils.get_recipe import get_recipe
from utils.get_makros import get_makros

def demo():
    print("This Demo ignores your input! Bear, with me")
    print("""\nIf you are coding and your foodie buddy tells you about this dish called 'Nam Tok'
you could use this CLI and search for an image about the topic as follows:
    
    python BiteWise.py --img or -i "Nam Tok"
    """)
    input("\nPress Enter to see a Demo\n")
    image = provide_image("https://thai-foodie.com/wp-content/uploads/2024/09/moo-nam-tok-redo-1-1024x1024.jpg")
    print("""
Now I know there are strong opinions about coriander / celantro which is why we will now continue with some more programmer friendly food.

Our BEAREST friend Boots loves his "Backed Salmon", but from time to time it is hard to remember how the dish is produced. Fear no more, this CLI got you covered.

    python BiteWise.py --recipe or -r "Backed Salmon"
    """)
    input("\nPress Enter to see a Demo\n")
    steps, ingredients = get_recipe("https://www.lecremedelacrumb.com/best-easy-healthy-baked-salmon/","Backed Salmon")

    print("These are the cooking Steps:")
    print(steps)
    
    input("\nPress Enter to see the ingredients aswell\n")
    
    print("These are the used ingredients:")
    print(ingredients)

    print("""We can also get Nutrional Values for these Recipies to ensure we enjoy our food but keep it calorie friendly
    
    python BiteWise.py --nutrition or -n "Backed Salom" 
    """)
    input("\nPress Enter to see a Demo\n")

    makros = get_makros(ingredients)

def fetch_recipe(dish):
    name, url = find_food_information(dish) 
    steps, ingredients = get_recipe(url,name)
    print(ingredients)
    return

def fetch_nutrition(dish):
    name, url = find_food_information(dish) 
    steps, ingredients = get_recipe(url,name)
    get_makros(ingredients)
    return 