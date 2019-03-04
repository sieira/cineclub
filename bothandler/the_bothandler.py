import time

from client_corleone.botclient import BotClient
# from controller import CineclubController

import settings

client = BotClient(settings.BOT_TOKEN)
# controller = CineclubController()
in_buffer = client.updates()

for update in in_buffer:
    # action, params = controller.parse(update.message.text)
    # exit_code, response = action(*params)
    # client.send_text(update.message.chat.cid, response)
    client.send_text(update.message.chat.cid, update.message.text)

time.sleep(1)
exit(1)  # Exit in error state so docker-compose triest to restart
