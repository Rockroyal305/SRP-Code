# if problems, try pip install google-cloud-speech and try again

# Imports the Google Cloud client library
from google.cloud import speech

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\rockr\Desktop\Code\SRP\sample-key.json"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://srp_speech_to_text/SRP Audio Files/Speech10_8k.wav"

audio = speech.RecognitionAudio(uri=gcs_uri)

# Find out which language to use
lang_code = input(
    "What Language Do You Want to Use? (e.g. en-US, de-DE, fr-FR, hi-IN, zh-CN, etc;)")
if(lang_code != "en-US"):
    print("Sorry, only english is supported!")
    quit()

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    language_code=lang_code,
)

# Detects speech in the audio file
response = client.recognize(config=config, audio=audio)

for result in response.results:
    s = (format(result.alternatives[0].transcript))
    if(s[0] == ' '):
        s = s[:0] + s[1:]
    print(s)
