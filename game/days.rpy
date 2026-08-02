init python:
    def dayShift():
        match day:
            case 1:
                renpy.jump("dayOne")
            case _:
                return
        return

label dayOne:

    ilana "Looking for this?"

    show Ilana Hehe at right
    with dissolve

    peri "HEY!!!"
    blank "(Ilana hands you your flower manual.)"

    show Ilana Meh at right

    peri "...thank goodness, it's just you..."
    ilana "You really should keep a better eye on your shop."
    ilana "Did you know how easy it was to sneak in here before you opened?"
    peri "I leave the lock open once..."
    ilana "To think I'd give this to you, only for you to leave this so carelessly in the shop like this..."
    
    show Ilana Sucks Ass at right

    ilana "You hate me or something?"
    blank "(Ilana sighs very exaggeratedly, then giggles as you hit her very lightly.)"
    
    show Ilana Meh at right

    ilana "Come on, you and I both know I was kidding!"
    peri "I guess..."
    ilana "Now, come on. You're opening soon, right?"
    ilana "I'll be your first customer!"
    ilana "Make me something!"
    blank "(You giggle.)"
    peri "You want anything specific?"

    $ bouquet = []
    $ meanings = {}
    $ decor = ""
    $ joyRating = IlanaTutorialCustomer.runOnEnter()
    $ IlanaTutorialCustomer.runAfterFlowers(joyRating)
    $ print(joyRating)

    $ majorCustomerDayList = [ArthurOneCustomer, KaraOneCustomer]
    $ quota = 5
    $ initialize_customers(majorCustomerDayList)

    deb "Hi!"

    deb "[UnmetCustomerList]"
    
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
    
    $ nightShift()
    # This ends the game.

    return