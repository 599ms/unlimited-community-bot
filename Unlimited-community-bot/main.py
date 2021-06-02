### DENNE BOT ER LAVET TIL UNLIMITED COMMUNITY OG ER KODET AF pog#3713

from configparser import InterpolationMissingOptionError
import discord
from discord.ext import commands
from discord import *
import os
import mysql.connector
import requests
from colorama import *
import pipes
from datetime import *
import time
import sys
import asyncio
import traceback
import re
from fivem import FiveM
import json
import subprocess
import datetime

with open('data.json') as f:
  data = json.load(f)
  
os.system("title DISCORD BOT")

client = commands.Bot(command_prefix=data['Prefix'], case_insensitive=True)
client.remove_command('help')

for file in os.listdir("cogs"):
    if file.endswith(".py") and not file.startswith("_"):
        client.load_extension(f"cogs.{file[:-3]}")

mydb = mysql.connector.connect(
	  host=data['host'],
	  user=data['user'],
	  password=data['password'],
	  database=data['database']
	)

@client.command()
async def ping(ctx):
  lat = str(client.latency)[3] + str(client.latency)[4]
  await ctx.send(f'Bottens ping er på {lat}ms')


@client.command()
@commands.has_role('Bot adgang')
async def adduser(ctx, discord_id, user_id):
    if discord_id == None:
      await ctx.send("Skriv et Discord ID!")
    if user_id == None:
      await ctx.send("Skriv et user_id!")

    mycursor = mydb.cursor()
    sql = f"INSERT INTO discord_profiles (discord_id, user_id) VALUES (%s, %s)"
    val = (f"{discord_id}", f"{user_id}")
    mycursor.execute(sql, val)

    mydb.commit()

    user = await client.fetch_user(int(discord_id))
    embed = discord.Embed(
      title = f"User: {user} \nDiscord ID: {discord_id}\nUser_id: {user_id}\n\nStatus: Er blevet tilføjet til databasen :white_check_mark: ",
      color = 0x7CFC00,
      timestamp=datetime.datetime.utcnow()
      )
    await ctx.send(embed = embed)
    print(f"{Fore.RESET}[{Fore.GREEN}User: {user}{Fore.RESET}] {Fore.RESET}  [{Fore.GREEN}Discord ID: {discord_id} {Fore.RESET}]   [{Fore.GREEN}user_id: {user_id}{Fore.RESET}]\nStatus: {Fore.GREEN}Added{Fore.RESET} user to database\n\n")


@client.command()
@commands.has_role('Bot adgang')
async def removeuser(ctx, discord_id):
    if discord_id == None:
      await ctx.send("Skriv et Discord ID!")

    mycursor = mydb.cursor()
    sql = f"DELETE FROM main_database WHERE discord_id = '{discord_id}"
    mycursor.execute(sql)

    mydb.commit()

    user = await client.fetch_user(int(discord_id))
    embed = discord.Embed(
      title = f"User: {user} \nDiscord ID: {discord_id}\n\nStatus: Er blevet tilføjet til databasen :white_check_mark: ",
      color = 0x7CFC00,
      timestamp=datetime.datetime.utcnow()
      )
    await ctx.send(embed = embed)
    print(f"{Fore.RESET}[{Fore.GREEN}User: {user}{Fore.RESET}] {Fore.RESET}  [{Fore.GREEN}Discord ID: {discord_id} {Fore.RESET}] \nStatus: {Fore.GREEN}Added{Fore.RESET} user to database\n\n")

@client.command(help = "Dette er en profil command")
async def profil(ctx):
  try:
    discord_id_num = ctx.author.id
    mycursor = mydb.cursor()

    sql = f'SELECT * FROM vrp_user_ids WHERE identifier = "discord:{discord_id_num}";'

    mycursor.execute(sql)

   
    myresult = mycursor.fetchall()

    list1 = myresult

    *x, = list1[0]
    id,secondpart = x

    sql = f'SELECT * FROM vrp_user_identities WHERE user_id = "{secondpart}";'

    mycursor.execute(sql)

    uhhhhresult = mycursor.fetchall()
    

    list2 = uhhhhresult

    *x, = list2[0]
    id,id2,id3,id4,id5,id6 = x

    sql = f'SELECT * FROM vrp_user_vehicles WHERE user_id = "{secondpart}";'

    mycursor.execute(sql)

    uhhhhresult2 = mycursor.fetchall()
    list3 = uhhhhresult2

    *x, = list3[0]
    id100, id101, id102, id103, id104, id105, id106, id107, id108, id109, id110, id111, id112, id113, id114, id115, id116, id117, id118, id119, id120, id121, id122, id123, id124, id125, id126, id127, id128, id129, id130, id131, id132, id133, id134, id135, id136, id137, id138, id139, id140, id141, id142, id143, id144, id145, id146, id147, id148 = x
    #48

    sql = f'SELECT * FROM vrp_user_moneys WHERE user_id = "{secondpart}";'

    mycursor.execute(sql)

    uhhhhresult24 = mycursor.fetchall()
    list4 = uhhhhresult24
    *x, = list4[0]
    useridman, wallet, bank, dept, depositnlogin = x

    user = await client.fetch_user(int(discord_id_num))
    
    embed = discord.Embed(
      title = "Profile",
      color = 0x2f3136,
      timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(
      name = f"Username: ", value = user, inline=False
    )
    embed.add_field(
      name = "Discord ID: ", value = discord_id_num, inline=False
    )
    embed.add_field(
      name = f"Ingame info: ", value = f"Navn: {id4} {id5}\nAlder: {id6}\nIngame ID: {secondpart}\n", inline=True
    )
    embed.add_field(
      name = "**Penge**", value = f"Pengepung: {wallet}\nBank: {bank}", inline=False
    )
    embed.add_field(
      name = f"Biler: ", value = f"Navn: {id101}", inline=True
    )
    
    await ctx.send(embed = embed)
  except IndexError as e:
    embed = discord.Embed(
      title = "FEJL",
      color = 0x2f3136,
      timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(
      name = "Du har ikke linket dit Discord med FiveM!", value = "Hvis du tror dette er en fejl i vores system, bedes du kontakte pog#3713 for at få ydligere oplysninger."
    )
    await ctx.send(embed = embed)

@client.command(name="updatestatus")
@commands.has_role('Bot adgang')
async def _main(ctx):
        fivem = FiveM(ip=data['Server_IP'], port=data['Server_Port'])

        server = await fivem.get_server_info()

        currentclients = server.clients
        maxclients = server.max_clients
        loop = asyncio.get_event_loop()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{currentclients}/{maxclients}"))
        await ctx.send("Status er nu blevet updated!")

@client.event
async def on_ready():
	    print(f'{client.user.name} is ready to go.')

	    now = datetime.now()

	    a = now.strftime("%H:%M:%S")
	    b = date.today()

	    id_channel = data['on_ready']
	    channel = client.get_channel(id_channel)
	    embed = discord.Embed(
	        title = "Online!",
	        color = 0x2f3136
	    )
	    embed.add_field(
	        name = f"Jeg er nu online igen!", value = f"Dato: {b}\nTid: {a}", inline=False
	    )
	    await channel.send(embed = embed)
      
      
      

      


client.run(data['discord_bot_token'])