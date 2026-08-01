init python:
    def is_similar(bouquet: dict, compare: dict) -> dict:
        joy = {}
        for key, val in compare.items():
            joy[key] = 0
            if key in bouquet:
                joy[key] = (bouquet[key] + 1 - (compare[key]+1))/ (compare[key]+1)
            else:
                joy[key] = -1
        return joy

    def add_flower(name: str, bouquet: list, meanings: dict):
        if len(bouquet) >= 7:
            return
        bouquet.append(name)
        print(name)
        for key, val in get_flower_meanings(name).items():
            if key in meanings:
                meanings[key] += val
            else:
                meanings[key] = val
        print(meanings)
        return

    def remove_flower(name: str, bouquet: list, meanings: dict):
        if name in bouquet:
            bouquet.remove(name)
            for key, val in get_flower_meanings(name).items():
                if key in meanings:
                    meanings[key] -= val
        return
    
    def set_addon(name: str, addon: str, meanings: dict):
        for key, val in get_flower_meanings(addon).items():
            if key in meanings:
                meanings[key] -= val
        for key, val in get_flower_meanings(name).items():
            if key in meanings:
                meanings[key] += val
        return

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

    def get_flower_meanings(name: str) -> dict:
        meanings = {}
        if name == "Rose":
            meanings = {"Love": 3, "Red":1, "Rose": 1, "Classic": 1}
        if name == "Carnation":
            meanings = {"Admiration": 3, "Pink":1, "Carnation": 1, "Mother": 1}
        if name == "Hydrangea":
            meanings = {"Pride": 3, "Purple":1, "Hydrangea": 1, "Royalty": 1}
        if name == "Lily":
            meanings = {"Hate": 3, "Orange":1, "Lily": 1, "Passion": 1}
        if name == "Bluebell":
            meanings = {"Humility": 3, "Blue": 1, "Bluebell": 1, "Gratitude": 1}
        if name == "Hyacinth":
            meanings = {"Jealousy": 3, "Yellow":1, "Hyacinth": 1, "Contempt": 1}
        if name == "Orchid":
            meanings = {"Purity": 3, "White":1, "Orchid": 1, "Funeral": 1}
        if name == "Forget-Me-Not":
            meanings = {"Faithful": 3, "Light Blue":1, "Forget-Me-Not": 1, "Remembrance": 1}
        if name == "Stick":
            meanings = {"Negative": 3, "Brown":1, "Stick": 1, "Dog": 1}
        if name == "Leaf":
            meanings = {"Positive": 3, "Green":1, "Leaf": 1, "Yum": 1}
        return meanings

    def flower_pic(name: str, imgType: str) -> str:
        if name == "Rose":
            image = "red " + imgType + " %s.png"
        if name == "Carnation":
            image = "pink " + imgType + " %s.png"
        if name == "Hydrangea":
            image = "purple " + imgType + " %s.png"
        if name == "Lily":
            image = "orange " + imgType + " %s.png"
        if name == "Bluebell":
            image = "blue " + imgType + " %s.png"
        if name == "Hyacinth":
            image = "yellow " + imgType + " %s.png"
        if name == "Orchid":
            image = "white " + imgType + " %s.png"
        if name == "Forget-Me-Not":
            image = "aqua " + imgType + " %s.png"
        if name == "Stick":
            image = "branch " + imgType + " %s.png"
        if name == "Leaf":
            image = "leaf " + imgType + " %s.png"
        return image

    def init_globals():
        global meanings
        global bouquet
        global decor
        global FlowerList
        global AddonList
        global page
        meanings = {}
        bouquet = []
        decor = ""
        FlowerList = ["Rose", "Lily", "Hyacinth", "Forget-Me-Not", "Bluebell", "Hydrangea", "Carnation", "Orchid"]
        AddonList = ["Stick", "Leaf"]
        page = 1
