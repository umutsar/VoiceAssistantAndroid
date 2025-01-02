import speech_recognition as sr
import os
import requests

recognizer = sr.Recognizer()

def speak(text):
    os.system(f"termux-tts-speak -l tr-TR -r 1.3 '{text}'")

while True:
    with sr.Microphone() as source:
        print("Sizi dinliyorum... (Çıkmak için 'Çık' yazın)")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            print("Ses alındı, işleniyor...")


            text = recognizer.recognize_google(audio, language="tr-TR")
            print(f"Söylediğiniz şey: {text}")

            if 'çık' in text.lower():
                print("Çıkılıyor...")
                speak("Çıkılıyor...")
                break

            data = {"prompt": text}
            try:
                api_url = "http://localhost:3001/generateContent"
                response = requests.post(api_url, json=data)
                response_data = response.json()

                if response.status_code == 200:
                    gemini_response = response_data.get("response")
                    print(f"Gemini'den gelen cevap: {gemini_response}")
                    speak(gemini_response) 
                else:
                    print("Gemini API hatası")
            except requests.exceptions.RequestException as e:
                print(f"API isteği sırasında hata oluştu: {e}")

        except sr.UnknownValueError:
            print("Google Speech Recognition sesi anlayamadı")
        except sr.RequestError as e:
            print(f"Google Speech Recognition servisine ulaşılamıyor; hata: {e}")
