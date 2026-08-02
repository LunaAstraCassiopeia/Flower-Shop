# The script of the game goes in this file.
default bouquet = []
default meanings = {}
default decor = ""
default page = 1
default day = 0
default book_open = False
define deb = Character("Debug")
define flowery = Character("Flowery")
define config.layers = [ 'master', 'transient', 'flowers', 'book', 'screens', 'overlay' ]
define long_dissolve = Dissolve(1.0)
# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:
    scene black
    
    $ renpy.add_layer("book", above = "screens")
    $ init_globals()
    $ day = 1
    stop music fadeout 0.5

    blank "(You arrive at the airport.)"
    blank "(5:42 AM. The Sun is just beginning to rise, but that doesn't stop the influx of people walking out of the gates.)"
    blank "(\"Each of them has some reason they're going home,\" you think to yourself.)"
    blank "(Some are here to visit family, some are coming back from international trips, some are just flying back to be in the comfort of their home country again.)"
    blank "(But you're not here to leave or anything.)"
    blank "(You hear the grating noise of a steel door opening, as you begin to set up shop for the day.)"
    blank "(You realize that you forgot to lock the door when you closed. It's probably fine, right?)"
    blank "(It's a quaint shop, located near the gifts and souvenirs section of the airport.)"
    blank "(Instead of acrylic keychains, fridge magnets or vague merchandise relating to the country you're currently standing on...)"

    scene default bg
    with long_dissolve
    play music "flowershop day.mp3" if_changed loop volume 0.75

    blank "(Your shop specializes in selling flowers and custom bouquets.)"
    peri "Now to make sure everything's in order..."
    blank "(You check through all the colored baskets of flowers, making sure that none of them have wilted or have suddenly been stolen while you were away.)"
    blank "(There's a sweet, floral scent that fills the space around you immediately.)"
    peri "Everything seems good...{w=0.3} I just have to look for..."
    blank "(You begin searching the drawers near your desk for something.)"
    blank "(You're still pretty new to this business, so you kind of can't survive a day of work without it.)"
    blank "(Despite this, you can't seem to find it. You start to panic.) "
    peri "Oh no, oh no! Did I leave it at home?"
    blank "(You circle around the shop, double- no, triple-checking places you swear you've looked a hundred times beforehand for where it might be.)"
    blank "(You're thinking of looking for it at home, when suddenly...)"

    $ dayShift()
    jump dayOne

transform shift_right:
    align (-0.45, -0.05) alpha 0.0
    linear 0.5 alpha 1.0
    
transform position0:
    pos (0.53, 0.26)
transform position1:
    pos (0.47, 0.225)
transform position2:
    pos (0.59, 0.215)
transform position3:
    pos (0.52, 0.16)
transform position4:
    pos (0.48, 0.15)
transform position5:
    pos (0.57, 0.14)
transform position6:
    pos (0.51, 0.07)
transform addonpos:
    pos (0.58, 0.07)
    
transform sPosition0:
    pos (0.56, 0.4)
transform sPosition1:
    pos (0.53, 0.365)
transform sPosition2:
    pos (0.59, 0.365)
transform sPosition3:
    pos (0.56, 0.30)
transform sPosition4:
    pos (0.56, 0.4)
transform sPosition5:
    pos (0.56, 0.28)
transform sPosition6:
    pos (0.56, 0.4)

transform bouquetbackpos:
    pos (0.41, 0.04)
transform bouquetfrontpos:
    pos (0.44, 0.28)


transform bookpos:
    pos (0.64, 0.27)
transform openbookpos:
    pos (0.43, 0.04)
transform leftarrowos:
    pos (0.455, 0.07)
transform rightarrowpos:
    pos (0.935, 0.07)
transform exitbuttonpos:
    pos (0.455, 0.19)
    
transform nothing:
    align (0,0) alpha 0.0
        

