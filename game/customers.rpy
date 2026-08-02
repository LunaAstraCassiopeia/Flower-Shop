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

image Kara Meh = "Kara/Kara Meh.png"
image Kara Happy = "Kara/Kara Happy.png"
image Kara Sucks Ass = "Kara/Kara Sucks Ass.png"

# all instances of customers are defined here.
init python:

    # all ilana instances!

    ilana = Character("Ilana")
    
    ilanaTutorialWants = {"Orchid": 7}
    noPreferences = {"test": 0}
    ilanaTutorialEnter = ["Those flowers... I forget what they're called...", "The, uh, white ones?", "About innocence, and new beginnings, and stuff...", "Give me an entire bouquet of those. Seven of 'em.", "...", "Don't just stare at me like that! Use your manual to figure out what I mean!", "BL:(Pick out flowers by selecting them on the left, then click submit to give the customer their bouquet! You can click on flowers to remove them from the bouquet.)"]
    ilanaTutorialExit = {
        "Happy": ["There you go.", "Exactly what I asked.", "Told you you should've kept that book safe!", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
        "Meh": ["I mean... you're kind of there?", "I told you I wanted more of those white ones, right?", "Ah, well. At least you got halfway there.", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
        "Sucks Ass": ["...This isn't what I asked for?", "...Like, at all?", "You're doing this on purpose, aren't you?", "Anyways, you should have everything you need now. I'll be on my way, I'm kinda busy today.", "See you later!"],
    }
    IlanaTutorialCustomer = Customer(ilanaTutorialWants, noPreferences, ilana, ilanaTutorialEnter, ilanaTutorialExit, "Ilana", False)

    # all arthur instances!

    arthur = Character("Arthur")
    
    arthurOneWants = {"Lily": 4, "Orchid": 2, "Hydrangea": 1}
    noPreferences = {"test": 0}
    arthurOneEnter = ["Hey. This is that one shop... right? With, the flowers?", "BL:(You're not sure what other flower shops are there. Nearby, at least.)", "Bit of a strange ask, but... give me the worst bouquet you can think of.", "BL:(...?)", "I'm thinking of... hatred, spite, wishing this person was dead. Maybe something to remind them that I'm better than them."]
    arthurOneExit = {
        "Happy": ["Perfect.", "This guy's not dumb, he'll know what I mean with these."],
        "Meh": ["This will have to do.", "I don't think it'll fully get the point across, but it will have to suffice."],
        "Sucks Ass": ["...", "Is this not the exact opposite of what I said I wanted?"],
    }
    ArthurOneCustomer = Customer(arthurOneWants, noPreferences, arthur, arthurOneEnter, arthurOneExit, "Arthur", True)
    
    # all kara instances!

    kara = Character("Kara")
    
    karaOneWants = {"Carnation": 4, "Bluebell": 3}
    noPreferences = {"test": 0}
    karaOneEnter = ["Hello!", "I'm not sure what flowers I think she'd like, but...", "...I have a friend who really likes pink flowers!", "I would like some of those, along with ones that generally convey gratitude."]
    karaOneExit = {
        "Happy": ["Oh! I think she'd like these ones, yeah!", "These will cheer her up, definitely!"],
        "Meh": ["Ah!", "I think this could work!", "Could use a little more, but I think she'd like this nonetheless."],
        "Sucks Ass": ["Hmm...", "It's an honest effort, at least!", "I'm not sure if she'd like these, but it's worth a shot!"],
    }
    KaraOneCustomer = Customer(karaOneWants, noPreferences, kara, karaOneEnter, karaOneExit, "Kara", True)

    # minor characters

    roseWants = {"Rose": 5}
    Rose = Character("Rose")
    roseEnter = ["Hi!", "I'm Rose!", "Could I have 5 roses?"]
    roseExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :)"],
        "Meh": ["It's okay!", "I guess..."],
        "Sucks Ass": ["Wow...", "I didn't know this could suck so much ass..."],
    }
    RoseCustomer = Customer(roseWants, noPreferences, Rose, roseEnter, roseExit, "Rose", False)

    carnieWants = {"Carnation": 5}
    Carnation = Character("Carnation")
    carnieEnter = ["Hi... I'm Carnation...", "5 carnations please..."]
    carnieExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    CarnationCustomer= Customer(carnieWants, noPreferences, Carnation, carnieEnter, carnieExit, "Carnation", False)
    
    hydraWants = {"Hydrangea": 5}
    Hydrangea = Character("Hydrangea")
    hydraEnter = ["Hi!", "Hydrangea!", "5 hydrangeas, please and thank you!"]
    hydraExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    HydrangeaCustomer = Customer(hydraWants, noPreferences, Hydrangea, hydraEnter, hydraExit, "Hydrangea", False)

    tomiWants = {"Forget-Me-Not": 4, "Bluebell": 3}
    tomi = Character("Tomura")
    tomiEnter = ["Hi..!", 
    "I'm planning on visiting a good friend of mine today, one I haven't talked to in a while...", 
    "They like a lot of blue flowers!",
    "They're very good with flower language, and I want a bouquet that conveys how constant they've been in my life, even despite not meeting for a bit...",
    "I hope they never forget me!",
    "Could you help me out?"]
    tomiExit = {
        "Happy": ["Oh..!", "I recall them saying they really liked these flowers!", "Thank you so much!"],
        "Meh": ["Ah..?", "You really think they'd like these..?", "Well, thank you regardless."],
        "Sucks Ass": ["Huh...", "Are these really the right flowers for this?"],
    }
    TomiCustomer = Customer(tomiWants, noPreferences, tomi, tomiEnter, tomiExit, "Tomura", True)


    def initialize_customers(custList: list[Customer]):
        global UnmetCustomerList
        global minorCustomerMasterlist
        minorCustomerMasterlist = [CarnationCustomer, HydrangeaCustomer, RoseCustomer, TomiCustomer]
        
        UnmetCustomerList = []
        for customer in custList:
            UnmetCustomerList.append(customer)
        while len(UnmetCustomerList) < quota:
            UnmetCustomerList.append(getMinorCustomer())

    # hydraWants = {"Hydrangea": 5}
    # Hydrangea = Character("Hydrangea")
    # HydrangeaCustomer = Customer(hydraWants, noPreferences, Hydrangea)

    # lilyWants = {"Lily": 5}
    # Lily = Character("Lily")
    # LilyCustomer = Customer(lilyWants, noPreferences, Lily)
    
