import discord
from discord.ext import commands
import sys
import subprocess
import asyncio
from fivem import FiveM
import json
import os
import datetime

with open('data.json') as f:
  	data = json.load(f)


class ServerCommands(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.command()
	async def online(self, ctx):
		fivem = FiveM(ip=data['Server_IP'], port=data['Server_Port'])
		server = await fivem.get_server_info()
		currentclients = server.clients
		maxclients = server.max_clients

		helpmenu = discord.Embed(title = "Online Spillere!",color = 0x2f3136, timestamp=datetime.datetime.utcnow())
		helpmenu.add_field(name = f"Der er **{currentclients}/{maxclients}** online på serveren", value = "** **", inline=False)
		helpmenu.set_footer(text = ctx.guild.name)

		await ctx.send(embed = helpmenu)


	@commands.command()
	@commands.has_role('Bot adgang')
	async def restart(self, ctx):
		python = sys.executable
		os.execl(python, python, * sys.argv)
		quit()
		subprocess.call('main.py')
		embed = discord.Embed(title = "Genstarter!", color = 0x2f3136, timestamp=datetime.datetime.utcnow())
		embed.add_field(
			name = "Dette kan tage op til 5 sek!", value = f"** **", inline=False
		)
		embed.set_footer(
			text = f"Admin: {ctx.author}"
		)
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(ServerCommands(client))