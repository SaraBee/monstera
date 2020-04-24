import random
pages = [
    "Um, @SaraBee? ",
    "Hey! @SaraBee! ",
    "Paging @SaraBee: "
]

moisture_openers = [
    "My soil moisure reading is {} and ",
    "My sensor currently reads {} and ",
    "Moisture levels are at {} and "
]

happy_thoughts = [
    "I'm feeling fine 😎🌿",
    "I'm p comfy 😌",
    "I'm a happy camper 🛶🏕",
    "that's the way I like it 💦",
]

thirsty_thoughts = [
    "I could use a beverage 🍹",
    "I'm feeling a little parched 🥵",
    "it's time for a drink 🚰🙏🏻",
    "I'm hecking thirsty!!"
]

dry_openers = [
    "I could use a misting! ",
    "Would you mind turning on the humidifier? ",
    "Could you get the spray bottle please? ",
    "Turn the humidifier on, please! "
]

dry_thoughts = [
    "My humidity is only {}% 🥵",
    "{}% humidity is less than ideal 😒",
    "I'm a tropical plant and like my humidity higher than {}% 😩",
]

class Thoughts:

    def get_happy_thought(reading):
        opener = random.choice(moisture_openers).format(str(reading))
        return opener + random.choice(happy_thoughts)

    def get_thirsty_thought(reading):
        page = random.choice(pages)
        opener = random.choice(moisture_openers).format(str(reading))
        return page + opener + random.choice(thirsty_thoughts)

    def get_unearthed_thought(reading):
        opener = random.choice(moisture_openers).format(str(reading))
        return opener + "@SaraBee must have pulled out my sensor 🤷🏻‍♀️"

    def get_dry_thought(reading):
        page = random.choice(pages)
        opener = random.choice(dry_openers)
        return page + opener + random.choice(dry_thoughts).format(str(reading))