label customerCutscene:
    # Unlimited If Statement Works
    if customer == HydrangeaCustomer:
        deb "Here's more extra dialogue!"

        deb "Yay!"

    if customer == TomiCustomer:
        show Tomura Meh at right

        peri "Say..."
        peri "You must really care about this person, huh?"

        show Tomura Happy at right

        tomi "Yes! I feel kind of bad that we don't get to talk that much, especially since I have to fly out so frequently."
        peri "Right... well I hope they take these well!"
        tomi "I hope so too!"
        tomi "Thank you very much!"

        hide Tomura Happy
        with dissolve
    
    if customer == ArthurOneCustomer:
        show Arthur Happy at right

        blank "(You wonder if you should even be giving bouquets like these to random people.)"
        peri "Can I ask..?"

        show Arthur Meh at right

        arthur "It's none of your business. You wouldn't get it."
        blank "(Rude...)"
        peri "Should you really be giving that to-"
        arthur "I know what I want to do, thank you very much!"

        hide Arthur Meh
        with dissolve

        blank "(Before you can get any other words out, Arthur storms out of the shop.)"

    
    if customer == KaraOneCustomer:
        show Kara Meh at right

        peri "So, what brings you here?"
        kara "Coming home from overseas work... you know how it is."
        peri "Mmm..."
        kara "These flowers are for a friend, actually."
        kara "Part of why I'm visiting is because she's sick..."
        kara "Caught a kinda serious illness... I want to look out for her whenever I can."
        peri "I see..."
        peri "That's really sweet of you!"

        show Kara Happy at right

        kara "Hehe, I sure hope so..."
        peri "I hope she gets better soon."

        show Kara Meh at right

        kara "Thanks... though, it might be a while."
        blank "(You nod. Kara waves at you as she leaves the store.)"
        
        hide Kara Meh
        with dissolve


    jump customerWave