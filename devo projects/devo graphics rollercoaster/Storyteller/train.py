import asyncio
import edge_tts
import os
from playsound import playsound
from time import sleep as delay

# Asynchronous function to handle text-to-speech with a custom voice parameter
async def hinspeak(text, voice="hi-IN-SwaraNeural"):
    audio_file = "af.mp3"
    
    # Initialize edge-tts communicate object
    communicate = edge_tts.Communicate(text, voice)
    
    # Save the generated audio file asynchronously
    await communicate.save(audio_file)
    
    # Play and clean up the file
    playsound(audio_file)
    os.remove(audio_file)

# Helper function to call the async speech function sequentially
def speak(text, voice="hi-IN-SwaraNeural"):
    asyncio.run(hinspeak(text, voice))

def say_train_no(num, voice_gender):
    for i in num:
        speak(i, voice=voice_gender)

# Define your train announcement variables
gadino = "1। 9। 4। 7। 2।"
train = "एक जगह - दूसरी जगह एक्स्प्रेस"
platform = "2"
frrom = "एक जगह "
to = "दूसरी जगह"

# CHOOSE YOUR VOICE HERE:
# For Female voice: "hi-IN-SwaraNeural"
# For Male voice: "hi-IN-MadhurNeural"
selected_voice = "hi-IN-Madhur Neural" 
speak(f"{frrom} -  से -   {to} -  को जाने वाली -   {train} -   गाड़ी नंबर -  {gadino} -  प्लेटफॉर्म क्रमांक -   {platform} -  पे -  आ रही है।-")
# Announcement sequence execution

