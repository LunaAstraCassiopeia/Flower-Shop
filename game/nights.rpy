init python:
    def nightShift():
        renpy.force_autosave(take_screenshot=True, block=False)
        match day:
            case 1:
                renpy.jump("nightOne")
            case 2:
                renpy.jump("nightTwo")
            case 3:
                renpy.jump("nightThree")
            case 4:
                renpy.jump("nightFour")
            case 5:
                renpy.jump("nightFive")
            case _:
                return
        return

transform tint_blue:
    matrixcolor TintMatrix("#8882bd")

label nightOne:
    scene night bg
    with long_dissolve
    play music "departures.mp3" fadein 1 fadeout 0.5 if_changed loop volume 0.75

    blank "(As you close up shop today, Ilana suddenly opens the door and lets herself in.)"
    
    show Ilana Meh at tint_blue, center
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

    hide Ilana
    with dissolve

    stop music fadeout 1

    scene black
    with long_dissolve
    
    $ day = day + 1
    $ dayShift()

label nightTwo:
    scene night bg
    with long_dissolve
    play music "departures.mp3" fadein 1 fadeout 0.5 if_changed loop volume 0.75

    show Ilana Meh at tint_blue, center
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
    peri "Like, bad as in the \"I hate you and want you to die\" bad."
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
    ilana "As a \"get-well-soon\" gift, I hope?"
    peri "Seems like it."
    ilana "Aww, that's really nice! Glad there are some people out there who remember what bouquets are for."
    blank "(Right... right...)"
    blank "(The two rivals, the son, and the friend... all of them have different reasons for buying bouquets.)"
    blank "(Some, admittedly more reasonable than others, but you choose to hold that thought for now.)"
    blank "(Flowers mean a lot of different things, and that's part of why you found an interest in taking up something like this.)"
    blank "(It's fun to think about.)"
    blank "..."

    scene black
    with long_dissolve
    stop music fadeout 1

    blank "(You and Ilana continue sorting the flowers.)"

    hide Ilana
    with dissolve

    $ day = day + 1
    $ dayShift()

label nightThree:
    scene night bg
    with long_dissolve
    stop music fadeout 0.5

    blank "(Huh...)"
    peri "Ilana should be here by now..."
    blank "(You look around, and see...)"
    blank "(...no one...?)"
    peri "Maybe she's just late..."

    scene black 

    blank "(Having been forced to be left to your own devices, you write down all the orders you got today. You turn around, facing away from the shop's entrance for a second, when suddenly...)"

    scene night bg
    show Ilana Hehe at tint_blue, center
    play music "departures.mp3" fadein 0.5 volume 0.75

    ilana "SPECIAL DELIVERY!"
    peri "AAAHH?!"
    blank "(Ilana slams the door wide open. You can't help but flinch a little.)"
    peri "Don't do that! You could've..."
    ilana "Heh, sorry! Was I too loud?"
    peri "Kind of..."
    blank "(Ilana sets down the flowers as she comes in.)"

    show Ilana Meh at tint_blue, center

    ilana "Here you are, Miss Peri."
    blank "(...since when was she allowed to call you that?)"
    blank "(Anyways, you two begin sorting the flowers once again.)"
    ilana "So..."
    blank "(...)"
    ilana "How are you?"
    peri "Work's been well, I suppose. I'm meeting more regulars than I thought I ever would..."
    ilana "Regulars? As in, people who visit you frequently?"
    peri "Yeah?"
    ilana "Those nerds bother you again?"
    peri "Yeah... I really can't help but wonder why they choose to hate on each other like this."
    peri "Like, there has to be better ways to express your hatred for someone."
    ilana "Are they in love?"
    blank "(...)"
    blank "(...as farfetched as that is...)"
    peri "Who knows?"
    blank "(...changing the topic)"
    peri "I saw Mark again today, too. The one buying flowers for his mom."
    ilana "Right..."
    ilana "...and how about you? You been doing okay?"
    peri "Hm?"
    peri "I've been alright, I suppose. Things are getting busy again, is all."
    blank "(Silence fills the air between you two as you continue unloading the flowers.)"
    ilana "Say..."
    ilana "Do you do anything after work?"
    peri "What's that supposed to mean?"
    peri "It's not like I'm some shut-in, spending her entire life in this flower shop..."

    show Ilana Sucks Ass at tint_blue, center

    ilana "Hey, you know I didn't mean it like that!"
    blank "(You giggle playfully. Ilana gives you a kind of mean look.)"
    peri "I write."

    show Ilana Meh at tint_blue, center

    ilana "Like, books? You're an author?"
    peri "Not specifically... I mostly tend to journal. Write about my experiences in the shop, you know..."
    peri "Though, I do like reading in my spare time too. I've tried writing some prose every now and then, but not enough to really get anywhere with it."
    ilana "Oho?"
    ilana "You should show me some of your writing sometime! I think you'd be great at it."

    show Ilana Happy at tint_blue, center

    blank "(You blush.)"
    peri "Not a chance."
    ilana "Come on!"
    peri "No!"

    show Ilana Hehe at tint_blue, center

    ilana "You know you want to!"
    peri "I do not!"
    blank "(The two of you tease each other on for a little longer.)"
    ilana "Say..."
    
    show Ilana Meh at tint_blue, center

    ilana "Do you wanna hang out sometime? Like, outside of work?"
    peri "If it gets you to shut up about my writing, then sure."
    ilana "I know a few spots near the airport. Cafes, bars, restaurants... I'd love to try some of them out with you."
    peri "That does sound nice..."

    show Ilana Happy at tint_blue, center

    ilana "It's a date, then! Sometime after we finish restocking, perhaps?"
    peri "Yeah."
    blank "(You continue sorting the flowers, Ilana joining you not long after.)"

    scene black
    with long_dissolve
    stop music fadeout 1

    blank "(She keeps insisting that you show her your writing.)"

    $ day = day + 1
    $ dayShift()
    
