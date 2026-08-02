# The script of the game goes in this file.
default bouquet = [None, None, None, None, None, None, None]
default meanings = {}
default decor = ""
default page = 1
default day = 0
default book_open = False
default egg = False
default in_man = False
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
    play music "arrivals.mp3" if_changed loop volume 0.75

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
    xzoom 1
transform position1:
    pos (0.47, 0.22)
    xzoom 1
transform position2:
    pos (0.59, 0.21)
    xzoom -1
transform position3:
    pos (0.52, 0.16)
    xzoom 1
transform position4:
    pos (0.48, 0.1)
    xzoom 1
transform position5:
    pos (0.57, 0.14)
    xzoom -1
transform position6:
    pos (0.51, 0.07)
    xzoom 1
transform addonpos:
    pos (0.58, 0.07)
    xzoom 1
    
transform sPosition0:
    pos (0.48, 0.4)
    rotate 0
transform sPosition1:
    pos (0.45, 0.365)
    rotate 345
transform sPosition2:
    pos (0.51, 0.363)
    rotate 15
transform sPosition3:
    pos (0.48, 0.30)
    rotate 359
transform sPosition4:
    pos (0.45, 0.25)
    rotate 349
transform sPosition5:
    pos (0.5, 0.28)
    rotate 12
transform sPosition6:
    pos (0.48, 0.23)
    rotate 348

transform shPosition0:
    pos (0.11, 0.05)
    zoom 0.75
transform shPosition1:
    pos (0.22, 0.03)
    zoom 0.75
transform shPosition2:
    pos (0.32, 0.05)
    zoom 0.75
transform shPosition3:
    pos (0.11, 0.29)
    zoom 0.75
transform shPosition4:
    pos (0.215, 0.29)
    zoom 0.75
transform shPosition5:
    pos (0.32, 0.29)
    zoom 0.75
transform shPosition6:
    pos (0.11, 0.55)
    zoom 0.75
transform shPosition7:
    pos (0.22, 0.55)
    zoom 0.75
transform leafTransform:
    pos (0.35, 0.51)
    zoom 0.75
transform branchTransform:
    pos (0.3, 0.51)
    zoom 0.75
    xzoom -1

transform bouquetbackpos:
    pos (0.41, 0.04)
transform bouquetfrontpos:
    pos (0.44, 0.28)


transform bookpos:
    pos (0.64, 0.27)
transform openbookpos:
    pos (0.43, 0)
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
    $ i = 0
    for name in FlowerList:
        imagebutton auto flower_pic(name, "bouquet") at get_shelftransform(i):
            action [SensitiveIf((None in bouquet) and not book_open), Function(add_flower, name, bouquet, meanings)]
        $ i = i + 1
    imagebutton auto flower_pic("Leaf", "bouquet") at leafTransform:
        action [SensitiveIf(not book_open), Function(set_addon, "Leaf", meanings)]
    imagebutton auto flower_pic("Stick", "bouquet") at branchTransform:
        action [SensitiveIf(not book_open), Function(set_addon, "Stick", meanings)]
    $ i = len(bouquet)
    for flowerName in bouquet:
        if bouquet[i-1] is not None:
            add "flowers/stem idle.png" at get_stem_transform(i)
        $ i = i - 1
    if len(bouquet) > 0 and bouquet.count(None) < 7:
        imagebutton auto "flowers/bouquet front %s.png" at bouquetfrontpos:
            hovered [Function(show_bouquet)]
            unhovered [Function(hide_bouquet)]
            action [Return(customer.calculateJoy(meanings)), SensitiveIf(not book_open)]
    if(decor != ""):
        imagebutton auto flower_pic(decor, "bouquet") at addonpos:
            action [SensitiveIf(not book_open), Function(set_addon, name, decor, meanings), SetVariable("decor", "")]
    $ i = len(bouquet)
    for flowerName in bouquet:
        if bouquet[i-1] is not None:
            imagebutton auto flower_pic(bouquet[i-1], "bouquet") at get_transform(i):
                action [SensitiveIf(not book_open), Function(remove_flower, i-1, bouquet, meanings)]
        $ i = i - 1

screen book_button():
    zorder -1
    imagebutton auto "flower manual %s" at bookpos:
        action [Function(open_book, page), SetVariable("book_open", True)]

screen book_screen():
    if (page > 1):
        imagebutton auto "left arrow %s" at leftarrowos:
            action [SensitiveIf(page > 1 and not in_man), Function(change_page, page, -1)]
        imagebutton auto "exit button %s" at exitbuttonpos:
            action [Function(close_book), SetVariable("book_open", False)]
    else:
        imagebutton auto "exit button %s" at leftarrowos:
            action [Function(close_book), SetVariable("book_open", False)]
    if (page < 5):
        imagebutton auto "right arrow %s" at rightarrowpos:
            action [SensitiveIf(page < 5 and not in_man), Function(change_page, page, 1)]

init python:
    import random
    def open_book(current_page: int):
        global book_open
        renpy.hide_screen("book_button")
        renpy.show("manual page " + str(current_page), at_list={openbookpos}, layer = "book")
        if page == 1 and egg:
            renpy.show("egg", at_list={openbookpos}, layer = "book")
        renpy.show_screen("book_screen")
        book_open = True
        
    def show_bouquet():
        renpy.show("bouquet back hover", at_list={bouquetbackpos})
        
    def hide_bouquet():
        renpy.hide("bouquet back hover")

    def change_page(current_page: int, shift: int):
        global page
        global book_open
        global egg
        global in_man
        book_open = True
        renpy.hide("manual page " + str(current_page), layer = "book")
        renpy.hide("egg", layer = "book")
        page = current_page + shift
        if(random.random() > 0.999 and not egg):
            renpy.music.play("man.mp3",loop=True)
            renpy.show("black")
            egg = True
            in_man = True
            renpy.show("manual page tree", at_list={openbookpos}, layer = "book")
        else:
            renpy.show("manual page " + str(page), at_list={openbookpos}, layer = "book")
            if page == 1 and egg:
                renpy.show("egg", at_list={openbookpos}, layer = "book")
    
    def close_book():
        global book_open
        global in_man
        if in_man:
            in_man = False
            renpy.hide("black")
            renpy.music.play("arrivals.mp3", fadein=5, if_changed=True, loop=True, relative_volume=0.75)
        renpy.hide_screen("book_screen")
        renpy.hide("manual page " + str(page), layer = "book")
        renpy.hide("egg", layer = "book")
        renpy.show_screen("book_button")
        book_open = False


    def get_shelftransform(index):
        match index:
            case 0:
                return shPosition0
            case 1:
                return shPosition1
            case 2:
                return shPosition2
            case 3:
                return shPosition3
            case 4:
                return shPosition4
            case 5:
                return shPosition5
            case 6:
                return shPosition6
            case 7:
                return shPosition7
            case _:
                return shPosition0
            
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
