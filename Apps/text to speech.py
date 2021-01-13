from gtts import gTTS

print("\nThis app is going to convert to text that you entered to speech as text2speech.mp3 file.\n")

while True:
    try:
        text = input(" Please write your text here to convert speech: ")
        file_name = input("Wat is name of the speech? ")
        tts = gTTS(text)
        tts.save(r'C:\Users\ChaN\Desktop\{}.mp3'.format(file_name))
        
    except:
        print("Your text is incorrect, please try again.")


