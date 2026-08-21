import pyttsx3
from time import sleep

sentences = [
    "The Lion and the Mouse",
    "Once upon a time, there was a lion living in a forest.",
    "One day, a little mouse accidentally woke the lion."
]

for sentence in sentences:

    print(sentence)

    teller = pyttsx3.init()

    teller.setProperty("volume", 1.0)

    teller.say(sentence)

    teller.runAndWait()

    teller.stop()

    sleep(1)