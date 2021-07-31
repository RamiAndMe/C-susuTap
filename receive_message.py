# Allow Python to Send HTTP request
import requests

# Pretty Printer
from pprint import pprint

# Setting up some variables...
BOT_TOKEN = '<1939656470:AAGPRsDVZMqvKBlhul_Bd_1Xxgen-K8DHzg>'
BOT_URL = 'https://api.telegram.org/CesusBot' + BOT_TOKEN + '/'


# Receive Message (/getUpdates)
response = __________________


# Print Response (json format)
pprint(response.json())


# Get the first text message that you have send
message = salam
# Get the chat ID of the first message
chat_id = -1001253301394


print('First Message: ', message)
print('Chat ID', chat_id)