label nightFour:
    scene night bg
    with long_dissolve
    play music "departures.mp3" fadein 0.5 fadeout 0.5 if_changed loop volume 0.75

    show Ilana Meh at tint_blue, center
    with dissolve
    
    ilana "Coming in."
    peri "Hello."
    blank "(As usual, Ilana places the box of flowers by your side.)"
    blank "(You open the box, and the two of you begin unloading flowers.)"
    blank "..."
    blank "(The air gets awfully quiet in the shop.)"
    blank "(By now, you know to expect Ilana to ask you how your day went.)"
    blank "(You have an answer to it, even.)"
    blank "(But somehow, that question never comes.)"
    blank "(After some time, Ilana suddenly glances towards you.)"

    show Ilana Sucks Ass at tint_blue, center

    ilana "Could I ask you something?"
    peri "What's up? Are you... okay?"

    show Ilana Meh at tint_blue, center

    ilana "No, no, I'm fine, I swear!"
    blank "(She scratches the back of her head and smiles at you, as if to ensure she's doing alright.)"
    ilana "There's just... something I've been meaning to ask you."
    peri "What is it?"
    ilana "Why'd you choose to set up shop here? Near an airport of all places?"
    ilana "And why flowers?"
    peri "Well..."
    blank "(You ponder over it for a moment.)"
    peri "I guess I started selling flowers and bouquets because of the amount of depth and meaning that goes into each one."
    peri "The idea of a bouquet conveying a personal message, that of which you'll find out about by understanding what each individual flower represent..."

    show Ilana Happy at tint_blue, center

    peri "The idea of that is... amazing, to me."
    peri "You would know, I think. You gave me that manual, after all."
    blank "(You notice Ilana smiling until you attempt to make eye contact with her, after which she looks away and starts... blushing?)"

    show Ilana Sucks Ass at tint_blue, center

    peri "I opened a flower shop near the airport, because..."
    blank "(You think back to all the people you've gotten to know. Arthur, Reuben, Kara, Mark...)"
    peri "I think... the people I've gotten to know while working here have always been nice to hear from."
    peri "Knowing why they're buying flowers, hearing about them and how these reasons change over time, figuring out what they want to convey with them..."
    peri "...I guess what I'm trying to say is, I like hearing the stories people have, and what motivates them to come to the shop and buy things."
    blank "(The atmosphere in the room seems to loosen up a bit.)"

    show Ilana Meh at tint_blue, center

    peri "What about you? Why do you keep coming back to restock for this flower shop in particular?"
    ilana "Not important."
    peri "You sure....?"
    ilana "Noooooot important."
    blank "(You laugh a bit, but try your best to hide it from Ilana.)"
    blank "(Does she really not have any ulterior motives for coming here all the time?)"
    blank "(You're not sure.)"
    blank "(Either way, seeing her come into the flower shop, chatting with you as you two sort out the new restock she bought, just hearing from her, even if it only happens every few months...)"
    blank "(You enjoy her company.)"

    scene black
    with long_dissolve
    stop music fadeout 1
    blank "(You get the feeling that she appreciates yours, too.)"


    $ day = day + 1
    $ dayShift()

    
    
