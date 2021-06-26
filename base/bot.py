from discord.ext import commands

class Demonize(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded = False
    
    async def on_ready(self):
       #if not self.loaded:
         print(f"[Session] : O bot {self.user.name} está online.") 