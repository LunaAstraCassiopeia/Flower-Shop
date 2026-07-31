init python:
    def is_similar(bouquet: dict, compare: dict) -> dict:
        joy = {"satisfaction": 0}
        for key, val in compare.items():
            joy[key] = 0
            if key in bouquet:
                joy[key] = bouquet[key] - compare[key]
                joy["satisfaction"] += bouquet[key] - compare[key]
            else:
                joy[key] -= compare[key]
                joy["satisfaction"] -= compare[key]
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