import speech_recognition as sr
import pyttsx3
# from gtts import gTTS
import os
from Ellie.ellie import Ellie
from Gemini.geminiAPI import geminiAssistant
from SDXL import ImageScraper
from Utils.files import generate_task, load_tasks
from image_widget import ImageGridWidget


class Jarvis():
    def __init__(self, voice=None, version = '1.5') -> None:
        self.voice = Ellie(voice) if voice else None 
        self.engine = self.initEngine()
        self.gemini = geminiAssistant(version=version)
        self.imageGen = None

    # Initialize the recognizer and text-to-speech engine
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 600
    recognizer.pause_threshold = 1
 

    def initEngine(self):
        if self.voice: return None
        engine = pyttsx3.init()
        engine.setProperty('voice', engine.getProperty('voices')[1].id)
        engine.setProperty('voice', engine.getProperty('rate') - 300)
        return engine


    # def listen(self):
    #     with sr.Microphone(device_index=1) as source:
    #         print("Listening...")
    #         recognizer.adjust_for_ambient_noise(source, 2)
    #         audio = recognizer.listen(source)
    #         try:
    #             text = recognizer.recognize_google(audio, language="en-US")
    #             print(f"You said: {text}")
    #             return text.lower()
    #         except sr.UnknownValueError:
    #             return "Sorry, I did not understand that."
    #         except sr.RequestError:
    #             return "Sorry, I'm having trouble connecting to the service."


    def speak(self, text):
        
        if self.voice:
            print(f'{self.voice.voice.name}: {text}\n')
            status = self.voice.speak(text)
            if status: return
    
            self.engine.say(text)
            self.engine.runAndWait()
            return
        
        print(f'Assistant: {text}\n')


    def process_command(self, command):
        if 'hello' in command:
            return "Hello! How can I assist you?"
        if 'your name' in command:
            return f"My name is {self.voice.voice.name if self.voice else 'Friday'}, at your service!"
        if 'bye' in command:
            return "Goodbye! Have a great day!"
        if 'image' in command:
            self.genImages(command)
            return 'Here are some images:'
        else:
            return self.gemini.sendSimpleTask(command)

    def genImages(self, command):
        prompt, style = self.gemini.getImage(command)
        imageGen = ImageScraper()
        images = imageGen.get_images(prompt=prompt, artStyle=style)
        if images:
            imageGen.close()
            image_widget = ImageGridWidget(images)
            image_widget.display_images()  # Show the widget
        else:
            # Close the scraper
            imageGen.close()

    def test():
        return sr.Microphone.list_microphone_names()

    def run(self, command=None, complex = False, mode='chat'):
        
        if mode != 'chat':
            
            if complex:
                tasks = load_tasks()

                for task in tasks:
                    task = self.gemini.executeTasks(task)
                    generate_task(task)
                resp = 'Tasks finished succesfully'
            
            elif command:    
                resp = self.gemini.sendSimpleTask(command)
            else:
                resp = 'Please ask something'
            
            self.speak(resp)
            
            return resp
        
        while True:
            # self.speak('How can I help you?')
            command = input('Me: ').lower()
            if command == 'bye':
                exit()
                break
            response = self.process_command(command)
            self.speak(response)