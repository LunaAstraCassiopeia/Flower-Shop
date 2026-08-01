# The script of the game goes in this file.
default bouquet = []
default meanings = {}
default decor = ""
define deb = Character("Debug")
# Declare characters used by this game. The color argument colorizes the
# name of the character.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene default bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    # debug set of Customers
    $ customerMasterlist = [RoseCustomer, CarnationCustomer, HydrangeaCustomer]
    $ initialize_customers(customerMasterlist)
    $ quota = 2

    deb "Hi!"

    deb "[CustomerList]"
    
    jump customerWave

label customerWave:
    while len(UnmetCustomerList) > 0 and quota > 0:
        $ bouquet = []
        $ meanings = {}
        $ decor = ""
        $ customer = getNewCustomer()
        $ joyRating = customer.runOnEnter()
        $ customer.runAfterFlowers(joyRating)
        $ print(joyRating)
        $ quota -= 1
        jump customerCutscene

    # This ends the game.

    return

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
    
transform nothing:
    align (0,0) alpha 0.0
        

screen flower_menu(customer):
    tag _flower_menu
    grid 3 2 at shift_right:
        vbox:
            spacing 10 
            null height 20
            grid 3 3:
                spacing 32
                for name in FlowerList:
                    imagebutton auto flower_pic(name, "flower"):
                        action [SensitiveIf(len(bouquet) <7), Function(add_flower, name, bouquet, meanings)]
                grid 2 1:
                    for name in AddonList:
                        imagebutton auto flower_pic(name, "flower"):
                            action [Function(set_addon, name, decor, meanings), SetVariable("decor", name)]
    if(decor is not ""):
        imagebutton auto flower_pic(decor, "bouquet") at addonpos:
            action [Function(set_addon, name, decor, meanings), SetVariable("decor", "")]
    $ i = 0
    for flowerName in bouquet:
        imagebutton auto flower_pic(flowerName, "bouquet") at get_transform(i):
            action Function(remove_flower, flowerName, bouquet, meanings)
        $ i = i + 1
    frame:
        vbox:
            textbutton _("submit"):
                action Return(customer.calculateJoy(meanings))
init python:
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
