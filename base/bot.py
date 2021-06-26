from discord.ext import commands
from database import MongoDB

class Demonize(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded = True
        self.db = MongoDB()

    async def on_ready(self):
       #if not self.loaded:
         print(f"[Session] : O bot {self.user.name} está online.") 

    async def on_message(self, message):
       ctx = await self.get_context(message)
       
       if not self.loaded or ctx.guild is None:return   
       if ctx.author.bot or not ctx.channel.permissions_for(ctx.guild.me).send_messages:return
       if not ctx.valid:return
       
       ctx.db = await self.db.get_guild(guild_id=ctx.guild.id)
       
       await self.invoke(ctx)