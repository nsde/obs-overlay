import os
import time
import twitch

from dotenv import load_dotenv

load_dotenv()

def on_message(channel, user, text):
    print(user, text)

helix = twitch.Helix(client_id=os.getenv('TWITCH_ID'), client_secret=os.getenv('TWITCH_SECRET'), use_cache=True)
twitch.Chat(channel='#' + os.getenv('TWITCH_CHANNEL'), nickname=os.getenv('TWITCH_NAME'), oauth=os.getenv('TWITCH_OAUTH')).subscribe(lambda message: on_message(message.channel, message.sender, message.text))

print()