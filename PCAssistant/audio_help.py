import speech_recognition
import webbrowser

class audioQuery():

    query = ''
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5

    commands_dict = {
        'commands': {
            'open_youtube' : ['открой youtube', 'включи youtube'],
            'open_twitch' : ['открой twitch', 'включи twitch', 'включи твич', 'открой твич']
        }
    }

    def __listen_command(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                print("Говорите")
                audio = self.sr.listen(source=mic)
                query = self.sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                print (query)
                return query
        except speech_recognition.UnknownValueError:
            return 'Не удалось распознать речь'

    def __open_youtube(self):
        webbrowser.open("https://www.youtube.com/")

    def __open_twitch(sefl):
        webbrowser.open("https://twitch.tv")

    def startModule(self):
        self.query = self.__listen_command()
        for key, value in self.commands_dict['commands'].items():
            if self.query in value:
                if key == 'open_youtube':
                    self.__open_youtube()
                elif key == 'open_twitch':
                    self.__open_twitch()