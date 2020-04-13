import random

thought_openers = [
    "My soil moisure reading is {} and ",
    "My sensor currently reads {} and ",
    "Moisture levels are at {} and "
]

happy_thoughts = [
    "I'm feeling fine 😎🌿",
    "I'm p comfy 😌",
    "I'm a happy camper 🛶🏕",
    "that's the way I like it 💦",
    "@SaraBee is doing a great job 💯"
]

thirsty_thoughts = [
    "I could use a beverage 🍹",
    "I'm feeling a little parched 🥵",
    "it's time for a drink 🚰🙏🏻",
    "I'm hecking thirsty!!"
]

class Thoughts:

    def get_happy_thought(reading):
        opener = random.choice(thought_openers).format(str(reading))
        return opener + random.choice(happy_thoughts)

    def get_thirsty_thought(reading):
        opener = random.choice(thought_openers).format(str(reading))
        return opener + random.choice(thirsty_thoughts)

    def get_unearthed_thought(reading):
        opener = random.choice(thought_openers).format(str(reading))
        return opener + "@SaraBee must have pulled out my sensor 🤷🏻‍♀️"
