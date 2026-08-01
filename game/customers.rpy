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
    RoseCustomer = Customer(roseWants, noPreferences, Rose, roseEnter, roseExit)

    carnieWants = {"Carnation": 5}
    Carnation = Character("Carnation")
    carnieEnter = ["Hi... I'm Carnation...", "5 carnations please..."]
    carnieExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    CarnationCustomer= Customer(carnieWants, noPreferences, Carnation, carnieEnter, carnieExit)
    
    hydraWants = {"Hydrangea": 5}
    Hydrangea = Character("Hydrangea")
    hydraEnter = ["Hi!", "Hydrangea!", "5 hydrangeas, please and thank you!"]
    hydraExit = {
        "Happy": ["Yay!!!", "Exactly what I wanted!", "Thank you!! :]"],
        "Meh": ["It's okay!", "I guess...", "This is fine..."],
        "Sucks Ass": ["Wow...", "This sucks..."],
    }
    HydrangeaCustomer = Customer(hydraWants, noPreferences, Hydrangea, hydraEnter, hydraExit)

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
    if customer == HydrangeaCustomer:
        deb "Here's more extra dialogue!"

        deb "Yay!"
    jump customerWave