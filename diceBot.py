# diceBot v0.4.py

#?--- Imports ---
from os import getenv
from dotenv import load_dotenv
from discord import Client, Intents 
from diceBot_Functions import diceFunction

#?--- Intents ---
intents = Intents.default() 
intents.members = True 

#?--- Imports the data from .env's ---
load_dotenv()
DISCORD_TOKEN = getenv('DISCORD_TOKEN') 

#?--- Variables ---
commandPrefix = "!"

#?--- Init' Client ---
client = Client(intents=intents)

#?--- Events ---
#* on_ready() event
@client.event
async def on_ready():
    print(f"{client.user.name} has connected to the following servers:\n") 
    for guild in client.guilds:
        print(f"Name: {guild.name}, ID: {guild.id}")

#* on_message() event
@client.event
async def on_message(message):

    #* Stops the bot responding to it's self
    if message.author == client.user:
        return

    #* Dice Function
    elif message.content.lower().startswith(commandPrefix + "dice"):
        await diceFunction(message)

#?--- Run Client ---
client.run(DISCORD_TOKEN)
