init python:
    def nightShift():
        match day:
            case 1:
                renpy.jump("nightOne")
            case _:
                return
        return

label nightOne:
    scene night bg
 
    blank "(As you close up shop today, Ilana suddenly opens the door and lets herself in.)"
    
    show Ilana Meh at right
    with dissolve
    
    blank "(Right. She also helps supply your shop with flowers.)"
    blank "(You usually take the time during days where you need to restock to catch up with her, chatting away as she helps you take account of your new inventory.)"
    blank "(Admittedly, you appreciate the company.)"
    peri "Hey, Ilana."
    ilana "Good evening to you too, Peri!"
    blank "(She puts down a new batch of flowers in front of you.)"
    ilana "Here's the flowers you ordered. Should last you the next couple of months?"
    peri "Thanks."
    blank "(You and Ilana begin sorting through the flowers.)"
    ilana "How's the shop doing?"
    peri "Well, for one, it's December. Lots of people are flying here to spend time with their loved ones, so I end up running into a lot of people at the shop."
    ilana "In a good way?"
    peri "Yes, in a good way. There was one guy..."
    ilana "Who..?"
    peri "Nah, I'll tell you about it some other time."
    ilana "Aw, what? Now I wanna know!"
    peri "It's probably nothing."
    ilana "You sure?"
    peri" Yes, I'm sure. It was just one kid, anyways."
    peri "Mind helping me sort through these ones? It's kinda hard to distinguish Carnation from Hydrangea, especially in this light."
    ilana "Fine, fine..."
    blank "(You and Ilana continue sorting through the flowers.)"
    blank "(Work days in December were always kind of long. You signed up to sell gifts right next to an airport, so you knew about this beforehand.)"
    blank "(Still, you feel like you're always never prepared for the amount of customers you'd end up getting.)"
    blank "(As such, you've always found the closing time during these hectic days a little comforting.)"
    blank "(You end up talking to Ilana about anything at all, as your inventory is restocked for the months to come.)"
    
    $ day = day + 1
    $ dayShift()

