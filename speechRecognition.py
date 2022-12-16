import speechRecognition as sr
import os


def list_micro():
    micro = sr.Recognizer()

    with sr.Microphone() as source:

        # Calls a noise reduction algorithm on the sound
        micro.adjust_for_ambient_noise(source)

        print('Say something: ')

        # Stores what was said in a variable
        audio = micro.listen(source)

    try:
        # Pass the variable to the pattern recognition algorithm
        phrase = micro.recognize_google(audio, language='en-US')

        if "Chrome" in phrase:
            os.system('start Chrome.exe')

        elif "Excel" in phrase:
            os.system('start Excel.exe')

        print('You said: ' + phrase)

    # If it did not recognize the speech pattern, it displays the message
    except sr.UnknownValueError:
        print(f"I didn't understand")

    return phrase


list_micro()
