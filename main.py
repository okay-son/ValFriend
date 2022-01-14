import discord
import requests
import json
import random

no_valorant = ["valorant", "val", "Val", "VAL", "VALORANT", "Valorant"]

val_response = [
    "hey hey hey... you\'re playing valorant again? loser lmao just stop",
    "stop playing valorant",
    "valorant is so bad for you, just stop",
    "you're gonna stay tinfoil 1, just stop",
    "you wish you were radiant",
    "stop being such a loser",
    "get off of valorant smh",
    "valarante child game.... look to cartoon grapfix to make kid player happy like children show.. valarante cartoon world with rainbow unlike counter strike with dark corridorr and raelistic gun.. valarante like playhouse. valarant playor run from csgo fear of dark world and realism",
    "You're fantastic. Just need to work on communication, aim, map awareness, crosshair placement, economy management, pistol aim, awp flicks, grenade spots, smoke spots, pop flashes, positioning, bomb plant positions, retake ability, bunny hopping, spray control and getting a kill.",
    "valorant is just gonna trigger you more cuz you suck, just stop"]

@client.event
async def on_ready():
    print('we have logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if any(word in msg for word in no_valorant):
        await message.channel.send(random.choice(val_response))
