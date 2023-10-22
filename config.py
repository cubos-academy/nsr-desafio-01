import requests, ngrok
from dotenv import dotenv_values

env_vars = dotenv_values('.env')

telegramApiUrl = f'https://api.telegram.org/bot{env_vars['TELEGRAM_API_KEY']}/'

# Webhook configuration/initialization:
def startNgrok():
  print('[STATUS]: Starting Ngrok service...')
  tunnel = ngrok.connect("localhost:5000", authtoken_from_env=True)

  print(f'[STATUS]: Ngrok started successfully!')

  return tunnel.url()

def setBotWebhook():
  print('[STATUS]: Bot configuration started.')

  # Get Ngrok public generated URL to webhook:
  webhook_url = startNgrok();
  # ------------- #


  print('[STATUS]: Setting webhook from bot...')

  # Set Telegram bot webhook:
  response = requests.post(telegramApiUrl + 'setWebhook', params={
    'url': webhook_url,
    'allowedUpdates': '["message"]'
  }).json()
  # ------------- #
  
  if (response['ok']):
    print(f'[STATUS]: Webhook set successfully!')
  else:
    print(f'[ERROR]: Failed to set webhook. Error message: {response['description']}')
# ------------- #
