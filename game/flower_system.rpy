init python:
    def is_similar(bouquet: dict, compare: dict) -> dict:
        joy = {}
        for key, val in compare.items():
            joy[key] = 0
            if key in bouquet:
                joy[key] = (bouquet[key] - (compare[key]+1))/ (compare[key]+1)
                print(key + " joy is set to" + str((bouquet[key] - (compare[key]+1))/ (compare[key]+1)))
            else:
                joy[key] = -1
        return joy

    def add_flower(flower: dict, bouquet: dict) -> dict:
        for key, val in flower.items():
            if key in bouquet:
                bouquet[key] = flower[key] + bouquet[key]
            else:
                bouquet[key] = flower[key]
        return bouquet

    def unique_combo(bouquet: dict, baseJoy: dict) -> dict:
        gunsAndRoses = {"Roses": 1, "Guns": 1}
        if is_similar(bouquet, gunsAndRoses)["satisfaction"] >= 0:
            baseJoy["satisfaction"] += 10
            baseJoy["gunsAndRoses"] = True
        return baseJoy

    def calculate_preferences(bouquet: dict, preferences: dict, joy: dict):
        for key, val in preferences.items():
            if key in bouquet and bouquet[key] > 1:
                joy["satisfaction"] += preferences[key]
        return joy

    def calculate_satisfaction(joy: dict):
        total = 0
        for key, val in joy.items():
            total += abs(val)
        joy["satisfaction"] = total/len(joy)
        return joy


    class Customer:
        def __init__(self, wants: dict[str, int], preferences: dict[str, int]):
            self.preferences = preferences
            self.wants = wants
        
        def calculateJoy(self, bouquet):
            joy = is_similar(bouquet, self.wants)
            if "NoOverflow" in self.preferences:
                for key, val in joy.items():
                    if val > 0:
                        joy[key] = 0
            joy = calculate_satisfaction(joy)
            joy = calculate_preferences(bouquet, self.preferences, joy)
            return joy