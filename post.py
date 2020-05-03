import requests
import json

def send_form():
    POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=57df0ce7c475359f84af91d686e34c1a7105782e"
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(POST, files=answer)
    print(submit.headers)

send_form()