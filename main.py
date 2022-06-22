from chatbot import ChatBot
import speech_recognition as sr
import os
from gtts import gTTS

# bu kısım Bülent'ten alındı 
# SPEECH TO TEXT
# r = sr.Recognizer()
chatBot = ChatBot()

# kullanıcıya seçenek sunmak istedim
# sesli ya da yazarak sorusunu sorabiliyor
# isterse sorusunun cevabını dinleyebiliyor
while True:
    choice = int(input("Sorunuzu yazmak için 1'e basınız. \nSorunuzu sesli sormak için 2'ye basınız. \nKonuşmayı sona erdirmek için 3'e basınız.\n"))
    
    if (choice == 1):
        text_1 = input("Size nasıl yardımcı olabiliriz? \n")
        answer = chatBot.chatbot_question(text_1)
        print(answer)
        
        # sorunun cevabını dinlemek için 
        listen = int(input("Sorunuzun yanıtını sesli olarak dinlemek için 1'e basınız. \nDevam etmek için herhangi bir rakama basınız.\n"))
        if (listen == 1):
            # TEXT TO SPEECH
            # cevap konuşmaya çeviriliyor
            tts = gTTS(text = answer, lang="tr")
            # speech.mp3 olarak kaydediliyor
            tts.save("speech.mp3")
            # speech.mp3 dosyası çalıştırılıyor
            os.system("speech.mp3")
        else:
            continue 
        
    if (choice == 2):
        # SPEECH TO TEXT
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            
            print("Konuşun...")
            data = r.record(source, duration=10)
            
            print("Sesiniz Metne Dönüştürülüyor…")
            text_2 = r.recognize_google(data,language="tr")
            print(text_2)

        answer = chatBot.chatbot_question(text_2)
        print(answer)
        
        listen = int(input("Sorunuzun yanıtını sesli olarak dinlemek için 1'e basınız. \nDevam etmek için herhangi bir rakama basınız.\n"))
        if (listen == 1):
            # TEXT TO SPEECH
            # cevap konuşmaya çeviriliyor
            tts = gTTS(text = answer, lang="tr")
            # speech.mp3 olarak kaydediliyor
            tts.save("speech.mp3")
            # speech.mp3 dosyası çalıştırılıyor
            os.system("speech.mp3")
        else:
            continue
    
    if (choice == 3):
        print("Konuşma sona erdirildi. Umarım yardımcı olabilmişimdir.")
        break
    
    # kullanıcı girmesi gereken 1, 2 veya 3 rakamlarını girmezse
    if (choice > 3):
        print("Yanlış bir rakam girdiniz!!!")

# TEXT TO SPEECH
"""
# Text will be translated to speech and saved as “speech.mp3”
tts = gTTS(text=answer, lang="tr")
tts.save("speech.mp3")
# For run “speech.mp3” file
os.system("speech.mp3")
"""