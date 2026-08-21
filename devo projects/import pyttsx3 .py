import pyttsx3

engine = pyttsx3.init()

# Find and switch to a Hindi voice if available on your system
voices = engine.getProperty('voices')
hindi_voice_found = False

for voice in voices:
    print(voice.name .lower())
    print(voice.id.lower())
    #Check for 'Hindi' or 'HI' in the system voice descriptions
    if "hindi" in voice.name.lower() or "hi" in voice.id.lower():
        engine.setProperty('voice', voice.id)
        hindi_voice_found = True
        break

if not hindi_voice_found:
    print("Warning: Native Hindi voice pack not detected. Falling back to default system voice.")

# Set speed rate (Optional)
engine.setProperty('rate', 150) 

# Speak the text
text = "नमस्ते दुनिया, यह एक ऑफलाइन स्पीच इंजन है।"
engine.say(text)
engine.runAndWait()
if "w" in "wert":
    print("yes")