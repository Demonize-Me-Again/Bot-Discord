from base import Demonize
from os import environ
from discord import Game, Intents
from dotenv import load_dotenv
import asyncio, platform

platform = platform.system()
if platform.lower() == 'windows':
   load_dotenv("./data/config/.env")

intents = Intents.default()
intents.members = True

bot = Demonize(intents=intents, command_prefix='d.', activity=Game('Starting...'))

loop = asyncio.get_event_loop()
task_bot = loop.create_task(bot.run(environ['TOKEN_BOT']))
gathered = asyncio.gather(task_bot)

try:
  loop.run_until_complete(gathered)
except KeyboardInterrupt:
    loop.close()