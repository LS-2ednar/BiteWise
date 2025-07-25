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
    group.add_argument("--test" ,type=str, help="A Demo for our friend Boots the Bear")
    group.add_argument("-t" ,type=str, help="A Demo for our friend Boots the Bear")
    group.add_argument("--url" ,type=str, help="URL to a recipie")
    group.add_argument("-u" ,type=str, help="URL to a recipie")
    group.add_argument("--name", type=str, help="Name of a recipe to search for")
    group.add_argument("-n", type=str, help="Name of a recipe to search for")

    args = parser.parse_args()

    if args.test or args.t:
        example()
    elif args.url or args.u:
        url_recipe(args.url)
    elif args.name or args.n:
        name_recipe(args.name)
    


def test():
    img_url = "TESTURL.CX"
    provide_image("TESTURL.CX")
    print("NUTRITION INFO")
    print("Protionsize")
    print("Cooking Instructions")
    return





if __name__ == "__main__":
    main()
    """
    test()
    """