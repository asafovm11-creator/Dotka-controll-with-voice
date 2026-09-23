import numpy as np
import pydirectinput
import scipy.io.wavfile as wav
import sounddevice as sd
import speech_recognition as sr


pydirectinput.PAUSE = 0.05


def play_beep():
    sr_rate = 44100
    beep_duration = 0.15  #150 миллисекунд
    freq = 1000  # Частота тона: 1000 Гц
    t = np.linspace(0, beep_duration, int(sr_rate * beep_duration), False)
    # Звуковая синусоида (0.3 - комфортная громкость, чтобы не глушило)
    tone = np.sin(freq * t * 2 * np.pi) * 0.3
    sd.play(tone, sr_rate)
    sd.wait()  # Ждем окончания сигнала перед началом записи


while True:
    duration = 1.5  # Секунды записи микрофона
    sample_rate = 44100

    print("Слушаю команду...")
    play_beep()  

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
    )
    sd.wait()

    wav.write("output.wav", sample_rate, recording)

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("Команда:", text)

       
        if "первый" in text or "ку" in text:
            pydirectinput.press("q")

        elif "второй" in text or "ве" in text:
            pydirectinput.press("w")

        elif "третий" in text or "ешка" in text:
            pydirectinput.press("e")

        elif "ульта" in text or "ультимейт" in text or "эр" in text:
            pydirectinput.press("r")

        elif "четвёртый" in text:
            pydirectinput.press("d")

        elif "пятый" in text:
            pydirectinput.press("f")

       
        elif "стоп" in text or "стой" in text or "забей" in text:
            pydirectinput.press("s")

        elif "атака" in text or "бить" in text:
            pydirectinput.press("a")

        elif "где я" in text or "герой" in text:
            pydirectinput.press("space")

        elif "тык" in text or "клик" in text:
            pydirectinput.click(button='left')

        elif "бить туда" in text or "огонь" in text:
            pydirectinput.click(button="right")

        
        elif "принеси" in text or "курьер" in text:
            pydirectinput.press("f3")

        elif "магазин" in text or "лавка" in text:
            pydirectinput.press("b")

        elif "закуп" in text or "быстрый закуп" in text:
            pydirectinput.press("f4")

       
        elif "предмет один" in text or "слот один" in text:
            pydirectinput.press("z")

        elif "предмет два" in text or "слот два" in text:
            pydirectinput.press("x")

        elif "тапки" in text or "дагер" in text:
            pydirectinput.press("c")

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Ошибка Google: {e}")
    else: print("hello")

