init python:
    def nightShift():
        renpy.force_autosave(take_screenshot=True, block=False)
        match day:
            case 1:
                renpy.jump("nightOne")
            case 2:
                renpy.jump("nightTwo")
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

label nightTwo:
    scene night bg

    show Ilana Meh at right
    with dissolve

    ilana "I'm coming in!"
    peri "Hello, again."
    blank "(Ilana once again puts down a new set of flowers by your side.)"
    ilana "So... how's work?"
    peri "Pretty good. Interesting, more like."
    ilana "Oh? How so?"
    peri "Remember that kid I told you about back in December?"
    ilana "Yeah...?"
    peri "It seems he and this other kid have a bit of a... rivalry?"
    ilana "Oh no! Are they both warriors, fighting for the love of a beautiful princess?"
    peri "Not like that at all? It's more... they're giving each other bad bouquets."
    ilana "How can a bouquet be bad?"
    peri "Like, bad as in the "I hate you and want you to die" bad."
    ilana "Yeesh! You think it's a breakup?"
    peri "I tried to ask, but the first kid just ran off after I handed him the bouquet."
    ilana "Weird... A bouquet of flowers to express hatred..."
    peri "Of all things, right?"
    ilana "At least he paid, huh....?"
    peri "Yeah, at least..."
    blank "(You wince a bit. He seemed so upset when he came in...)"
    peri "Anyways, the other kid came in today."
    ilana "And...?"
    peri "Turns out the rivalry is a kind of academic one. Both of them go to competitions, olympiads, those kinds of things. Representing their school and all."
    peri "The rivalry stems because they both want to one-up each other.\nThe reason the first kid bought a bouquet in the first place was because the other kid beat him. Once."
    ilana "That's petty!"
    peri "I know, right?"
    blank "(You're distracted a bit by the conversation topic. You soon continue unloading the flowers.)"
    ilana "Anyone else?"
    peri "Someone came in today to buy flowers for his mom's grave."
    ilana "Oh no... I hope he's well..."
    peri "Seems this is a thing he does every time he comes back. I get why you'd be concerned, though... must be hard."
    peri "There was another customer a while back, who bought a bouquet for her sick friend."
    ilana "As a "get-well-soon" gift, I hope?"
    peri "Seems like it."
    ilana "Aww, that's really nice! Glad there are some people out there who remember what bouquets are for."
    blank "(Right... right...)"
    blank "(The two rivals, the son, and the friend... all of them have different reasons for buying bouquets.)"
    blank "(Some, admittedly more reasonable than others, but you choose to hold that thought for now.)"
    blank "(Flowers mean a lot of different things, and that's part of why you found an interest in taking up something like this.)"
    blank "(It's fun to think about.)"
    blank "..."
    blank "(You and Ilana continue sorting the flowers.)"

    $ day = day + 1
    $ dayShift()
