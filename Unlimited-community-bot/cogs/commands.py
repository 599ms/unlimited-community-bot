import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import asyncio


class Commands(commands.Cog):
	def __init__(self, client):
		self.client = client

		##Help
	@commands.command(aliases = ["hjælp", "commands", "komandoer"])
	async def help(self, ctx):
	    embed = discord.Embed(
	        title = "Hjælp menu",
	        color = 0x2f3136
	    )
	    embed.add_field(
	        name = "Admin", value="Kun for admins!", inline=False
	    )
	    embed.set_footer(
	        text = f"{ctx.guild.name}"
	    )
	    await ctx.send(embed = embed)


	
		

	    ##Admin
	@commands.command()
	async def admin(self, ctx):
	    embed = discord.Embed(
	        title = "Admin menu",
	        color = 0x2f3136
	    )
	    embed.add_field(
	        name = "Restart", value="Genstarter discord botten hvis der er fejl eller lign. `Kræver Dev Team rolle`", inline=False
	    )
	    embed.add_field(
	        name = "Nuke", value="Fjerner en kanal og laver en kopi (Bruges til hvis beskeder er mere end 14 dage gamle). `Kræver Dev Team rolle`", inline=False
	    )
	    embed.add_field(
	        name = "Purge <ANTAL>", value="Fjerner de bestemte antal beskeder i chatten `Kræver Dev Team rolle`", inline=False
	    )
	    embed.set_footer(
	        text = f"{ctx.guild.name}"
	    )
	    await ctx.send(embed = embed)

	    ##Purge
	@commands.command(pass_context=True)
	@commands.has_role('Bot adgang')
	async def purge(self, ctx, amount=5):
	    channel = ctx.message.channel
	    messages = []
	    async for message in channel.history(limit=amount + 1):
	              messages.append(message)

	    await channel.delete_messages(messages)
	    await ctx.send(f'{amount} beskeder fjernet')

	    ##Mute
	@commands.command()
	@commands.has_role('Bot adgang')
	async def mute(self, ctx, user : discord.Member, duration = 0,*, unit = None):
	    roleobject = discord.utils.get(ctx.message.guild.roles, id=837027860647772170)
	    await ctx.send(f"Muted {user.mention} for {duration}{unit}")
	    await user.add_roles(roleobject)
	    if unit == "s":
	        wait = 1 * duration
	        await asyncio.sleep(wait)
	    elif unit == "m":
	        wait = 60 * duration
	        await asyncio.sleep(wait)
	    elif unit == "t":
	        wait = 3600 * duration
	        await asyncio.sleep(wait)
	    await user.remove_roles(roleobject)
	    await ctx.send(f"{user.mention} er unmuted")
       
	@commands.command()
	async def sele(self, ctx):
		await ctx.send("Husk din sele!")

	@commands.command()
	async def pog(self, ctx):
		await ctx.send("Ja Pog er meget sej")

	    ##Nuke
	@commands.command()
	@commands.has_role('Bot adgang')
	async def nuke(self, ctx):

	    channel = ctx.channel
	    channel_position = channel.position

	    new_channel = await channel.clone()
	    await channel.delete()
	    await new_channel.edit(position=channel_position, sync_permissions=True)
	    embed = discord.Embed(
	        title = "Nuke",
	        color = 0x2f3136
	    )
	    embed.add_field(
	        name = "Kanalen er blevet bollet i kussen!", value = "** **", inline=False
	    )
	    embed.set_footer(
	        text = f"Admin: {ctx.author}"
	    )
	    await new_channel.send(embed = embed)
	    return

	@commands.command()
	async def support(self, ctx):
		staffrole = discord.utils.get(ctx.guild.roles, id=843451048727543808)
		await ctx.send(f"{staffrole.mention}")
		embed = discord.Embed(
			title = "Support sag",
			color = 0x2f3136
		)
		user = ctx.author
		embed.add_field(
			name = f"{user} har brug for hjælp!", value = "Staff har nu fået besked at du venter i <#837027961008947270>, og har brug for hjælp!\n\nVi ser gerne at du har tålmodighed, og venter på at der kommer en staff.", inline=False)
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(Commands(client))