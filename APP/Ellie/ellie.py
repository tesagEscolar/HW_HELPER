import io
import pygame
import requests
from Ellie.voices import Voices, Keys
apiKey = "89f08c0977ff4a79ad1bd20c5adc56e2"
# Set your API credentials here
API_URL = "https://api.play.ht/api/v2/tts/stream"


class Ellie():
    def __init__(self, voice) -> None:
        self.voice = voice

    def getVoicesPlayHT(self):
        resp = requests.get("https://api.play.ht/api/v2/cloned-voices", headers=self.getHeaders())
        print(resp.text)
        print(resp.content)
    
    def getVoicesPfy(self):
        resp = requests.get("https://api.sws.speechify.com//v1/voices", headers=self.getHeaders())
        print(resp.text)
        print(resp.content)

    def setPayload(self, prompt):
        if self.voice == Voices.ELLIE:
            return  {
            "text": prompt,
            "voice": self.voice.value,
            "output_format": "mp3",
            "speed": 0.8, #0.7
            "sample_rate": 48000,
            "temperature": 0.3,   #0.2
            "voice_guidance":2.1, #1.9
            "text_guidance":0.6,  #0.7
            "voice_engine": "PlayHT2.0-turbo",
            "seed":1,}
        else:
            return {
            "input": f"<speak>{prompt}</speak>",
            "voice_id": self.voice.value,
            "audio_format": "mp3"
            }

    def getHeaders(self):
        if self.voice == Voices.ELLIE:
            return {
                "Authorization": f"Bearer {Keys.PLAYHT_KEY.value}",
                "X-USER-ID": Keys.PLAYHT_USER.value,
                "accept": "audio/mpeg",
                "content-type": "application/json"
            }
        else:
            return {
            "Authorization": f"Bearer {Keys.SPEECHIFY.value}",
            }

    def getUrl(self):
        if self.voice == Voices.ELLIE:
            return "https://api.play.ht/api/v2/tts/stream"
        else:
            return "https://api.sws.speechify.com/v1/audio/speech"

    def speak(self, prompt):
    # Set up headers
        # Set up the payload (the body of the request)
        print('Waiting for audio...')
    
        # Make the POST request
        response = requests.post(url=self.getUrl(), headers=self.getHeaders(), json=self.setPayload(prompt))
        if response.status_code != 200:
            print(response.reason, response.content)
            return False
        self.playVoice(response)

    def playVoice(self, response):
        if response.status_code != 200:
            print(f"Error: {response.status_code} {response.text}")
            return
        # Initialize Pygame mixer
        pygame.mixer.init()

    # Create a byte stream from the audio data
        audio_data = io.BytesIO(response.content)

        # Load the audio data into Pygame
        pygame.mixer.music.load(audio_data, 'mp3')
        pygame.mixer.music.play()

        # Keep the program running until the audio is finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Wait until the audio finishes