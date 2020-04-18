import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Ta funkcja czyta zadany tekst
def speak(text):
    engine.say(text)
    engine.runAndWait()

instructions = ['Dzień dobry', 'Dowidzenia', 'Jak się masz?']
instructionsApproved = []

speak("""Importuję następujące komendy głosowe""")
for instr in instructions:
    speak('Komenda')
    speak(instr)
    instructionsApproved.append(instr)
speak("W bazie posiadam następujące komendy")
speak(instructionsApproved)