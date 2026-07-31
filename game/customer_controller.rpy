init python:
    import random

    CustomerList = []
    UnmetCustomerList = []

    class Customer:
        def __init__(self, wants: dict[str, int], preferences: dict[str, int], character):
            self.preferences = preferences
            self.wants = wants
            self.character = character
            UnmetCustomerList.append(self)
            CustomerList.append(self)
        
        def calculateJoy(self, bouquet):
            joy = is_similar(bouquet, self.wants)
            if "NoOverflow" in self.preferences:
                for key, val in joy.items():
                    if val > 0:
                        joy[key] = 0
            joy = calculate_satisfaction(joy)
            joy = calculate_preferences(bouquet, self.preferences, joy)
            return joy

        def runOnEnter(self):
            renpy.show("Default Person", at_list=[right])
            renpy.with_statement(dissolve)
            self.character(_("Hi there! This is default text and needs to be replaced!"))
            self.character(_("I don't know what I want, can you pick for me?"), interact = False)
            renpy.choice_for_skipping()
            rating = renpy.call_screen("flower_menu", self)
            return rating
            
        def runAfterFlowers(self, joyRating):
            renpy.hide("Default Person")
            if joyRating["satisfaction"] < 0.3:
                renpy.show("Happy", at_list=[right])
                self.character(_("I LOVE THIS AAA THANK YOU!!!!"))
                renpy.hide("Happy")
            elif joyRating["satisfaction"] < 1:
                renpy.show("Meh", at_list=[right])
                self.character(_("eh."))
                renpy.hide("Meh")
            elif joyRating["satisfaction"] < 10:
                renpy.show("Sucks Ass", at_list=[right])
                self.character(_("Hey has anyone noticed this sucks ass?"))
                renpy.hide("Sucks Ass")
            renpy.show("Default Person", at_list=[right])
            self.character(_("My satisfaction score is [joyRating['satisfaction']]"))
            renpy.hide("Default Person")
            renpy.with_statement(dissolve)
            renpy.hide_screen("flower_menu")
            renpy.with_statement(dissolve)
            return
        
        def replaceMethods(self, runMethod, AfterMethod):
            self.runOnEnter = runMethod
            self.runAfterFlowers = AfterMethod

    def getNewCustomer():
        bouquet = []
        meanings = {}
        decor = ""
        customer = random.choice(UnmetCustomerList)
        UnmetCustomerList.remove(customer)
        return customer