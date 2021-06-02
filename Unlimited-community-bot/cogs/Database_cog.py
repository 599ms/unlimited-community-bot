import discord
from discord.ext import commands
import json
import mysql.connector

with open('data.json') as f:
  	data = json.load(f)

class Database_cog(commands.Cog):
	def __init__(self, client):
		self.client = client


	


def setup(client):
	client.add_cog(Database_cog(client))