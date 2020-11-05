import os
import pathlib
from datetime import datetime

import dotenv
import hata

dotenv.load_dotenv()

azuki = hata.Client(os.getenv('token'))


@azuki.events
async def ready(client):
    print(f'{client:f} logged in.')


@azuki.events
async def message_create(client, message: hata.discord.Message):
    if message.author.is_bot:
        return

    if message.content == '.ping':
        await client.message_create(message.channel, f'pong! ({(datetime.now() - message.created_at).seconds // 1000}ms)')

azuki.start()
