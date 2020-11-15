import json
import os
import signal
import threading
from datetime import datetime
from hata import Embed, ReuAsyncIO, KOKORO, Client, start_clients, VoiceClient
import hata
import dotenv
from botdata import BotData
from hata.discord.guild import GuildPreview

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
        embed = Embed(
         'Pong!',
         f'({(datetime.now() - message.created_at).seconds // 1000}ms)',
         color=0x00fbff
         )
        await client.message_create(message.channel, embed=embed)

    elif message.content == '.help':
        embed = Embed(
         'List Of Commands',
         '.ping\n.owners\n.set\n.set\n.get\n.stop',
         color=0x00fbff
         )
        await client.message_create(message.channel, embed=embed)

    elif message.content == '.owners':
        embed = Embed(
         'Owners',
         f'{", ".join(u.full_name for u in azuki.owners)}',
         color=0x00fbff
         )
        await client.message_create(message.channel, embed=embed)
    
    elif message.content.startswith('.set '):
        args = message.content.split()[1:]
        if len(args) != 2:
            embed = Embed(
             'Error',
             'Command `set` accepts 2 arguments',
             color=0xff0000
            )
            return await client.message_create(message.channel, embed=embed)
        data[args[0]] = args[1]
        embed = Embed(
         'Success',
         f'`"{args[0]}" has been set as "{data[args[0]]}"`',
         color=0x00fbff
        )
        await client.message_create(message.channel, embed=embed)
    
    elif message.content.startswith('.get '):
        args = message.content.split()[1:]
        if len(args) != 1:
            embed = Embed(
             'Error',
             'Command `get` accepts 1 argument',
             color=0xff0000
            )
            return await client.message_create(message.channel, embed=embed)
        embed = Embed(
         'Value Retrieved',
         f'`"{args[0]}" is equal to  "{data[args[0]]}"`',
         color=0x00fbff
        )
        await client.message_create(message.channel, embed=embed)

    elif message.content == '.stop':
        data.save()

        for client_ in hata.CLIENTS:
            await client_.disconnect()

        client.loop.stop()
        thread_id = threading.main_thread().ident
        os.kill(thread_id, signal.SIGKILL)
    
    elif message.content.startswith('.'):
        embed = Embed(
         'Invalid command',
         'try using: `.help`',
         color=0xff0000,
            )
        message = await client.message_create(message.channel,embed=embed)