from random import choice
import pyttsx3 as t2s
from time import sleep as delay
from os import system, path

stories = [
    {
        "story_name": "The Lion and the Mouse",
        "story": "lion_and_mouse.txt"
    },
    {
        "story_name": "The Thirsty Crow",
        "story": "thirsty_crow.txt"
    },
    {
        "story_name": "The Golden Goose",
        "story": "golden_goose.txt"
    },
    {
        "story_name": "The Tortoise and the Hare",
        "story": "tortoise_&_hare.txt"
    },
    {
        "story_name": "The Honest Woodcutter",
        "story": "honest_woodcutter.txt"
    },
    {
        "story_name": "The Lost Princess and the Enchanted Forest",
        "story": "lp&ef.txt"
    }
]

system("cls")

teller = t2s.init()

teller.setProperty("volume", 1.0)

story = choice(stories)


def print_and_say(text):

    text = text.strip()

    if text != "":
        print(text)
        t2s.speak(text)
        


# Speak the title
print_and_say(story["story_name"])

folder = r"C:\Users\bhuvnesh\Desktop\practice\Storyteller"

file_path = path.join(folder, story["story"])

with open(file_path, "r", encoding="utf-8") as tale:

    for line in tale:
        print(line.strip())
        t2s.speak(line.strip())
