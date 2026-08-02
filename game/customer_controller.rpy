init python:
    import random

    UnmetCustomerList = []

    class Customer:
        def __init__(self, wants: dict[str, int], preferences: dict[str, int], character, enter_dialogue: list[str], exit_dialogue: dict[str, list[str]], name: str, hasCutscene: bool):
            self.preferences = preferences
            self.wants = wants
            self.character = character
            self.enter_dialogue = enter_dialogue
            self.exit_dialogue = exit_dialogue
            self.header = name
            self.hasCutscene = hasCutscene
        
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
            renpy.show(self.formatImage("Meh"), at_list=[right])
            renpy.with_statement(dissolve)
            idx = 0
            for line in self.enter_dialogue:
                inter = idx + 1 != len(self.enter_dialogue)
                if line[:3] == "BL:":
                    blank(_(line[3:]), interact = inter)
                else:
                    self.character(_(line), interact = inter)
                idx += 1
            renpy.choice_for_skipping()
            renpy.scene()
            renpy.show("flowers bg")
            renpy.show_screen("book_button")
            rating = renpy.call_screen("flower_menu", self)
            renpy.show("default bg")
            return rating
            
        def runAfterFlowers(self, joyRating):
            renpy.hide_screen("book_button")
            renpy.hide("Default Person")
            char_status = ""
            if joyRating["satisfaction"] < 0.3:
                char_status += "Happy"
            elif joyRating["satisfaction"] < 1:
                char_status += "Meh"
            elif joyRating["satisfaction"] < 10:
                char_status += "Sucks Ass"
            renpy.show(self.formatImage(char_status), at_list = [right])
            for line in self.exit_dialogue[char_status]:
                if line[:3] == "BL:":
                    blank(_(line[3:]))
                else:
                    self.character(_(line))
            renpy.hide(self.formatImage(char_status))
            renpy.show(self.formatImage("Meh"), at_list=[right])
            self.character(_("My satisfaction score is [joyRating['satisfaction']]"))
            if not self.hasCutscene:
                renpy.hide(self.formatImage("Meh"))
                renpy.with_statement(dissolve)
            renpy.hide_screen("flower_menu")
            renpy.with_statement(dissolve)
            return
        
        def formatImage(self, mood: str):
            ret = f"{self.header} {mood}"
            return ret

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

    def getMinorCustomer():
        bouquet = []
        meanings = {}
        decor = ""
        customer = random.choice(minorCustomerMasterlist)
        minorCustomerMasterlist.remove(customer)
        return customer