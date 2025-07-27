#!/usr/bin/env python3
from utils.functions import demo, fetch_recipe, fetch_nutrition
import argparse
import re 

def main():
    parser = argparse.ArgumentParser(
        prog = "bitewise",
        description = "BiteWise: Your command-line sous-chef for recipes & more."
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--demo", "-d", action="store_true", help="a demo for our friend Boots the Bear")
    group.add_argument("--test", "-t", action="store_true", help="a demo for our friend Boots the Bear")
    group.add_argument("--recipe", "-r" , nargs="+", help="get a recipe for the dish based on its name")
    group.add_argument("--nutrition","-n", nargs="+", help="get nutritonal information about a dish based on its name")
    group.add_argument("--image","-i", nargs="+", help="get an image of the dish based on its name")
    args = parser.parse_args()

    if args.demo or args.test:
        demo()
    elif args.recipe:
        fetch_recipe("".join(args.recipe))
    elif args.nutrition:
        fetch_nutrition("".join(args.recipe))
    elif args.image:
        fetch_image("".join(args.recipe))

if __name__ == "__main__":
    main()