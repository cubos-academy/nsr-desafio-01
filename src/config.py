import requests, ngrok
from utils import telegramApiUrl

# Webhook configuration:
def getWebhook():
  print('[STATUS]: Getting Render webhook service informations...')
  webhook = requests.get('https://api.render.com/v1/services?name=apod-bot-webhook&limit=1', headers={
    'authorization': f'Bearer {env_vars['RENDER_API_KEY']}'
  }).json()[0]

  print(f'[STATUS]: Webhook get successfully!')
  return webhook["service"]["serviceDetails"]["url"]

def setBotWebhook():
  print('[STATUS]: Bot configuration started.')

  # Get Render public URL to set webhook:
  webhook_url = getWebhook();
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
