import speech_recognition as sr

recognizer = sr.Recognizer()

print("KD: Haan boss, main sun raha hoon. 🎙️")
print("KD: Bol boss...")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("KD: Ready. 👂")

    while True:
        try:
            audio = recognizer.listen(source)

            text = recognizer.recognize_google(audio)

            print("Boss:", text)

            if text.lower().strip() == "exit":
                print("KD: Theek hai boss, milte hain. 👑")
                break

            print("KD: Sun liya boss —", text)

        except sr.UnknownValueError:
            print("KD: Boss, samajh nahi aaya. Ek baar phir bol.")

        except sr.RequestError as error:
            print("KD: Speech service connect nahi ho paayi.")
            print(error)
            break
