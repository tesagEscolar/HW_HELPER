from Gemini.geminiAPI import geminiAssistant
from Utils.files import generate_task, load_tasks


class Jarvis():
    def __init__(self, voice=None, version = '1.5') -> None:
        self.voice = voice if voice else "Ellie" 
        self.gemini = geminiAssistant(version=version)
        self.imageGen = None

 

    def speak(self, text):
        
        if self.voice:
            print(f'{self.voice}: {text}\n')
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
            command = input('Me: ').lower()
            if command == 'bye':
                exit()
                break
            response = self.process_command(command)
            self.speak(response)