screen flower_menu(customer):
    layer "flowers"
    tag _flower_menu
    grid 3 2 at shift_right:
        vbox:
            spacing 10 
            null height 20
            grid 3 3:
                spacing 32
                for name in FlowerList:
                    imagebutton auto flower_pic(name, "flower"):
                        action [SensitiveIf((len(bouquet) <7) and not book_open), Function(add_flower, name, bouquet, meanings)]
                grid 2 1:
                    for name in AddonList:
                        imagebutton auto flower_pic(name, "flower"):
                            action [Function(set_addon, name, decor, meanings), SetVariable("decor", name)]
    $ i = len(bouquet)
    for flowerName in bouquet:
        add "flowers/stem idle.png" at get_stem_transform(i)
        $ i = i - 1
    if len(bouquet) > 0:
        imagebutton auto "flowers/bouquet front %s.png" at bouquetfrontpos:
            hovered [Function(show_bouquet)]
            unhovered [Function(hide_bouquet)]
            action [Return(customer.calculateJoy(meanings)), SensitiveIf(not book_open)]
    if(decor != ""):
        imagebutton auto flower_pic(decor, "bouquet") at addonpos:
            action [SensitiveIf(not book_open), Function(set_addon, name, decor, meanings), SetVariable("decor", "")]
    $ i = len(bouquet)
    for flowerName in bouquet:
        imagebutton auto flower_pic(bouquet[i-1], "bouquet") at get_transform(i):
            action [SensitiveIf(not book_open), Function(remove_flower, bouquet[i-1], bouquet, meanings)]
        $ i = i - 1

screen book_button():
    zorder -1
    imagebutton auto "flower manual %s" at bookpos:
        action [Function(open_book, page), SetVariable("book_open", True)]

screen book_screen():
    if (page > 1):
        imagebutton auto "left arrow %s" at leftarrowos:
            action [SensitiveIf(page > 1), Function(change_page, page, -1)]
        imagebutton auto "exit button %s" at exitbuttonpos:
            action [Function(close_book), SetVariable("book_open", False)]
    else:
        imagebutton auto "exit button %s" at leftarrowos:
            action [Function(close_book), SetVariable("book_open", False)]
    if (page < 5):
        imagebutton auto "right arrow %s" at rightarrowpos:
            action [SensitiveIf(page < 5), Function(change_page, page, 1)]

init python:
    import random
    def open_book(current_page: int):
        global book_open
        renpy.hide_screen("book_button")
        renpy.show("manual page " + str(current_page), at_list={openbookpos}, layer = "book")
        renpy.show_screen("book_screen")
        book_open = True
        
    def show_bouquet():
        renpy.show("bouquet back hover", at_list={bouquetbackpos})
        
    def hide_bouquet():
        renpy.hide("bouquet back hover")

    def change_page(current_page: int, shift: int):
        global page
        global book_open
        book_open = True
        renpy.hide("manual page " + str(current_page), layer = "book")
        page = current_page + shift
        if(random.random() > 0.99):
            renpy.show("manual page tree", at_list={openbookpos}, layer = "book")
        else:
            renpy.show("manual page " + str(page), at_list={openbookpos}, layer = "book")
    
    def close_book():
        global book_open
        renpy.hide_screen("book_screen")
        renpy.hide("manual page " + str(page), layer = "book")
        renpy.show_screen("book_button")
        book_open = False


    def get_transform(index):
        match index:
            case 1:
                return position0
            case 2:
                return position1
            case 3:
                return position2
            case 4:
                return position3
            case 5:
                return position4
            case 6:
                return position5
            case 7:
                return position6
            case _:
                return position0

    def get_stem_transform(index):
        match index:
            case 1:
                return sPosition0
            case 2:
                return sPosition1
            case 3:
                return sPosition2
            case 4:
                return sPosition3
            case 5:
                return sPosition4
            case 6:
                return sPosition5
            case 7:
                return sPosition6
            case _:
                return sPosition0
