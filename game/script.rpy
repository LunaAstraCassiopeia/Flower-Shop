# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

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

    $ flowers = {"Lilies": 0, "Roses": 0, "Hydrangeas": 0, "Guns": 0}

    show screen flower_menu(flowers)
    
    e "Give me a bouquet with 5 Roses and 3 Lilies!"

    hide screen flower_menu
    with dissolve

    e "or don't. fuck you."

    # This ends the game.

    return

screen flower_menu(bouquet):
    vbox:
        spacing 10 
        null height 20
        default number = amount
        vbox:
            label name
            null height 5
            hbox:
                textbutton _("down"):
                    action SetScreenVariable("number", number - 1)
                text "[number]"
                textbutton _("up"):
                    action SetScreenVariable("number", number + 1)

screen flower_stat(name, amount):
    default number = amount
    vbox:
        label name
        null height 5
        hbox:
            textbutton _("down"):
                action SetScreenVariable("number", number - 1)
            text "[number]"
            textbutton _("up"):
                action SetScreenVariable("number", number + 1)