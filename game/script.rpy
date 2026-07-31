# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.
default flowers = {"Lilies": 0, "Roses": 0, "Hydrangeas": 0, "Guns": 0}
default wanted = {"Lilies": 3, "Roses": 5}
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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    e "Just testing some things!!"
    
    e "Give me a bouquet with 5 Roses and 3 Lilies!"

    call screen flower_menu

    $ joyRating = _return
    
    if joyRating["satisfaction"] >= 0:
        e "ooh, this was great!"
    elif joyRating["satisfaction"] > -2:
        e "It's okay..."
    elif joyRating["satisfaction"] > -10:
        e "This wasn't what I asked for..."
    if joyRating["Roses"] < 0:
        e "Roses were a little lacking..."
    if joyRating["Lilies"] < 0:
        e "And there weren't that many Lilies..."
    if "gunsAndRoses" in joyRating:
        e "heh, cool guns and roses though."

    hide screen flower_menu
    with dissolve

    # This ends the game.

    return

screen flower_menu():
    vbox:
        spacing 10 
        null height 20
        grid 4 1:
            spacing 20
            for key, val in flowers.items():
                frame:
                    use flower_stat(key)
        textbutton _("submit"):
            action Return(is_similar(flowers, wanted))
    

screen flower_stat(name):
    vbox:
        label name
        null height 5
        hbox:
            textbutton _("down"):
                action IncrementDict(flowers, name, amount=-1)
            text "[flowers[name]]"
            textbutton _("up"):
                action IncrementDict(flowers, name, amount=+1)