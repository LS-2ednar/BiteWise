from term_image.image import from_url, Size

def provide_image(url):
    try:
        image = from_url(url)
    except:
        print("Cannot find an image at provided URL using a placeholder")
        image = from_url("https://www.boot.dev/_nuxt/baked-salmon.QSU05kuT.webp",width=Size.FIT_TO_WIDTH)
    try:
        image.draw() 
        #Looks kind of funny zsh terminal.
    except:
        print("\n\nYou are trying to eat more than your terminal can chew.\nChange your terminal size and try again.\n\n")
        