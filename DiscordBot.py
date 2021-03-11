# bot.py
import os
import discord
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):

    #This is so the bot can't talk to itself
    if message.author == client.user:
        return


#    messages = [serverStatusResponse, serverStartResponse, serverStopResponse]
#    commands = ["!serverStatus", "!serverStart", "serverStop!"]

    #Strings that the bot uses as a response
    valServerStatusResponse = "Server is TODO VARIABLE"
    valServerStartResponse = "Booting Valheim server."
    valServerStopResponse = "Stopping Valheim Server."
    valPrintIPResponse = "The IP is TODO VARIABLE"

    #Your command checks that come from the user.
    #I envision the bulk of your code going here in these IF blocks. <3 Have fun Evan!
    if message.content == "!ValStatus":
        await message.channel.send(valServerStatusResponse)
        #TODO Add code to print server status, IP and Password.

    if message.content == "!ValStart":
        await message.channel.send(valServerStartResponse)
        #TODO Add code to start server here

    if message.content == "!ValStop":
        await message.channel.send(valServerStopResponse)
        #TODO Add code to stop server here

    if message.content == "!ValIP":
        await message.channel.send(valPrintIPResponse)
        #TODO Add code to print IP here

client.run(TOKEN)
