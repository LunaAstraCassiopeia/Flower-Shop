# The script of the game goes in this file.
default bouquet = []
default meanings = {}
default decor = ""
default page = 1
default day = 0
default book_open = False
define deb = Character("Debug")
define blank = Character("")
define peri = Character("Periwinkle")
define config.layers = [ 'master', 'transient', 'flowers', 'book', 'screens', 'overlay' ]
# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene default bg
    $ renpy.add_layer("book", above = "screens")
    $ init_globals()
    $ day = 1
    $ dayShift()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    # debug set of Customers
    
    jump dayOne

transform shift_right:
    align (-0.45, -0.05) alpha 0.0
    linear 0.5 alpha 1.0
    
transform position0:
    pos (0.53, 0.26)
transform position1:
    pos (0.47, 0.255)
transform position2:
    pos (0.59, 0.245)
transform position3:
    pos (0.485, 0.18)
transform position4:
    pos (0.56, 0.17)
transform position5:
    pos (0.51, 0.1)
transform position6:
    pos (0.52, 0.19)
transform addonpos:
    pos (0.58, 0.1)
transform bookpos:
    pos (0.64, 0.27)
transform openbookpos:
    pos (0.46, 0.07)
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
    if(decor != ""):
        imagebutton auto flower_pic(decor, "bouquet") at addonpos:
            action [SensitiveIf(not book_open), Function(set_addon, name, decor, meanings), SetVariable("decor", "")]
    $ i = 0
    for flowerName in bouquet:
        imagebutton auto flower_pic(flowerName, "bouquet") at get_transform(i):
            action [SensitiveIf(not book_open), Function(remove_flower, flowerName, bouquet, meanings)]
        $ i = i + 1
    frame:
        vbox:
            textbutton _("submit"):
                action Return(customer.calculateJoy(meanings))

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
            case 0:
                return position0
            case 1:
                return position1
            case 2:
                return position2
            case 3:
                return position3
            case 4:
                return position4
            case 5:
                return position5
            case 6:
                return position6
            case _:
                return position0
