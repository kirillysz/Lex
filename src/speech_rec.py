import vosk
import pyaudio
import json


class VoskModelSingleton:
    """ Загружает и хранит модель Vosk один раз. """
    _instance = None

    def __new__(cls, model_path):
        if cls._instance is None:
            print("Загрузка модели Vosk...")

            cls._instance = super(VoskModelSingleton, cls).__new__(cls)
            cls._instance.model = vosk.Model(model_path)

            print("Модель загружена!")

        return cls._instance

class SpeechRecognition:
    """ Класс Распознавания речи с использованием модели Vosk. """
    def __init__(self):
        self.model = VoskModelSingleton(r"src\model").model
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)

        self.mic = pyaudio.PyAudio()
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
        self.stream.start_stream()

    def recognize(self):
        while True:
            data = self.stream.read(4096, exception_on_overflow=False)
            if len(data) == 0:
                continue

            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "")

                if text:
                    return text

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.mic.terminate()

