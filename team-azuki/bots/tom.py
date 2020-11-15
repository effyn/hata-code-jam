from hata import Embed
import hata
import os
import dotenv

dotenv.load_dotenv()
nook: hata.discord.Client = hata.Client(os.getenv('tom_token'))

@nook.events
async def ready(client):
    print(f'{client:f} logged in.')

@nook.events
async def message_create(client: hata.discord.Client, message: hata.discord.Message):
    if message.content.startswith('tom.hello'):
        embed = Embed(
         'Hiya!',
         'How are you doing?',
         color=0x00fbff
         )
        await client.message_create(message.channel, embed=embed)