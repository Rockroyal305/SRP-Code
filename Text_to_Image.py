# Example directly sending a text string:

import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'johnathan szeto',
    },
    headers={'api-key': 'a92a0b95-74ae-49ad-ab7e-764a958f786b'}
)
print(r.json())
