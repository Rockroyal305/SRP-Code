import os
from google.cloud import speech

'''if problems, try pip install google-cloud-speech and try again
imports the Google Cloud client library'''
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\rockr\Desktop\Code\SRP\sample-key.json"

# instantiates a client
client = speech.SpeechClient()

# the name of the audio file to transcribe
for i in range(10, 19, 1):
    print(i)
    gcs_uri = "gs://srp_speech_to_text/SRP Audio Files/Speech" + \
        str(i) + "_8k.wav"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
    )

    # detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    results = []
    for result in response.results:
        s = result.alternatives[0].transcript
        if(s[0] == ' '):
            s = s[:0] + s[1:]
        print(s)
        results.append(s)
