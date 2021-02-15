import os
import asyncio

from mutagen.mp3 import MP3
from discord import FFmpegPCMAudio
import discord
from dotenv import load_dotenv
from discord.ext import commands

active = False

file = open("archivo.txt","a") 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_context = True)
async def leave(ctx):
    await ctx.voice_client.disconnect()

#Taunts
@client.command(pass_context = True)
async def t(ctx, number):
    if active:
        await ctx.message.delete() 
        user = ctx.message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            audio = MP3(f"{number}.mp3")
            player = vc.play(FFmpegPCMAudio(f"{number}.mp3"))
            print(audio.info.length)
            await asyncio.sleep(audio.info.length)      
            await ctx.voice_client.disconnect()
    else:
        print("not active!")


@client.command(pass_context = True)
async def pause(ctx):
    global active
    if "wololo" in [y.name.lower() for y in ctx.message.author.roles]:
        await ctx.message.delete() 
        if ctx.message.author.id == 466423837672865793:
            active = False
        print(active) 
        
@client.command(pass_context = True)
async def resume(ctx):
    global active
    if "wololo" in [y.name.lower() for y in ctx.message.author.roles]:
        await ctx.message.delete() 
        if ctx.message.author.id == 466423837672865793:
            active = True
        print(active) 

@client.command(pass_context = True)
async def sos_wololo(ctx):
    if "wololo" in [y.name.lower() for y in ctx.message.author.roles]:
        print("sos wololo :)")
    else:
        print("no sos")

client.run(TOKEN)
