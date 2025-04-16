import requests
import json
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7963539181:AAGt_4IIW1bVMRkUk9B_AbVOEMQp6CWjeOU'
TEXT = ' Ты очень хороший человек!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int


while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            name_id = result['message']['chat']['first_name']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Приветик, {name_id}{TEXT}')

    time.sleep(1)
    counter += 1