import json
import os
import signal
import threading
from datetime import datetime

import dotenv
import hata

from botdata import BotData

dotenv.load_dotenv()

azuki: hata.discord.Client = hata.Client(os.getenv('token'))
data = BotData('data.json')


@azuki.events
async def ready(client):
    print(f'{client:f} logged in.')


@azuki.events
async def message_create(client: hata.discord.Client, message: hata.discord.Message):
    if message.author.is_bot:
        return

    elif message.content == '.ping':
        await client.message_create(message.channel, f'pong! ({(datetime.now() - message.created_at).seconds // 1000}ms)')
    
    elif message.content.startswith('.set '):
        args = message.content.split()[1:]
        if len(args) != 2:
            return await client.message_create(message.channel, 'Command `set` accepts 2 arguments')
        data[args[0]] = args[1]
        await client.message_create(message.channel, f'`"{args[0]}": "{args[1]}"`')
    
    elif message.content.startswith('.get '):
        args = message.content.split()[1:]
        if len(args) != 1:
            return await client.message_create(message.channel, 'Command `get` accepts 1 argument')
        await client.message_create(message.channel, f'`"{args[0]}": "{data[args[0]]}"`')

    elif message.content == '.stop':
        data.save()

        for client_ in hata.CLIENTS:
            await client_.disconnect()

        client.loop.stop()
        thread_id = threading.main_thread().ident
        os.kill(thread_id, signal.SIGKILL)


azuki.start()
