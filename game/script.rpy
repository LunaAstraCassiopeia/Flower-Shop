# The script of the game goes in this file.
default bouquet = []
default meanings = {}
default decor = ""
# Declare characters used by this game. The color argument colorizes the
# name of the character.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    while len(UnmetCustomerList) > 0:
        $ bouquet = []
        $ meanings = {}
        $ decor = ""
        $ customer = getNewCustomer()
        $ joyRating = customer.runOnEnter()
        $ customer.runAfterFlowers(joyRating)
        $ print(joyRating)

    # This ends the game.

    return

screen flower_menu(customer):
    tag _flower_menu
    grid 3 2:
        frame:
            vbox:
                spacing 10 
                null height 20
                grid 1 8:
                    spacing 20
                    for name in FlowerList:
                        textbutton _("[name]"):
                            action [SensitiveIf(len(bouquet) <7), Function(add_flower, name, bouquet, meanings)]
        frame:
            vbox:
                grid 1 9:
                    text _("Bouquet:")
                    for flowerName in bouquet:
                        textbutton _("[flowerName]"):
                            action Function(remove_flower, flowerName, bouquet, meanings)
                    textbutton _("[decor]"):
                        action [Function(set_addon, "", decor, meanings), SetVariable("decor", "")]
        frame:
            vbox:
                textbutton _("submit"):
                    action Return(customer.calculateJoy(meanings))
        frame:
            vbox:
                grid 1 2:
                    for name in AddonList:
                        textbutton _("[name]"):
                            action [Function(set_addon, name, decor, meanings), SetVariable("decor", name)]
            