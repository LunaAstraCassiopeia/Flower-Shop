# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default flowers = {"Lilies": 1, "Roses": 1, "Hydrangeas": 1, "Guns": 1}
default wanted = {"Lilies": 3, "Roses": 5}
default noPreferences = {"test": 0}
define e = Character("Eileen")
default eCustomer = Customer(wanted, noPreferences)


# The game starts here.
default floweryWants = {"Lilies": 1, "Roses": 1, "Hydrangeas": 1}
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

    call screen flower_menu(eCustomer)

    $ joyRating = _return
    
    if joyRating["satisfaction"] < 0.3:
        e "Oh, this was great!"
    elif joyRating["satisfaction"] < 0.3:
        e "It's okay..."
    elif joyRating["satisfaction"] < 0.5:
        e "This wasn't what I asked for..."
    if joyRating["Roses"] < 0:
        e "Roses were a little lacking, and..."
    if joyRating["Roses"] > 0:
        e "There were too many roses, and..."
    if joyRating["Lilies"] > 0:
        e "You added far too many Lilies..."
    if joyRating["Lilies"] < 0:
        e "There weren't that many Lilies..."
        
    e "My satisfaction score is [joyRating['satisfaction']]"

    hide screen flower_menu
    with dissolve

    hide eileen happy
    with dissolve

    show flowery
    $ flowers = {"Lilies": 1, "Roses": 1, "Hydrangeas": 1, "Guns": 1}
    FloweryChar "Jarona!"

    FloweryChar "Heh, I saw how you treated that last customer."

    FloweryChar "Flowers blooms in your heart!"

    FloweryChar "Gimme one of everything, but no gun's."

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
    if joyRating["Roses"] < 0:
        FloweryChar "There were no Roses!"
    if joyRating["Lilies"] < 0:
        FloweryChar "Barely even any Lilies.."
    if joyRating["Hydrangeas"] < 0:
        FloweryChar "Where were the Hydrangeas?"
        
    FloweryChar "Satisfied? I'd rate it a [joyRating['satisfaction']] out of Flowery"

    # This ends the game.

    return

screen flower_menu(customer):
    vbox:
        spacing 10 
        null height 20
        grid 10 1:
            spacing 20
            for key, val in flowers.items():
                frame:
                    use flower_stat(key)
        textbutton _("submit"):
            action Return(customer.calculateJoy(flowers))
    

screen flower_stat(name):
    vbox:
        label name
        null height 5
        hbox:
            textbutton _("down"):
                action IncrementDict(flowers, name, amount=-1)
            text "[flowers[name]-1]"
            textbutton _("up"):
                action IncrementDict(flowers, name, amount=+1)