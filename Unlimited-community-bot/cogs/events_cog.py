import discord
from discord.ext import commands
import os
import json

with open('data.json') as f:
  	data = json.load(f)




class Events(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def logs(event, *args, **kwargs):
		await get.channel("admin-logs").send(f"```{format_exc()[-1994:]}```")
		return


def setup(client):
	client.add_cog(Events(client))