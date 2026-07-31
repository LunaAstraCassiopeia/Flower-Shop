# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default meanings = {}
default bouquet = []
default decor = ""
default FlowerList = ["Rose","Carnation", "Hydrangea", "Lily", "Bluebell", "Hyacinth", "Orchid", "Forget-Me-Not"]
default AddonList = ["Stick", "Leaf"]

default wanted = {"Lily": 3, "Rose": 5}
default noPreferences = {"test": 0}
define e = Character("Eileen")
default eCustomer = Customer(wanted, noPreferences)


# The game starts here.
default floweryWants = {"Lily": 1, "Rose": 1, "Hydrangea": 1}
default floweryPreferences = {"Guns": 1000, "NoOverflow": 1}
define FloweryChar = Character("Flowery")
default flowery = Customer(floweryWants, floweryPreferences)
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Hi there! I'm your first customer! Please give me a bouquet with 5 Roses and 3 Lilies!"
    $ bouquet = []
    $ meanings = {}
    $ decor = ""

    call screen flower_menu(eCustomer)

    $ joyRating = _return
    
    if joyRating["satisfaction"] < 0.3:
        e "Oh, this was great!"
    elif joyRating["satisfaction"] < 0.3:
        e "It's okay..."
    elif joyRating["satisfaction"] < 0.5:
        e "This wasn't what I asked for..."
    if joyRating["Rose"] < 0:
        e "Roses were a little lacking, and..."
    if joyRating["Rose"] > 0:
        e "There were too many roses, and..."
    if joyRating["Lily"] > 0:
        e "You added far too many Lilies..."
    if joyRating["Lily"] < 0:
        e "There weren't that many Lilies..."
        
    e "My satisfaction score is [joyRating['satisfaction']]"
    $ print(joyRating)

    hide screen flower_menu
    with dissolve

    hide eileen happy
    with dissolve

    show flowery
    $ bouquet = []
    $ meanings = {}
    $ decor = ""
    FloweryChar "Jarona!"

    FloweryChar "Heh, I saw how you treated that last customer."

    FloweryChar "Flowers blooms in your heart!"

    FloweryChar "Gimme a rose, a lily, and a hydrangea."

    call screen flower_menu(flowery)

    $ joyRating = _return

    if joyRating["satisfaction"] < 0.3:
        FloweryChar "Flowers!"
    elif joyRating["satisfaction"] < 0.3:
        FloweryChar "It's okay, little guy"
    elif joyRating["satisfaction"] < 30:
        FloweryChar "Sustingus."
    else:
        FloweryChar "Guns? Heh, that's so human."
    if joyRating["Rose"] < 0:
        FloweryChar "There were no Roses!"
    if joyRating["Lily"] < 0:
        FloweryChar "Barely even any Lilies.."
    if joyRating["Hydrangea"] < 0:
        FloweryChar "Where were the Hydrangeas?"
        
    FloweryChar "Satisfied? I'd rate it a [joyRating['satisfaction']] out of Flowery"
    $ print(joyRating)

    # This ends the game.

    return

screen flower_menu(customer):
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
            