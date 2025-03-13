import pyttsx3

class TextToSpeech:
    def __init__(self, language: str):
        self.language = language
        self.engine = pyttsx3.init()

        self.languages_full = {
            "ru": "Russian",
            "en": "English"
        }

    def check_language(self):
        voices = self.engine.getProperty("voices")
        language_ = self.languages_full.get(self.language)

        for voice in voices:
            if language_ in voice.name:
                return voice.id
            
        return None

    def say(self, text):
        voice_id = self.check_language()

        if voice_id:
            self.engine.setProperty("voice", voice_id)
            self.engine.setProperty("rate", 150)
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            raise ValueError("Language not found")
