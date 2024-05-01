# api/openai.py
import os
import requests
from requests.exceptions import RequestException

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}


def get_lyrics(prompt, mode, max_tokens):
    system_message = "I need you to help me write a song." if mode == "song" else "I need you to help me write a poem."
    user_message = f"{system_message} {prompt}"
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": user_message
            }
        ],
        "max_tokens": max_tokens
    }
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()  # This will raise a RequestException if the status code is not 200
        return response.json()['choices'][0]['message']['content']
    except RequestException as e:
        if e.response.status_code == 400:
            raise Exception("Bad Request: The server could not understand the request due to invalid syntax.") from e
        elif e.response.status_code == 401:
            raise Exception("Unauthorized: The client must authenticate itself to get the requested response.") from e
        elif e.response.status_code == 403:
            raise Exception("Forbidden: The client does not have access rights to the content.") from e
        elif e.response.status_code == 404:
            raise Exception("Not Found: The server can not find the requested resource.") from e
        elif e.response.status_code == 500:
            raise Exception("Internal Server Error: The server has encountered a situation it doesn't know how to "
                            "handle.") from e
        else:
            raise Exception(f"Error: {e.response.status_code}, {e.response.text}") from e
