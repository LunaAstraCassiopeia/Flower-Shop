init python:
    roseWants = {"Rose": 5}
    noPreferences = {"test": 0}
    Rose = Character("Rose")
    RoseCustomer = Customer(roseWants, noPreferences, Rose)
    def roseRun():
        renpy.show("Rose", at_list=[right])
        renpy.with_statement(dissolve)
        self.character(_("Hi, I;m Rose! I know exactly what I want!"))
        self.character(_("Give me five flowers that bear my name!!"), interact = False)
        renpy.choice_for_skipping()
        rating = renpy.call_screen("flower_menu", self)
        return rating

    def roseFlowers():
        renpy.hide("Rose")
        if joyRating["satisfaction"] < 0.3:
            renpy.show("Happy", at_list=[right])
            self.character(_("Awessome!!!"))
            renpy.hide("Happy")
        elif joyRating["satisfaction"] < 1:
            renpy.show("Meh", at_list=[right])
            self.character(_("It's okay..."))
            renpy.hide("Meh")
        elif joyRating["satisfaction"] < 10:
            renpy.show("Sucks Ass", at_list=[right])
            self.character(_("Hey has anyone noticed this sucks ass?"))
            renpy.hide("Sucks Ass")
        renpy.show("Rose", at_list=[right])
        self.character(_("My satisfaction score is [joyRating['satisfaction']]"))
        renpy.hide("Rose")
        renpy.with_statement(dissolve)
        renpy.hide_screen("flower_menu")
        renpy.with_statement(dissolve)
        return
    
    RoseCustomer.replaceMethods(roseRun, roseFlowers)


    carnieWants = {"Carnation": 5}
    Carnation = Character("Carnation")
    CarnationCustomer= Customer(carnieWants, noPreferences, Carnation)

    hydraWants = {"Hydrangea": 5}
    Hydrangea = Character("Hydrangea")
    HydrangeaCustomer = Customer(hydraWants, noPreferences, Hydrangea)

    lilyWants = {"Lily": 5}
    Lily = Character("Lily")
    LilyCustomer = Customer(lilyWants, noPreferences, Lily)