import json
import signal
import threading
from datetime import datetime
from hata import Embed, ReuAsyncIO, KOKORO, Client, start_clients, VoiceClient
import dotenv
import hata
from hata.discord.guild import GuildPreview
from bots import azuki, tom



start_clients()