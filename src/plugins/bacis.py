from text_to_speech import TextToSpeech

class BasicCommands:
    def __init__(self):
        self.speak_engine = TextToSpeech(language="ru")

    def say_hello(self):
        self.speak_engine.say("Привет, я Лекс. Чем могу помочь?")

    def say_goodbye(self):
        self.speak_engine.say("До свидания!")
    