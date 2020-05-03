import requests
import json

URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=57df0ce7c475359f84af91d686e34c1a7105782e'

r = requests.get(URL).json()

with open('answer.json', 'w', encoding='utf-8') as f:
	json.dump(r, f, ensure_ascii=False, indent=4)