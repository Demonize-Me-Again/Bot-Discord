from os import environ
from motor import motor_asyncio
from .model import Guild
from .data import guild_dict

class MongoDB:
    def __init__(self):
      self.connection = motor_asyncio.AsyncIOMotorClient(environ['URL_DB'])
      self.db = db = self.connection[environ['NAME_DB']]
      self.guilds = db.guilds

    async def insert_guild(self, guild_id):
        guild_dict['_id'] = guild_id
        
        await self.guilds.insert_one(guild_dict)
        
        return guild_dict


    async def get_guild(self, guild_id):
        data = await self.guilds.find_one({"_id": guild_id})
        
        if data is None:
           data = await self.insert_guild(guild_id)
        
        return Guild(data, self.guilds) 