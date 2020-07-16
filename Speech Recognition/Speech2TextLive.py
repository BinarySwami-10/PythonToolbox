import speech_recognition as sr 
# import pyttsx3  
def startAssistant():
    r = sr.Recognizer()  
    with sr.Microphone() as source2: 
        r.adjust_for_ambient_noise(source2, duration=0.2) 
        print('listening')
        while 1:
            try:
                audio2 = r.listen(source2,timeout=1)
                MyText = r.recognize_google(audio2,language=language)
                print(MyText)
                if 'hey' in MyText:
                    print('were you talking to me master?')
                if stopWord in MyText:
                    break
            except Exception as e:
                # print(e)
                pass

language='en-IN' # te=telugu hi=hindi en=english
stopWord='stop stop' # this will stop listening if this is present in ur speech

startAssistant()