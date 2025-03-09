# import asyncio
# import base64
# import io
# import json
# import aiofiles
# import pygame
# import requests

# API_BASE_URL = "https://api.sws.speechify.com"
# API_KEY = "XuiiEbnC2LUkFOA0QzO34XpYvE1JBDx5--jd0ips6xY="

# async def get_voices_speechify():
#     url = f"{API_BASE_URL}//v1/voices"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#     }
#     resp = requests.get(url, headers=headers)
#     print(resp.json())
#     return  resp.json()


# async def get_audio(text):
#     url = f"{API_BASE_URL}/v1/audio/speech"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json",
#     }
#     payload = {
#         "input": f"<speak>{text}</speak>",
#         "voice_id": kratos,
#         "audio_format": "mp3",
#     }

#     response = requests.post(url, headers=headers, data=json.dumps(payload))

#     if response.status_code != 200:
#         raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

#     response_data = response.json()
#     decoded_audio_data = base64.b64decode(response_data["audio_data"])

#     pygame.mixer.init()

#         # Create a byte stream from the audio data
#     audio_data = io.BytesIO(decoded_audio_data)

#     # Load the audio data into Pygame
#     pygame.mixer.music.load(audio_data, 'mp3')
#     pygame.mixer.music.play()

#     # Keep the program running until the audio is finished
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)  # Wait until the audio finishes

#     return decoded_audio_data

