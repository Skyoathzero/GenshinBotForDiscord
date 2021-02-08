import discord
from discord.ext import commands

class test(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['se'])
    async def ping(self,ctx):
        await ctx.send("Pong!!")

def setup(client):
    client.add_cog(test(client))