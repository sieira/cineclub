import time

from client_corleone.botclient import BotClient
# from controller import CineclubController

import settings

client = BotClient(settings.BOT_TOKEN, max_retries=5)
# controller = CineclubController()
in_buffer = client.updates()

while 'Don\'t stop me, nooooooow':
    for update in in_buffer:
        # action, params = controller.parse(update.message.text)
        # exit_code, response = action(*params)
        # client.send_text(update.message.chat.cid, response)
        client.send_test(update.message.text)
    time.sleep(1)
