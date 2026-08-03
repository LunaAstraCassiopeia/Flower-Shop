# define character sprites here
image Tomura Happy = "Tomura/Tomura Happy.png"
image Tomura Meh = "Tomura/Tomura Meh.png"
image Tomura Sucks Ass = "Tomura/Tomura Sucks Ass.png"

image Ilana Meh = "Ilana/Ilana Meh.png"
image Ilana Happy = "Ilana/Ilana Happy.png"
image Ilana Sucks Ass = "Ilana/Ilana Sucks Ass.png"
image Ilana Hehe = "Ilana/Ilana Hehe.png"

image Arthur Meh = "Arthur/Arthur Meh.png"
image Arthur Happy = "Arthur/Arthur Happy.png"
image Arthur Sucks Ass = "Arthur/Arthur Sucks Ass.png"
image Arthur Sucks Ass Blush = "Arthur/Arthur Sucks Ass 2.png"
image Arthur Happy Blush = "Arthur/Arthur Happy 2.png"

image Kara Meh = "Kara/Kara Meh.png"
image Kara Happy = "Kara/Kara Happy.png"
image Kara Sucks Ass = "Kara/Kara Sucks Ass.png"

image Reuben Meh = "Reuben/Reuben Meh.png"
image Reuben Happy = "Reuben/Reuben Happy.png"
image Reuben Sucks Ass = "Reuben/Reuben Sucks Ass.png"
image Reuben Sucks Ass Blush = "Reuben/Reuben Sucks Ass 2.png"
image Reuben Happy Blush = "Reuben/Reuben Happy 2.png"

image Mark Meh = "Mark/Mark Meh.png"
image Mark Happy = "Mark/Mark Happy.png"
image Mark Sucks Ass = "Mark/Mark Sucks Ass.png"

image Tour Meh = "Tour Telle/Tour Telle Meh.png"
image Tour Happy = "Tour Telle/Tour Telle Meh.png"
image Tour Sucks Ass = "Tour Telle/Tour Telle Meh.png"

image Clove Meh = "Clove/Clove Meh.png"
image Clove Happy = "Clove/Clove Happy.png"
image Clove Sucks Ass = "Clove/Clove Sucks Ass.png"

image Avery Meh = "Avery/Avery Meh.png"
image Avery Happy = "Avery/Avery Happy.png"
image Avery Sucks Ass = "Avery/Avery Sucks Ass.png"

image Floweri Meh = "Floweri/Floweri Meh.png"
image Floweri Happy = "Floweri/Floweri Happy.png"
image Floweri Sucks Ass = "Floweri/Floweri Sucks Ass.png"

image Oliver Meh = "Oliver/Oliver Meh.png"
image Oliver Happy = "Oliver/Oliver Happy.png"
image Oliver Sucks Ass = "Oliver/Oliver Sucks Ass.png"

