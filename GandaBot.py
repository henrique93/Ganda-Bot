# GandaBot.py
import os
import sys
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random

from aux import *

TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='?')

voice = None


#////////////////////////////////////////////////////////////////
#/////////////////////// BOT STARTED EVENT //////////////////////
#////////////////////////////////////////////////////////////////
#on_ready
@bot.event
async def on_ready():
    set_roles(bot.get_guild(sopas_de_cafe_id).roles)
    print(f'Logged in as {bot.user}')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    servers = []
    for guild in bot.guilds:
        servers.append(guild.name)
    print(f'connected to {len(servers)} guilds: {servers}')
    print('------')


#////////////////////////////////////////////////////////////////
#/////////////////////////// COMMANDS ///////////////////////////
#////////////////////////////////////////////////////////////////

#---------------------------- INIT ----------------------------
#init
@bot.command(name='init', help='Makes the bot join your current voice channel and stay there.')
async def init(ctx):
    global voice
    channel = ctx.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if (voice and voice.is_connected()):
        await voice.move_to(channel)
        print(f'Bot moved to {channel} in guild {voice.guild}')
    else:
        voice = await channel.connect()
        print(f'Bot connected to {channel} in guild {voice.guild}')
#-----------------------------------------------------------------------------------


#-------------------------- DESTROY ---------------------------
#destroy
@bot.command(name='destroy', help='Makes the bot disconnect from its current voice channel.')
async def destroy(ctx):
    global voice
    channel = ctx.author.voice.channel
    if (voice and voice.is_connected()):
        await voice.disconnect()
        voice = None
        print(f'Bot disconnected from {channel} in guild {voice.guild}')
    else:
        print(f'Bot was told to disconnect but was not connected to any channel')
#-----------------------------------------------------------------------------------


#--------------------------- SOUNDS ---------------------------
#play
@bot.command(name='play', help='Makes the bot play a sound. Follow by the sound name to play a pecific sound, "random" to play a random sound or "ariana" to play a random Ariana Grande song')
async def play(ctx, arg):
    global voice
    if (arg == "random"):
        fileName = pickFile("random")
    elif (arg == "ariana"):
        fileName = pickFile("ariana")
    else:
        fileName = pickFile(arg)
        if (fileName is None):
            #play youtube
    #play_sound(fileName, ctx.author.voice.channel)
    inited = 1
    if (voice == None):
        inited = 0
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice = await ctx.author.voice.channel.connect()
    voice.play(discord.FFmpegPCMAudio(fileName,executable='ffmpeg'))
    while(voice.is_playing()):
        await asyncio.sleep(1)
    if (inited == 0 and not voice.is_playing()):
        await voice.disconnect()
        voice = None

#pause
@bot.command(name='pause', help='Makes the bot pause the current sound')
async def pause(ctx):
    global voice
    if (voice.is_playing()):
        voice.pause()
    else:
        print("Bot tried to pause but was not playing")

#resume
@bot.command(name='resume', help='Makes the bot resume the current sound')
async def resume(ctx):
    global voice
    if (voice.is_paused()):
        voice.resume()
    else:
        print("Bot tried to resume the sound but was not playing")

#stop
@bot.command(name='stop', help='Makes the bot stop playing the current sound')
async def stop(ctx):
    global voice
    if (voice.is_playing() or voice.is_paused()):
        voice.stop()
    else:
        print("Bot tried to stop playing but nothing was playing before")
#-----------------------------------------------------------------------------------


#---------------------- RUSSIAN ROULETTE ----------------------
#rroulette
@bot.command(name='rroulette', help='Makes the bot kick one random member from its current voice channel.⛔')
async def rroulette(ctx):
    await roulette(bot, ctx, 1)
#-----------------------------------------------------------------------------------


#------------------------- HIGHLANDER -------------------------
#highlander
@bot.command(name='highlander', help='Makes the bot kick every member from its current voice channel except for one chosen at random.⛔')
async def highlander(ctx):
    await roulette(bot, ctx, 2)
#-----------------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// MESSAGE EVENT ////////////////////////
#////////////////////////////////////////////////////////////////
#on_message
#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
#    msg = message.content
#    if (msg == "?test"):
#        dm_channel = await message.author.create_dm()
#        await dm_channel.send("ola")
#-----------------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// VOICE CHANNEL ////////////////////////
#////////////////////////////////////////////////////////////////
#on_voice_state_update
@bot.event
async def on_voice_state_update(member, before, after):
    ch = before.channel
    voice = get(bot.voice_clients, guild=member.guild)
    #Disconnect bot if he's the only member on the channel
    if (ch is not None and voice is not None):
        if(voice.channel == ch and len(ch.members) == 1):
            await voice.disconnect()
            print(f'Bot disconnected from {ch} in guild {voice.guild} because it was the only member connected')
#-----------------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// MEMEBER JOIN /////////////////////////
#////////////////////////////////////////////////////////////////
#on_member_join
@bot.event
async def on_member_join(member):
    await give_roles(member)
    await change_nickname(member)
#-----------------------------------------------------------------------------------


#play_sound
async def play_sound(fileName, ch):
    global voice
    inited = 1
    if (voice == None):
        inited = 0
        voice = get(bot.voice_clients, guild=ctx.guild)
        voice = await ch.connect()
    voice.play(discord.FFmpegPCMAudio(fileName,executable='ffmpeg'))
    while(voice.is_playing()):
        await asyncio.sleep(1)
    if (inited == 0 and not voice.is_playing()):
        await voice.disconnect()
        voice = None




bot.run(TOKEN)
