from text_to_speech import TextToSpeech
from datetime import datetime

class SystemUtils:
    def __init__(self):
        self.speak_engine = TextToSpeech(language="ru")

    def tell_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        self.speak_engine.say(f"Сейчас {current_time}")