# all instances of customers are defined here.
init python:
    import random

    def blip_voice(event, interact=True, blip_file = "mid blip", **kwargs):
        if event == "show_done":
            blips = make_blips(blip_file)
            renpy.sound.play(blips, loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
    
    def make_blips(filename = "mid blip", **kwargs):
        blips = []
        for x in range(10):
            blips.append((filename + " " + str(random.randint(1,3)) + ".mp3"))
        return blips

    blank = Character("", callback=blip_voice, cb_blip_file = "mid blip")
    peri = Character("Periwinkle", callback=blip_voice, cb_blip_file = "high blip")
    ilana = Character("Ilana", callback=blip_voice, cb_blip_file = "mid blip")
    arthur = Character("Arthur", callback=blip_voice, cb_blip_file = "low blip")
    reuben = Character("Reuben", callback=blip_voice, cb_blip_file = "high blip")
    kara = Character("Kara", callback=blip_voice, cb_blip_file = "mid blip")
    mark = Character("Mark", callback=blip_voice, cb_blip_file = "low blip")
    clove = Character("Clove", callback=blip_voice, cb_blip_file = "mid blip")
    tour = Character("Tour Telle", callback=blip_voice, cb_blip_file = "low blip")
    tomi = Character("Tomura", callback=blip_voice, cb_blip_file = "mid blip")
    avery = Character("Avery", callback=blip_voice, cb_blip_file="high blip")
    floweri = Character("Floweri" callback=blip_voice, cb_blip_file="low blip")
    oliver = Character("Oliver" callback=blip_voice, cb_blip_file="low blip")
    mich = Character("Michelle", callback=blip_voice, cb_blip_file = "mid blip")
    mika = Character("Mikaela", callback=blip_voice, cb_blip_file = "high blip")
    mike = Character("Mike", callback=blip_voice, cb_blip_file = "high blip")


    # all ilana instances!
    
    ilanaTutorialWants = {"Orchid": 7}
    noPreferences = {"test": 0}
    ilanaTutorialEnter = ["Those flowers... I forget what they're called...", "The, uh, white ones?", "About innocence and new beginnings and stuff...", "Give me an entire bouquet of those. Seven of 'em.", "...", "Don't just stare at me like that! Use your manual to figure out what I mean!", "BL:{cps=0}(Pick out flowers by selecting them on the left, then click on their stems to give the customer their bouquet! You can click on flowers to remove them from the bouquet.)"]
    ilanaTutorialExit = {
        "Happy": ["There you go.", "Exactly what I asked.", "Told you you should've kept that book safe!", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
        "Meh": ["I mean... you're kind of there?", "I told you I wanted more of those white ones, right?", "Ah, well. At least you got halfway there.", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
        "Sucks Ass": ["...This isn't what I asked for?", "...Like, at all?", "You're doing this on purpose, aren't you?", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
    }
    IlanaTutorialCustomer = Customer(ilanaTutorialWants, noPreferences, ilana, ilanaTutorialEnter, ilanaTutorialExit, "Ilana", False)
    
    ilanaGiftWants = {"Rose": 2, "Hydrangea": 1, "Forget-Me-Not": 3, "Bluebell": 1}
    ilanaGiftPreferences = {"Bluebell": -0.1, "Hydrangea": -0.1}
    ilanaGiftEnter = ["Hey!", "BL:(???)", "What?", "Can't show up in the morning or something?", "Look. I'm picking something up for someone.", "Someone I find to be a stable constant in my life, ever since we met.", "Someone who goes on and on about the stories they hear about from people.", "Someone... kinda special to me, y'know?", "...", "Do whatever you want! I'm sure they'll appreciate it."]
    ilanaGiftExit = {
        "Happy": ["BL:(Ilana studies your bouquet intently, and towards the end grins to herself.)", "You really know your stuff, don't you?", "BL:(And with not a single word more, she leaves the shop.)", "I'll be back tonight!"],
        "Meh": ["BL:(After looking at your bouquet, Ilana nods.)", "Yeah. This'll do.", "BL:(She mumbles.)", "I mean, if it's your flowers, right?", "I'll be back tonight!"],
        "Sucks Ass": ["BL:(Ilana chuckles a little.)", "BL:(Her mouth moves very subtly, as if trying to whisper something.)", "Really...?", "That book I gave you... do you ever use it?", "Or is this really what you want to say?", "BL:(Ilana turns around.)", "BL:(Almost out of the corner of your eye, you see Ilana grin as she leaves the shop.)", "Well, I can't say you picked anything bad.", "I'll be back tonight!"],
    }
    IlanaGiftCustomer = Customer(ilanaGiftWants, ilanaGiftPreferences, ilana, ilanaGiftEnter, ilanaGiftExit, "Ilana", False)

    # all arthur instances!
    
    arthurOneWants = {"Lily": 4, "Orchid": 2, "Hydrangea": 1}
    arthurOneEnter = ["Hey. This is that one shop... right? With, the flowers?", "BL:(You're not sure what other flower shops are there. Nearby, at least.)", "Bit of a strange ask, but... give me the worst bouquet you can think of.", "BL:(...?)", "I'm thinking of... hatred, spite, wishing this person was dead. Maybe something to remind them that I'm better than them."]
    arthurOneExit = {
        "Happy": ["Perfect.", "This guy's not dumb, he'll know what I mean with these."],
        "Meh": ["This will have to do.", "I don't think it'll fully get the point across, but it will have to suffice."],
        "Sucks Ass": ["...", "Is this not the exact opposite of what I said I wanted?"],
    }
    ArthurOneCustomer = Customer(arthurOneWants, noPreferences, arthur, arthurOneEnter, arthurOneExit, "Arthur", True)
    
    arthurTwoWants = {"Lily": 2, "Orchid": 2, "Hydrangea": 2, "Hyacinth": 1}
    arthurTwoEnter = ["You.", "BL:(Him again?)", "You've met Reuben?", "BL:(You have.)", "Ugh, that guy. Trying to take the moral high ground, as always.", "BL:(You're not sure whether to agree or disagree here.)", "BL:(Probably disagree.)", "Give me the same bouquet. Flowers that convey hate, death, and the fact that I'm superior to him. And maybe a flower that tells him that I'm envious of him."]
    arthurTwoExit = {
        "Happy": ["Perfect.", "This will show him."],
        "Meh": ["This will have to do.", "I don't think it'll get my whole point across, but it will have to suffice."],
        "Sucks Ass": ["...", "Are you trying to make me look like a fool?", "In front of Him?"],
    }
    ArthurTwoCustomer = Customer(arthurTwoWants, noPreferences, arthur, arthurTwoEnter, arthurTwoExit, "Arthur", True)
    
    # all kara instances!
    
    karaOneWants = {"Carnation": 4, "Bluebell": 3}
    karaPreferences = {"Rose": 0.2}
    karaOneEnter = ["Hello!", "I'm not sure what flowers I think she'd like, but...", "...I have a friend who really likes pink flowers!", "I would like some of those, along with ones that generally convey gratitude."]
    karaOneExit = {
        "Happy": ["Oh! I think she'd like these ones, yeah!", "These will cheer her up, definitely!"],
        "Meh": ["Ah!", "I think this could work!", "Could use a little more, but I think she'd like this nonetheless."],
        "Sucks Ass": ["Hmm...", "It's an honest effort, at least!", "I'm not sure if she'd like these, but it's worth a shot!"],
    }

    KaraOneCustomer = Customer(karaOneWants, karaPreferences, kara, karaOneEnter, karaOneExit, "Kara", True)
    
    karaTwoWants = {"Carnation": 4, "Bluebell": 2, "Forget-Me-Not": 1}
    karaTwoEnter = ["Hi! It's me again...", "Do you remember that order from last time?", "Just that same one, again... maybe with something different, this time.", "Some more pink flowers, those accent ones and maybe a single flower that expresses some kind of love and remembrance would be nice."]
    karaTwoExit = {
        "Happy": ["Yes, these ones! She'll like this a lot!", "This will liven up her room a ton!"],
        "Meh": ["Oh, this will do!", "Maybe it could use a bit more work, but...", "It'll do nicely next to her bed!"],
        "Sucks Ass": ["I'm not sure if this is what she wants...", "It's pretty nice, though! I'll give it anyways!"],
    }

    KaraTwoCustomer = Customer(karaTwoWants, karaPreferences, kara, karaTwoEnter, karaTwoExit, "Kara", True)

    karaThreeWants = {"Carnation": 2, "Bluebell": 1, "Forget-Me-Not": 2, "Hydrangea": 2}
    karaThreeEnter = ["Hi!!", "I'd like the same order again, please!", "Oh, but maybe add more variety and color?", "I want something special, extravagant! Something to express my love and gratitude!"]
    karaThreeExit = {
        "Happy": ["These are great! I'm sure she'd love this!", "I can't wait to give them to her..."],
        "Meh": ["Oh! These are nice...", "Not entirely what I had in mind, but...", "I think she'll like them anyways!"],
        "Sucks Ass": ["Mmm...", "Would these really be the best for today..?", "I trust your judgement, I hope she likes them!"],
    }
    KaraThreeCustomer = Customer(karaThreeWants, karaPreferences, kara, karaThreeEnter, karaThreeExit, "Kara", True)

    # all mark instances!
    
    markOneWants = {"Carnation": 4, "Forget-Me-Not": 3}
    markPreferences = {"Orchid": -0.1}
    markOneEnter = ["Hello.", "Is this a new shop? Can't help but feel like I haven't seen this before, haha.", "BL:(You nod.)", "I see.", "Could I have a bouquet for my mother? I plan to visit her grave while I'm here, and would like to honor her memory."]
    markOneExit = {
        "Happy": ["Ah.", "This bouquet is perfect.", "She always did like these flowers."],
        "Meh": ["Mmm.", "These work.", "Not entirely what I had in mind, but you got there anyhow."],
        "Sucks Ass": ["Oh...", "Are you also new here?", "BL:(You flinch.)", "Haha, it's okay. Stuff like this does take a while to get used to.", "You'll get better at it."],
    }
    MarkOneCustomer = Customer(markOneWants, markPreferences, mark, markOneEnter, markOneExit, "Mark", True)
    
    markTwoWants = {"Carnation": 3, "Forget-Me-Not": 2, "Orchid": 2}
    markTwoEnter = ["Hello, again.", "I'd like the same bouquet, the one I meant for my mother.", "Although this time, I'd like a few different flowers. Those white orchids, could I have two of those?"]
    markTwoExit = {
        "Happy": ["Ah.", "This bouquet is perfect.", "Both for her, and for the rest of us."],
        "Meh": ["Mmm.", "These work.", "Not entirely what I had in mind, but you got there anyhow."],
        "Sucks Ass": ["Oh...", "I think you could have done a better bouquet here.", "Not that I don't trust your intentions, of course.", "I'll give this to her anyways."],
    }
    MarkTwoCustomer = Customer(markTwoWants, noPreferences, mark, markTwoEnter, markTwoExit, "Mark", True)
    
    markThreeWants = {"Carnation": 1, "Orchid": 2, "Forget-Me-Not": 2, "Bluebell": 2}
    markThreeEnter = ["Hi!", "I'd like a bouquet again, but...", "This time it's for my family.", "I'd like more of those orchids, if you still have those. I know my kids also like a lot of blue flowers, and I'd still like for flowers to give to my mother."]
    markThreeExit = {
        "Happy": ["Ah.", "This bouquet is perfect.", "I just know all of them will love this."],
        "Meh": ["Mmm.", "These work.", "Not entirely what I had in mind, but you got there anyhow."],
        "Sucks Ass": ["Oh...", "I think you could have done a bit better here.", "I know that I should leave it to the professionals, but...", "I'll give these to them anyways."],
    }
    MarkThreeCustomer = Customer(markThreeWants, noPreferences, mark, markThreeEnter, markThreeExit, "Mark", True)

    # all reuben instances!
    
    reubenOneWants = {"Lily": 4, "Hyacinth": 3}
    reubenOneEnter = ["You... you're the flower shop, right?", "BL:(Not THE flower shop. But yes.)", "A few months ago, did you come across a guy? One who wanted a hateful, overall negative bouquet?", "Ugh, I hate that guy! Just because I beat him in an olympiad doesn't mean he gets to do that!", "Seriously, what's wrong with him?", "I want a bouquet too. One with much of the same message, without the \"wanting to die\" part."]
    reubenOneExit = {
        "Happy": ["Thank you very much.", "Apologies for the trouble... I really do hope you don't have to run into him again."],
        "Meh": ["It's okay... This is okay.", "I know these bouquets with negative connotations aren't really what... these are for.", "Thank you for trying, anyways."],
        "Sucks Ass": ["...", "This won't do...", "I'll probably give this to someone else. Someone I actually like.", "Thank you, still. I'll try to make sure this doesn't go to waste."],
    }
    ReubenOneCustomer = Customer(reubenOneWants, noPreferences, reuben, reubenOneEnter, reubenOneExit, "Reuben", True)
    
    reubenTwoWants = {"Lily": 3,"Rose": 2, "Hyacinth": 2, "Stick": 1}
    reubenTwoEnter = ["BL:(Him again...)", "BL:Yeah, same as last time.", "BL:(While you're working, he begins ranting to himself...)", "He's just been the bane of my existence! A thorn in my side! A stick in the mud! I envy him so much."]
    reubenTwoExit = {
        "Happy": ["Thank you, again.", "Apologies for the ranting... I can't believe I had to do this again..."],
        "Meh": ["It's okay... This is okay.", "Sorry, I know I wasn't really specific with my request. I was just...", "Thank you, this will still work."],
        "Sucks Ass": ["...", "This isn't right...", "Maybe you mistook me as someone else... I wanted something for someone I hate.", "Thank you, still. I'll try to make sure this doesn't go to waste."],
    }
    ReubenTwoCustomer = Customer(reubenTwoWants, noPreferences, reuben, reubenTwoEnter, reubenTwoExit, "Reuben", True)

    reubenThreeWants = {"Rose": 3, "Lily": 3, "Hydrangea": 1}
    reubenThreeEnter = ["BL:(Oh God, again?)", "Hi.", "BL:(Here it comes...)", "I need... a different set of flowers, this time.", "BL:(...?)", "Still for the same guy, just...", "I want to make an honest effort to make amends with him.", "I want to tell Arthur that I recognize his passion, but not in a way that makes me envious of him. Two different kinds of flowers that convey those, and a final one that tells him that I want to understand him."]
    reubenThreeExit = {
        "Happy": ["Thank you.", "I hope he takes this well..."],
        "Meh": ["It's okay... This is okay.", "Sorry, I know this comes off as strange coming from me...", "Thank you, this will still work."],
        "Sucks Ass": ["...", "Look. I recall saying I don't hate him anymore.", "...", "What? I'm serious!"],
    }
    ReubenThreeCustomer = Customer(reubenThreeWants, noPreferences, reuben, reubenThreeEnter, reubenThreeExit, "Reuben", True)

    # MINOR CHARACTERS START HERE

    # All Tour Telle instances
    
    tourOneWants = {"Rose": 7, "Leaf": 1}
    tourOnePreferences = {"Rose": -0.2}
    tourOneEnter = ["BL:(This is just a turtle.)", "BL:(Another turtle pokes out of the right sleeve and hands you a paper.)", "BL:(It's kind of gross, but you can barely make out a drawing of a leaf. And... something red....?)"]
    tourOneExit = {
        "Happy": [":>"],
        "Meh": [":|"],
        "Sucks Ass": [":{"],
    }
    TourOneCustomer = Customer(tourOneWants, tourOnePreferences, tour, tourOneEnter, tourOneExit, "Tour", False)

    tourTwoWants = {"Lily": 7, "Leaf": 1}
    tourTwoPreferences = {"Lily": -0.2}
    tourTwoEnter = ["BL:(Those damned turtles are BACK???)", "BL:(Tortoises?)", "BL:(You don't have the energy to recall the technicalities of it.)", "BL:(You're handed another sheet of paper.)", "BL:(This time, there's a drawing of a yellow cat, with claw markings on its face.)"]
    tourTwoExit = {
        "Happy": [">:-3"],
        "Meh": [":|"],
        "Sucks Ass": [">:("],
    }
    TourTwoCustomer = Customer(tourTwoWants, tourTwoPreferences, tour, tourTwoEnter, tourTwoExit, "Tour", False)

    # All Clove instances
    
    cloveOneWants = {"Carnation": 3, "Rose": 3, "Bluebell": 1}
    cloveOneEnter = ["Hello there! Haha, this is a really lovely shop. I love what you've done here!", "It really… Okay, gotta focus!", "My boyfriend's gonna come back from a fencing competition really far from here in an hour, and I really wanna surprise him with a nice bouquet!", "Usually, I'd use my own flowers, but it's not their season, I guess.", "I'd like a bouquet that says \"Congratulations, love!\". Could you do that for me?"]
    cloveOneExit = {
        "Happy": ["Oh!! This is perfect!", "Cinthus will love this! Thanks a bunch!"],
        "Meh": ["Mhm, this is good!", "Thank you!"],
        "Sucks Ass": ["Ah... Hm...", "This'll be nice, I think..."],
    }
    CloveOneCustomer= Customer(cloveOneWants, noPreferences, clove, cloveOneEnter, cloveOneExit, "Clove", True)

    cloveTwoWants = {"Carnation": 3, "Orchid": 3, "Bluebell": 1}
    cloveTwoEnter = [
        "Hi again! Guess who forgot to get a gift, haha…", 
        "This isn’t for my boyfriend this time, it’s for another friend of mine!", 
        "She’ll be coming back from work for the first time in a few months, so I wanna get her something nifty.", 
        "If I’d remembered earlier, I would’ve probably gifted her something more practical, but…", 
        "All’s well that ends well, right?",
        "Anyway! I have a more specific message I’d like to give her: “Congrats on your new job, and thanks for taking the time to come back!"]
    cloveTwoExit = {
        "Happy": ["Oh!! This is perfect!", "Es will definitely appreciate this! Thanks a bunch!"],
        "Meh": ["Mhm, this is good!", "Thank you!"],
        "Sucks Ass": ["Ah... Hm...", "This'll be nice, I think..."],
    }
    CloveTwoCustomer= Customer(cloveTwoWants, noPreferences, clove, cloveTwoEnter, cloveTwoExit, "Clove", True)

    # all Tomura instances

    tomiOneWants = {"Forget-Me-Not": 4, "Bluebell": 3}
    tomiOneEnter = ["Hi..!", 
    "I'm planning on visiting a good friend of mine today, one I haven't talked to in a while...", 
    "They like a lot of blue flowers!",
    "They're very good with flower language, and I want a bouquet that conveys how constant they've been in my life, even despite not meeting for a bit...",
    "I hope they never forget me!",
    "Could you help me out?"]
    tomiOneExit = {
        "Happy": ["Oh..!", "I recall them saying they really liked these flowers!", "Thank you so much!"],
        "Meh": ["Ah..?", "You really think they'd like these..?", "Well, thank you regardless."],
        "Sucks Ass": ["Huh...", "Are these really the right flowers for this?"],
    }
    TomiOneCustomer = Customer(tomiOneWants, noPreferences, tomi, tomiOneEnter, tomiOneExit, "Tomura", True)

    tomiTwoWants = {"Carnation": 4, "Bluebell": 3}
    tomiTwoEnter = ["Hello again!", 
    "My friend and I are performing together before I leave again, so I was thinking of getting flowers to celebrate.", 
    "Could you give me something to congratulate us?",
    "Don’t forget– they really like blue!"]
    tomiTwoExit = {
        "Happy": ["Ah!!!", "These are perfect! Thank you!"],
        "Meh": ["Hmm…", "It’s very pretty, but I don’t know if they’d get the message. Thank you still!"],
        "Sucks Ass": ["Huh...", "Are these really the right flowers for this?"],
    }
    TomiTwoCustomer = Customer(tomiTwoWants, noPreferences, tomi, tomiTwoEnter, tomiTwoExit, "Tomura", True)

    # all Avery instances
    
    averyOneWants = {"Orchid": 5, "Vanilla": 2}
    averyOneEnter = [
        "Ooh, is this shop new here?",
        "It's not often I get to see fellow florists, especially not in the wild like this!",
        "BL:(She extends a hand out to you.)",
        "Avery! Nice to meet ya!",
        "BL:(You shake her hand!)",
        "Mind if I test your knowledge a bit?",
        "I'm thinking of... a bouquet like tea. With a bit of vanilla, but not too much."
    ]
    averyOneExit = {
        "Happy": [
            "Yup!",
            "You sure do know your flowers, alright!"
        ],
        "Meh": [
            "Mmm!",
            "Not quite the answer I was looking for, but I see the thought behind this.",
            "Good job!",
        ],
        "Sucks Ass": [
            "...",
            "What kind of tea have you been drinking?",
            "Kidding, I'm kidding! It's okay!",
            "I suppose all teas are kind of floral, anyways.",
        ]
    }
    AveryOneCustomer = Customer(averyOneWants, noPreferences, avery, averyOneEnter, averyOneExit, "Avery", True)

    averyTwoWants = {"Hyacinth": 3, "Bluebell": 2, "Carnation": 2}
    averyTwoEnter = [
        "Heyyy!",
        "Glad to see you around still!",
        "BL:(Like there was a chance you wouldn't be...?)",
        "Mind if I order a weird bouquet again?",
        "BL:(Can you really say no...?)",
        "Three kinds of flowers this time! A bouquet about mythology, folklore, and history, please!",
    ]
    averyTwoExit = {
        "Happy": [
            "Yup!",
            "You sure do know your flowers, alright!"
        ],
        "Meh": [
            "Mmm!",
            "Not quite the answer I was looking for, but I see the thought behind this.",
            "Good job!",
        ],
        "Sucks Ass": [
            "...",
            "What myths have you been reading up on...?",
            "Kidding, I'm kidding! It's okay!",
        ]
    }
    AveryTwoCustomer = Customer(averyTwoWants, noPreferences, avery, averyTwoEnter, averyTwoExit, "Avery", True)

    # all Floweri instances

    floweriOneWants = {"Rose": 1, "Lily": 1, "Hyacinth": 1, "Forget-Me-Not": 1, "Bluebell": 1, "Hydrangea": 1, "Carnation": 1, "Leaf": 1}
    floweriOneEnter = [
        "Hey there!",
        "Lovely shop you have here!",
        "My friend… I’d like to cheer him up. He’s been real down lately.",
        "He loves flowers too! I think a little bit of everything would be nice.",
        "Give me the whole rainbow!",
    ]
    floweriOneExit = {
        "Happy": [
            "All according to plan!",
            "How lovely!",
        ],
        "Meh": [
            "Well, you got it!",
            "Mostly,",
        ],
        "Sucks Ass": [
            "You're eating my flesh with this one!"
        ]
    }
    FloweriOneCustomer = Customer(floweriOneWants, noPreferences, floweri, floweriOneEnter, floweriOneExit, "Floweri", True)

    floweriTwoWants = {"Rose": 1, "Lily": 1, "Hyacinth": 1, "Forget-Me-Not": 1, "Bluebell": 1, "Hydrangea": 1, "Carnation": 1, "Leaf": 1}
    floweriTwoEnter = [
        "Hey there!",
        "Lovely shop you have here!",
        "My friend… I’d like to cheer him up. He’s been real down lately.",
        "He loves flowers too! I think a little bit of everything would be nice.",
        "Give me the whole rainbow!",
    ]
    floweriTwoExit = {
        "Happy": [
            "All according to plan!",
            "How lovely!",
        ],
        "Meh": [
            "Well, you got it!",
            "Mostly,",
        ],
        "Sucks Ass": [
            "You're eating my flesh with this one!"
        ]
    }
    FloweriTwoCustomer = Customer(floweriTwoWants, noPreferences, floweri, floweriTwoEnter, floweriTwoExit, "Floweri", True)

    # all Oliver instances

    oliverOneWants = {"Rose": 1, "Lily": 1, "Hyacinth": 1, "Forget-Me-Not": 1, "Bluebell": 1, "Hydrangea": 1, "Carnation": 1, "Leaf": 1}
    oliverOneEnter = [
        "Hey there!",
        "Lovely shop you have here!",
        "My friend… I’d like to cheer him up. He’s been real down lately.",
        "He loves flowers too! I think a little bit of everything would be nice.",
        "Give me the whole rainbow!",
    ]
    oliverOneExit = {
        "Happy": [
            "All according to plan!",
            "How lovely!",
        ],
        "Meh": [
            "Well, you got it!",
            "Mostly,",
        ],
        "Sucks Ass": [
            "You're eating my flesh with this one!"
        ]
    }
    OliverOneCustomer = Customer(oliverOneWants, noPreferences, oliver, oliverOneEnter, oliverOneExit, "Oliver", True)

    oliverTwoWants = {"Rose": 1, "Lily": 1, "Hyacinth": 1, "Forget-Me-Not": 1, "Bluebell": 1, "Hydrangea": 1, "Carnation": 1, "Leaf": 1}
    oliverTwoEnter = [
        "Hey there!",
        "Lovely shop you have here!",
        "My friend… I’d like to cheer him up. He’s been real down lately.",
        "He loves flowers too! I think a little bit of everything would be nice.",
        "Give me the whole rainbow!",
    ]
    oliverTwoExit = {
        "Happy": [
            "All according to plan!",
            "How lovely!",
        ],
        "Meh": [
            "Well, you got it!",
            "Mostly,",
        ],
        "Sucks Ass": [
            "You're eating my flesh with this one!"
        ]
    }
    OliverTwoCustomer = Customer(oliverTwoWants, noPreferences, oliver, oliverTwoEnter, oliverTwoExit, "Oliver", True)
    

    def initialize_customers(custList: list[Customer]):
        global UnmetCustomerList
        global minorCustomerMasterlist
        
        UnmetCustomerList = []
        for customer in custList:
            UnmetCustomerList.append(customer)
        while len(UnmetCustomerList) < quota:
            UnmetCustomerList.append(getMinorCustomer())
    
label customerCutscene:
    # Unlimited If Statement Works
    if customer == ArthurOneCustomer:
        show Arthur Happy 

        blank "(You wonder if you should even be giving bouquets like these to random people.)"
        peri "Can I ask..?"

        show Arthur Meh 

        arthur "It's none of your business. You wouldn't get it."
        blank "(Rude...)"
        peri "Should you really be giving that to-"
        arthur "I know what I want to do, thank you very much!"

        hide Arthur Meh
        with dissolve

        blank "(Before you can get any other words out, Arthur storms out of the shop.)"

    if customer == ArthurTwoCustomer:
        show Arthur Meh
        
        blank "(You recall your encounter with Reuben a few months ago.)"
        peri "So it IS you..."
        arthur "Yes. It is me."
        blank "(...)"

        show Arthur Sucks Ass

        arthur "I don't know what kind of lies and misinformation he told you while he was here, but I want you to know that they're all lies."
        blank "(You stay silent.)"
        arthur "...?"
        blank "(...)"

        show Arthur Meh

        arthur "Did he... say anything?"
        peri "No... not really..."
        blank "(Arthur is taken aback.)"
        peri "If anything, he really just wants to get along with you."

        show Arthur Sucks Ass

        arthur "I don't... I don't believe that!"
        peri "Listen. I'm not really one to intervene with these things, but..."
        peri "I think you should try talking to him? Hear him out, even just once?"
        arthur "I don't need your advice, okay? I can handle this on my own."

        hide Arthur Sucks Ass
        with dissolve

        blank "(You try to think of something to say, but Arthur storms out of the shop before you can come up with something.)"
        blank "(You hope that what you said got through to him. In some way.)"

    
    if customer == KaraOneCustomer:
        show Kara Meh 

        peri "So, what brings you here?"
        kara "Coming home from overseas work... you know how it is."
        peri "Mmm..."
        kara "These flowers are for a friend, actually."
        kara "Part of why I'm visiting is because she's sick..."
        kara "Caught a kinda serious illness... I want to look out for her whenever I can."
        peri "I see..."
        peri "That's really sweet of you!"

        show Kara Happy 

        kara "Hehe, I sure hope so..."
        peri "I hope she gets better soon."

        show Kara Meh 

        kara "Thanks... though, it might be a while."
        blank "(You nod. Kara waves at you as she leaves the store.)"
        
        hide Kara Meh
        with dissolve
        

    if customer == KaraTwoCustomer:
        show Kara Meh 

        peri "So, how are you?"
        kara "I'm doing well... it's my friend I'm a little worried for."
        peri "Oh no... did her condition get worse?"
        kara "A little... not too bad yet, thankfully."

        show Kara Happy 

        kara "I do hope she ends up liking these flowers, though..."
        blank "(The room gets a little quiet. To lighten the mood a bit, you ask...)"
        peri "You must care for her a lot, huh?"
        kara "Mmm."
        kara "She's one of the best friends I've ever had, I think."
        kara "We've been friends since childhood, and I'm glad to have had her constantly throughout my life..."
        kara "I like listening to her talk, hanging out with her, and..."
        blank "(She pauses for a bit.)"

        show Kara Sucks Ass 

        kara "Every day I'm away I really do miss her..."
        blank "(You really do hope Kara's friend gets better soon...)"
        blank "(Another part of you, though it probably shouldn't, wonders if...)"
        kara "Do you think I like her, or something like that?"
        blank "(Crap.)"
        peri "Kind of....? I don't mean to pry, of course..."
        kara "No, no, it's okay, I get what you mean..."
        kara "It's just..."
        kara "I don't think it's in me to love like that, you know?"
        kara "I feel like I have so much love in my heart, and I want to share that with everyone I meet... equally, I guess."
        kara "I've never really felt like I loved anyone in a way I found to be different from other people..."
        kara "And I'm content with that!"
        kara "...does that make sense...?"
        blank "(You nod.)"
        peri "Thats very admirable of you."

        show Kara Happy 

        kara "Thanks...!"
        peri "I hope your friend gets better soon. And that she likes the flowers, too."
        kara "I hope so too."

        show Kara Meh 

        kara "Well, I better get going! Thank you so much for hearing me out!"
        blank "(You watch Kara leave the shop.)" 

        hide Kara Meh 
        with dissolve
        
    if customer == KaraThreeCustomer:
        show Kara Meh 

        peri "You seem a lot happier today."
        kara "Well..."

        show Kara Happy 

        blank "(Kara's smile is seen from ear to ear.)"
        kara "My friend's being discharged from the hospital today!"
        peri "Woah! Congratulations!"
        peri "Are you two doing anything today?"
        kara "Well, I'm still seeing her at the hospital, but we're going to get dinner after she's discharged!"
        peri "I see, thats great!"
        peri "I'm so happy for you."
        kara "Thank you!"
        kara "Thank you so much for the help, and for listening to me all this time."
        peri "It's no problem at all. Be well!"
        kara "Thanks!"
        blank "(And just as quickly as she entered, Kara has left the shop.)"

        hide Kara Happy 
        with dissolve

    if customer == MarkOneCustomer:
        show Mark Meh 

        peri "I'm... I'm so sorry."
        mark "It's alright."
        mark "I've been doing this for a while, every time I fly back. I just thought I'd drop by, since it's closer to the airport and I won't have to go out of my way."
        peri "I see..."
        peri "Visiting family, then?"
        mark "Haha, yeah. I always do miss them."
        mark "Especially now, when I'm away and working overseas."
        mark "I can't help but feel bad sometimes, but someone has to make ends meet, right?"
        blank "(You nod. There's an awkward silence between you two.)"

        show Mark Sucks Ass 

        mark "Hahaha! Was that too much? My apologies."
        peri "No, no, not at all! I get what you mean."
        peri "Being so far from home all the time must be hard."

        show Mark Meh 

        mark "You get used to it. Anyways, I do have to get going now."
        mark "Good luck with the rest of your shift."
        peri "Thank you very much."
        blank "(Mark picks up the bouquet, and leaves the shop.)"

        hide Mark Meh
        with dissolve
        
    if customer == MarkTwoCustomer:
        show Mark Meh 

        peri "Why the orchids, all of a sudden?"
        mark "I looked into it on my own, and saw that orchids are meant to symbolize new beginnings."
        mark "And, a few months after I flew back, I was told of a job opening that would allow me to work here."
        mark "With a similar pay to my current job, no less."
        peri "Aw, that's nice to hear! You'll get to spend more time together with your family too, right?"
        mark "Indeed. I won't have to fly back every few months anymore, haha!"
        blank "(Mark sighs.)"

        show Mark Sucks Ass 

        mark "I wish my mother were here to see this. It feels like things are finally looking up for me. My family, too."
        peri "I'm happy for you."
        mark "Thank you."

        show Mark Meh 

        mark "Well! I have to get going now."
        mark "Good luck with the shop."

        hide Mark Meh
        with dissolve
        
    if customer == MarkThreeCustomer:
        show Mark Meh 

        blank "(Almost out of the corner of your eye, you see two children running towards the shop, one boy and one girl, and a figure that seems to be their mother chasing after them.)"
        mike "DAAAAAAD!"

        show Mark Happy 

        blank "(One of the kids reaches towards Mark, tightly embracing him.)"
        mark "Mike, Mikayla, what a surprise to see you two here!"
        blank "(He glances over at what seems to be the kids' mother, his wife.)"
        mark "I didn't know you would be visiting!"
        mich "Well, it's the least we could do!"
        mika "Mom told us about your new job! You get to stay here now?"
        mark "Yes I can! I missed spending more time with you all, you have no idea."
        blank "(You obviously can't help but smile.)"
        peri "Here. I think your dad meant to give you these."
        blank "(You hand the children the bouquet.)"
        mika "Oooh, pretty!"
        if joyRating["Bluebell"] > -1 or joyRating["Forget-Me-Not"] > -1:
            mike "So blue!"
        else:
            mike "Where's the blue?"
        blank "(Mark's wife laughs.)"
        mich "Guess we're not the only one with surprises today, huh? "
        mark "Indeed, hahaha!"
        blank "(Mark turns to you.)"

        show Mark Sucks Ass 
        mark "Thank you, again. For all the help, and joy you've brought us here."
        mika "Thank you, Miss... uh..."
        peri "Periwinkle! It's no problem at all."
        mark "Well, we'll get going now. I know we might not see each other that much now, but know that you were lovely to work with."
        mika "Thank you, Miss Periwinkle!"
        mike "Bye!!!"
        mich "Thank you."
        
        hide Mark Sucks Ass
        with dissolve

        blank "(You watch as the family leaves the shop, and you can't help but feel fulfilled.)"

    if customer == ReubenOneCustomer:
        show Reuben Meh 

        peri "You know him...?"
        reuben "Arthur?"
        reuben "A bit, yeah... We fly out a lot to go to international competitions. Representatives of the school, the country, all that."
        peri "Woah... that must be really nice."

        show Reuben Happy 

        reuben "It is... I just came back from another Math contest."
        blank "(Reuben grins for a bit, then sighs.)"

        show Reuben Meh 

        reuben "I just wish that guy would stop bothering me sometimes."
        reuben "He goes on and on about how he should be so much better than me..."
        reuben "And then I beat him once and he blows up on me! "
        reuben "I didn't even win this time, and he still finds ways to rub that in my face! God, I hate him!"
        reuben "It's like he wants to do this so he can show off on me! Can't we both just get along and have fun every time we compete?"
        peri "Have you tried talking to him? It really seems like you mean well..."
        reuben "I have! And every time, he always snaps back at me..."
        peri "Right..."
        blank "(You recall your last interaction with Arthur.)"
        peri "Well, I hope you get through to him sometime."
        reuben "Thanks... sorry for the bother, too."
        reuben "Well, I have to go now. The delegation's waiting for me, and all."
        reuben "Thank you so much."

        hide Reuben Meh
        with dissolve

    if customer == ReubenTwoCustomer:
        show Reuben Meh 

        peri "It happened again, I'm assuming?"
        reuben "Yeah... Geology competition this time."
        reuben "I'm really sorry for all the trouble, I'll try to keep us both out of here this time."
        blank "(Reuben is about to turn to leave, but you can't help but ask.)"
        peri "Why flowers?"
        reuben "Hmm?"
        peri "If you two really dislike each other that much... why go buying flowers?"
        peri "I mean, there are surely other ways to express your disdain for someone, aren't there?"
        blank "(Certainly less expensive ways, too.)"
        peri "If you wanted to shame or humiliate someone so badly, why do it with flowers?"

        show Reuben Happy 

        reuben "..."
        blank "(The room is silent. Reuben is deep in thought.)"
        peri "You don't actually want for that to happen to him, do you?"
        blank "(Reuben pauses, then inhales deeply.)"

        show Reuben Meh 

        reuben "No..."
        blank "(You nod.)"
        peri "Look, if you're open to making amends with him, I really think you should."
        reuben "But how...?"
        peri "I don't know... try to be honest with him? Make an earnest, genuine attempt, then if he snaps back at you despite that then that's that. You could try buying him a nicer set of flowers next time."
        blank "(You meant that last sentence as a joke. Reuben, however, takes this advice to heart, and nods.)"

        show Reuben Happy 

        reuben "I'll keep that in mind. Thank you so much."
        
        hide Reuben Happy
        with dissolve
        
    if customer == ReubenThreeCustomer:

        show Reuben Meh

        peri "Did... something happen?"
        reuben "Not much, just... I thought about what you said all those months ago..."
        reuben "I want to try giving him this. And. Be nice to him. You know?"
        blank "(You smile.)"
        peri "You should do that."
        peri "I think... Arthur has a few things he should sort out with you, too."

        show Reuben Sucks Ass at left
        with move
        show Arthur Sucks Ass at right

        blank "(As if on cue, Arthur storms into the store.)"
        arthur "...what are YOU doing here?"
        blank "(Reuben flinches a little, with the bouquet currently in his hands.)"
        arthur "What? Another bouquet, just to spite me? To rub the fact that you're so much better than me in my face?"

        show Reuben Happy at left

        reuben "That's not what I intend to do..."

        show Arthur Meh at right

        arthur "Huh?"

        reuben "Not this time, at least..."
        blank "(The room falls silent for a little bit.)"
        blank "(You wonder if you're intruding, but...)"
        
        show Reuben Meh at left

        reuben "Look."
        blank "(Reuben extends the bouquet to Arthur.)"
        reuben "These are for you."

        show Reuben Happy at left

        reuben "Not because I hate you, or want you to die, or think I'm better than you..."

        show Reuben Happy Blush at left

        reuben "But because I want you to know that I respect you quite a lot."

        show Arthur Sucks Ass at right

        blank "(Arthur looks... confused.)"
        reuben "The amount of passion, energy, and commitment you put into... everything."
        reuben "I know that I've been kind of... petty, recently. With all the hateful bouquets I've been giving you recently."
        reuben "And I do truly apologize for that! I know what it feels like to have lost in something. Especially something on as large of a scale as an international competition."
        reuben "But I hope you know that I don't see you as any less of an individual despite that."

        show Arthur Sucks Ass Blush at right

        arthur "..."
        reuben "I hope we get to a kind of... understanding between ourselves. I truly only want us to get along."
        blank "(Reuben extends the bouquet once more, with Arthur responding by holding it gently in his hands.)"
        reuben "And besides..."
        reuben "It's kind of weird that we're hating on each other with flowers, of all things, isn't it?"
        blank "(The bouquet is received by Arthur.)"

        show Arthur Meh at right
        show Reuben Meh at left

        arthur "If you're being serious then... I'm sorry too."
        arthur "This whole flower thing was kind of... rash, wasn't it?"
        blank "(You mutter to yourself.)"
        peri "Tell me about it..."

        show Arthur Happy at right
        arthur "And... thank you."
        blank "(He looks at you.)"
        arthur "Sorry... about all this. I think I was a bit mean to you, too."
        peri "I get it. It's okay."
        blank "(Reuben gestures towards Arthur.)"
        reuben "Do you want to talk for a bit?"

        show Arthur Happy Blush at right

        arthur "..."
        arthur "...yeah, sure."
        reuben "Then, we'll leave the shop now, Thank you so much for the help."

        hide Reuben Meh
        with dissolve

        blank "(Reuben exits the shop, with Arthur following suit soon after.)"

        hide Arthur Happy Blush
        with dissolve

        peri "Let's hope I never have to go through that again, huh...?"
    
    if customer == IlanaGiftCustomer:         
        peri "What was that about...?"
        blank "(Ilana isn't usually one to visit at mornings.)"
        blank "(Usually she just does this to tease you. But ordering flowers, furthermore bouquets...)"
        blank "(Is she...?)"

    # Minor Customers

    # Tomi cutscenes
    if customer == TomiOneCustomer:
        $ minorCustomerMasterlist.append(TomiTwoCustomer)
        show Tomura Meh 

        peri "Say..."
        peri "You must really care about this person, huh?"

        show Tomura Happy 

        tomi "Yes! I feel kind of bad that we don't get to talk that much, especially since I have to fly out so frequently."
        peri "Right... well I hope they take these well!"
        tomi "I hope so too!"
        tomi "Thank you very much!"

        hide Tomura Happy
        with dissolve
    
    if customer == TomiTwoCustomer:
        show Tomura Meh
        peri "So, you perform?"

        peri "What is it that you play?"

        tomura "Oh! Haha, you might not believe it.."

        show Tomura Happy
        tomura "I’m an opera singer! In training. I do normal vocal things too."

        peri "Really? Wow! That’s…"

        tomura "I know. I don’t look like it, no?"

        peri "Haha, I wasn’t gonna say that. Just that that’s really cool!"

        tomura "Anyhow, we’re doing a set downtown this evening. Come if you’re not busy!" 
        with dissolve

    # Tour Telle cutscenes
    if customer == TourOneCustomer:
        $ minorCustomerMasterlist.append(TourTwoCustomer)

        peri "..."
        peri "...am I dreaming??"
    
    if customer == TourTwoCustomer:
        peri "..."

        peri "...wait? Is that cat gonna be okay?"

    # Clove cutscenes
    if customer == CloveOneCustomer:
        $ minorCustomerMasterlist.append(CloveTwoCustomer)

        show Clove Meh 

        peri "Your boyfriend's competing in international competitions? Wow, that's incredible."
        clove "Isn't it? It's kinda hard to believe he's even mine sometimes!"
        clove "I hope even something like this could measure up to a fraction of his medals…"
        peri "Well, didn't you say that you make bouquets out of your own flowers sometimes?"
        clove "Mhm! I pick them from the garden in our home."
        peri "I think that maybe whatever you'd make for him means more than any award, then. He can get a medal from anywhere, but only one you exists, right?"
        
        show Clove Happy 

        clove "Haha, that's true. Thanks for that, I think I needed it."
        clove "Take care!"

        hide Clove Happy
        with dissolve
    
    if customer == CloveTwoCustomer:

        show Clove Meh

        peri "Your friend got a new job, huh? What was her job before?"
        
        show Clove Sucks Ass

        clove "Eheh… I don’t think I can say…"

        peri "(...What is that supposed to mean?)"

        show Clove Happy

        clove "But!! Um!! Her new job’s really quaint! She’s working as a Laboratory Aide in a college, and she’s using their facilities to study ecosystem simulations! It’s a nice change of pace for her, haha."
        peri "I hope she has an easier time with her new job, then."
        clove "Heh, with her, I think that’s the opposite of what she wants."
        clove "...Ah!! I forgot the time! I gotta go now!"
        clove "Thank you so much again! It was really nice talking to you!"

        hide Clove Happy
        with dissolve
    
    # Avery cutscenes
    if customer == AveryOneCustomer:
        $ minorCustomerMasterlist.append(AveryTwoCustomer)

        show Avery Meh

        peri "So, you grow flowers too?"

        show Avery Happy

        avery "Yeah! Have a whole greenhouse of plants, actually, haha..."
        peri "That's nice..."
        peri "..."
        peri "...you're not trying to put me out of business, are you?"

        show Avery Sucks Ass

        avery "WHAAAT! Of course not!!!"
        avery "I just like seeing other people like me out in the open, you know?"

        show Avery Happy
        avery "Flowers are great! Wouldn't you agree?"
        peri "Yeah."
        blank "(You sigh in relief. Your shop lives to see another day.)"

        hide Avery Happy
        with dissolve

    if customer == AveryTwoCustomer:
        
        show Avery Meh

        peri "You sure seem to know a lot about flowers, don't you?"

        show Avery Happy

        avery "You could say that!"
        avery "I like learning the little details about each of them."
        blank "(For obvious reasons, you relate to this quite a bit.)"
        avery "So..."

        show Avery Sucks Ass

        avery "Are these the only flowers in your shop?"
        peri "Ack!"
        peri "Yes...? Is there anything wrong with that?"

        show Avery Meh

        avery "Ah, well...! These do seem to be very popular ones, so I can't blame you for having these in stock, but..."

        show Avery Happy

        avery "I think it wouldn't hurt to have some variety! Maybe some chrysanthemums, tulips, you know?"
        avery "There are tons more things you can convey with flowers that aren't just the ones you have here!"
        blank "(You're not really sure you need Avery to tell you that, but...)"
        avery "I have a few I'm growing right now that I could drop off here sometime, if you'd like!"
        peri "That's a bit much... but, thanks anyways." 
        blank "(You can't really tell if the advice is too overbearing...)"
        blank "(...but seeing someone as enthusiastic about flowers as you are is nice, right?)"

        hide Avery Happy
        with dissolve

    if customer == FloweriOneCustomer:
        $ minorCustomerMasterlist.append(FloweriTwoCustomer)

        show Floweri Meh
        blank "(This guy is kinda weird.)"
        peri "Did you say... your king?"

        show Floweri Happy

        floweri "Heh, yes!"
        peri "Are you like, some sort of medieval LARPer... or...?"

        show Floweri Sucks Ass

        floweri "Get a chance! Of course not!"

        show Floweri Happy

        floweri "I’ll take these now."
        floweri "Here I come San Francisco!"

        hide Floweri Happy
        with dissolve 
        
        blank "(We're not in the United States...)"
    
    if customer == FloweriTwoCustomer:
        # PLACEHOLDER --- CHANGE LATER
        show Floweri Meh
        blank "Hahahahaflowershahahahaha"
    
    # Oliver cutscenes
    if customer == OliverOneCustomer:
        # PLACEHOLDER --- CHANGE LATER
        $ minorCustomerMasterlist.append(OliverTwoCustomer)

        show Oliver Meh
        oliver "dogggggggggg"

    if customer == OliverTwoCustomer:

        show Oliver Meh
        oliver "woof woof!!!!!"

    play sound "come again sometime.mp3"
    pause 1.0

    jump customerWave