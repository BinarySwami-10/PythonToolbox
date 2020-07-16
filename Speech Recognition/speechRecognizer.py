import speech_recognition as sr 
# import pyttsx3  

language='en' # te=telugu hi=hindi en=english
stopWord='ఆగు' # this will stop listening if this is present in ur speech
r = sr.Recognizer()  

# with sr.Microphone() as source2: 
demo=sr.AudioFile('2.wav')
with demo as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2) 
    print('listening')
    # while 1:
    # audio2 = r.listen(source2,timeout=1) 
    audio2 = r.record(demo)
    try:
        MyText = r.recognize_google(audio2,language=language)
        MyText = MyText 
        print(MyText) 
        # SpeakText(MyText)
        # if stopWord in MyText:
        #     break
    except Exception as e:
        print(e)