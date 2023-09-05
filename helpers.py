import requests
import os
API_URL = "https://api-inference.huggingface.co/models/volvoDon/petro-daemon"
headers = {"Authorization": f"Bearer {os.getenv('HKEY')}"}
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