label nightFive:
    scene night bg
    with long_dissolve
    stop music fadeout 1

    show Ilana Hehe at tint_blue, center
    with dissolve

    ilana "I'm coming in!"
    blank "(Ilana shuffles into the shop, putting down a fresh batch of flowers near you once again.)"

    show Ilana Meh at tint_blue, center

    peri "Should we start?"
    ilana "Not yet. I..."
    ilana "I have something to show you, first."

    hide Ilana Meh 
    with dissolve

    blank "(Ilana exits the store.)"
    blank "(Somewhere in the distance, you hear muffled noises of a car door opening, and someone reaching into what you can only assume is somewhere in the passenger seat, to grab something.)"
    blank "(...)"
    blank "(Not long after, Ilana comes back into the store. Her hands are behind her back, seemingly to hide something?)"

    play music "departures.mp3" fadein 0.5 fadeout 0.5 if_changed loop volume 0.75

    show Ilana Happy at tint_blue, center

    peri "What's all this about..."

    show Ilana Sucks Ass at tint_blue, center

    blank "(You can see Ilana tense up a bit, before responding.)"

    show Ilana Meh at tint_blue, center

    ilana "I've been thinking, a bit."
    ilana "About this flower shop, about the people who go to it, and about..."
    ilana "...you."
    ilana "And I'm starting to realize how much this flower shop must mean to you."
    ilana "All the stories I've heard from you, all the people you've met..."
    ilana "It has to be nice, right? Being a part of something as grand, yet humble and down-to-earth as this."
    ilana "What I'm trying to say is..."
    ilana "You said you liked hearing about the stories people have whenever you meet them, here, in the flower shop."
    ilana "..."

    show Ilana Happy at tint_blue, center

    stop music fadeout 2.0

    ilana "And I like hearing about these stories from you."
    ilana "So... here."

    scene black
    with dissolve
    blank "(Ilana finally reveals what she's been hiding behind her back this entire time.)"

    play music "flight.mp3" if_changed loop volume 0.75
    scene ilana gift 
    with long_dissolve
    pause 1.0

    ilana "I know, I know, this is a bouquet that I bought from YOU, but..."
    ilana "I want you to have this."
    peri "...!"
    blank "(Inspecting the bouquet with your hands, you realize that there's a small necklace hidden inside.)"
    blank "(The necklace just barely fits you, and on its center looks to be a rock, carved out into the shape of a flower.)"
    peri "Th- thank you! You shouldn't have-!"
    ilana "It's okay, really...!"
    ilana "I hope you look at both of these and remember all the love you've managed to spread to everyone."
    ilana "To me, if nothing else."
    blank "(You can't help but tear up. Ilana pulls you into an embrace, and you hug her tightly in return.)"
    ilana "Now, come on. We still have these flowers to sort through, yeah?"
    blank "(You hug Ilana again, trying to regain your composure as you begin sorting through these flowers again, as usual.)"
    blank "(...)"

    scene black
    with long_dissolve
    stop music fadeout 1

    $ ending_score = total_satisfaction / 25
    if ending_score <= 0.6: # Good End
        blank "(The next few months couldn't have went any more differently.)"
        blank "(Guess it comes with the fact that your shop is in an airport, right?)"
        blank "(You meet a lot of new faces, people who come and go for a variety of different reasons...)"
        blank "(Some of them still come back. Arthur came in a week ago to buy flowers for Reuben.)"
        blank "(Kara took her friend to visit your shop. She's quite nice.)"
        blank "(Mark's family still comes, despite not needing to fly out anymore. His kids insist on getting a bouquet full of bluebells.)"


    if 0.6 < ending_score <= 1: # Meh End
        blank "(The next few months, though fulfilling in their own right, also feel a little stagnant.)"
        blank "(You get a few new faces, even those that come back again.)"
        blank "(More new stories to hear about, and more to help grow.)"
        blank "(You note that some of them don't show up again, and that's okay!)"
        blank "(You're in an airport, and all. Not everyone needs to be going back here.)"

    if 1 < ending_score:
        blank "(...and admittedly, you might need a bit more help with these flowers than you thought you would.)"
        blank "(Ilana comes back, way more than usual, to quiz you on that manual.)"
        blank "(Surely, after some time, you'd get better at it.)"
        blank "(And you did!)"

    blank "(But no matter what, you end up helping them growing a part of your customers' stories.)"
    blank "(Every single time, you help them reach their dreams.)"
    blank "(Even just a little more.)"

    stop music fadeout 0.5

    jump end_credits