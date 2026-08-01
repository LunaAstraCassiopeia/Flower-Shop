# define character sprites here
image Tomura Happy = "Tomura Happy.png"
image Tomura Meh = "Tomura Meh.png"
image Tomura Sucks Ass = "Tomura Sucks Ass.png"

# all instances of customers are defined here.
init python:

    roseWants = {"Rose": 5}
    noPreferences = {"test": 0}
    Rose = Character("Rose")
    roseEnter = ["Hi!", "I'm Rose!", "Could I have 5 roses?"]
    roseExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :)"],
        "Meh": ["It's okay!", "I guess..."],
        "Sucks Ass": ["Wow...", "I didn't know this could suck so much ass..."],
    }
    RoseCustomer = Customer(roseWants, noPreferences, Rose, roseEnter, roseExit, "Rose")

    carnieWants = {"Carnation": 5}
    Carnation = Character("Carnation")
    carnieEnter = ["Hi... I'm Carnation...", "5 carnations please..."]
    carnieExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    CarnationCustomer= Customer(carnieWants, noPreferences, Carnation, carnieEnter, carnieExit, "Carnation")
    
    hydraWants = {"Hydrangea": 5}
    Hydrangea = Character("Hydrangea")
    hydraEnter = ["Hi!", "Hydrangea!", "5 hydrangeas, please and thank you!"]
    hydraExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    HydrangeaCustomer = Customer(hydraWants, noPreferences, Hydrangea, hydraEnter, hydraExit, "Hydrangea")

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
    TomiCustomer = Customer(tomiWants, noPreferences, tomi, tomiEnter, tomiExit, "Tomura")


    def initialize_customers(custList: list[Customer]):
        global CustomerList
        global UnmetCustomerList
        
        CustomerList = []
        UnmetCustomerList = []
        for customer in custList:
            CustomerList.append(customer)
            UnmetCustomerList.append(customer)

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
        show Tomura Meh

        peri "Say..."

        peri "You must really care about this person, huh?"

        hide Tomura Meh
        show Tomura Happy
        tomi "Yes! I feel kind of bad that we don't get to talk that much, especially since I have to fly out so frequently."

        peri "Right... well I hope they take these well!"

        tomi "I hope so too!"

        tomi "Thank you very much!"
        hide Tomura Happy
    jump customerWave