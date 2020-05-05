# GandaBot.py
import os
import sys
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import random

import lists
from aux import *

TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='?', description='Ganda bot mano!')

voice = None


#////////////////////////////////////////////////////////////////
#/////////////////////// BOT STARTED EVENT //////////////////////
#////////////////////////////////////////////////////////////////
#on_ready
@bot.event
async def on_ready():
    set_roles(bot.get_guild(consts.sopas_de_cafe_id).roles)
    print(f'Logged in as {bot.user}')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    servers = []
    for guild in bot.guilds:
        servers.append(guild.name)
    lists.initLists()
    print(f'connected to {len(servers)} guilds: {servers}')
    print('------')
    return


#////////////////////////////////////////////////////////////////
#/////////////////////////// COMMANDS ///////////////////////////
#////////////////////////////////////////////////////////////////

#---------------------------- INIT ----------------------------
#init
@bot.command(name='init', help='Join your current voice channel and stay there.')
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
    return
#-----------------------------------------------------------------------------------


#-------------------------- DESTROY ---------------------------
#destroy
@bot.command(name='destroy', help='Disconnect from its current voice channel.')
async def destroy(ctx):
    global voice
    channel = ctx.author.voice.channel
    if (voice and voice.is_connected()):
        await voice.disconnect()
        voice = None
        print(f'Bot disconnected from {channel} in guild {voice.guild}')
    else:
        print(f'Bot was told to disconnect but was not connected to any channel')
    return
#-----------------------------------------------------------------------------------


#--------------------------- SOUNDS ---------------------------
#play
@bot.command(name='play', help='Play a sound. Follow by the sound name to play a specific sound, "list" to get the list of sounds, "random" to play a random sound or "ariana" to play a random Ariana Grande song')
async def play(ctx, arg):
    if (arg == "random"):
        fileName = pickFile("random")
    elif (arg == "ariana"):
        fileName = pickFile("ariana")
    #elif (arg == "list"):
        #send sound list
    else:
        fileName = pickFile(arg)
        if (fileName is None):
            #play youtube
            return
    await play_file(fileName, ctx.author.voice.channel, ctx.guild)
    return

#pause
@bot.command(name='pause', help='Pause the current sound')
async def pause(ctx):
    global voice
    if (voice.is_playing()):
        voice.pause()
    else:
        print("Bot tried to pause but was not playing")
    return

#resume
@bot.command(name='resume', help='Resume the current sound')
async def resume(ctx):
    global voice
    if (voice.is_paused()):
        voice.resume()
    else:
        print("Bot tried to resume the sound but was not playing")
    return

#stop
@bot.command(name='stop', help='Stop playing the current sound')
async def stop(ctx):
    global voice
    if (voice.is_playing() or voice.is_paused()):
        voice.stop()
    else:
        print("Bot tried to stop playing but nothing was playing before")
    return
#-----------------------------------------------------------------------------------


#---------------------------- MUTE ----------------------------
#mute
@bot.command(name='mute', help='Keep a member muted')
async def mute(ctx, arg):
    target = getMemberFromCtxName(ctx, arg)
    if (ctx.author.top_role > target.top_role):
        lists.addMuted(target.id)
        await target.edit(mute=True)
        print(f'Bot is now keeping {target.name} muted')
        return
    else:
        message = "⛔ You don't have permission to mute " + target.nick + " ⛔"
        await ctx.send(message)
        print(f'{ctx.author.name} does not have permission to mute {target.name}')
        return

#--------------------------- UNMUTE ---------------------------
#unmute
@bot.command(name='unmute', help='Stops keeping a member muted')
async def unmute(ctx, arg):
    target = getMemberFromCtxName(ctx, arg)
    if (arg == "all" and ctx.author.guild_permissions.administrator):
        for i in lists.muted:
            lists.removeMuted(i)
            user = get(bot.get_all_members(), id=i)
            await user.edit(mute=False)
        print("Bot is no longer keeping anyone muted")
    elif (target is None):
        return
    elif (ctx.author.top_role > target.top_role):
        lists.removeMuted(target.id)
        await target.edit(mute=False)
        print(f'Bot is no longer keeping {target.name} muted')
    else:
        message = "⛔ You don't have permission to unmute " + target.nick + " ⛔"
        await ctx.send(message)
        print(f'{ctx.author.name} does not have permission to unmute {target.name}')
    return
#-----------------------------------------------------------------------------------


#---------------------- RUSSIAN ROULETTE ----------------------
#rroulette
@bot.command(name='rroulette', help='⛔ Kick one random member from its current voice channel.')
async def rroulette(ctx):
    fileName = pickFile("rroulette")
    await play_file(fileName, ctx.author.voice.channel, ctx.guild)
    await roulette(bot, ctx, 1)
    return

#------------------------- HIGHLANDER -------------------------
#highlander
@bot.command(name='highlander', help='⛔ Kick every member from its current voice channel except for one chosen at random.')
async def highlander(ctx):
    fileName = pickFile("highlander")
    ch = ctx.author.voice.channel
    sv = ctx.guild
    await play_file(fileName, ch, sv)
    await roulette(bot, ctx, 2)
    await play_file(highlander_victory, ch, sv)
    return
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
    global voice
    #Check if state update's origin is a bot
    if (member.bot):
        return
    before_vc = before.channel
    after_vc = after.channel
    id = member.id
    #Keep muting members in the keep_muted list
    if (member.id in lists.muted and not after.mute):
        await member.edit(mute=True)
    #Play sound if user deafens himself
    if (after.self_deaf and not before.self_deaf):
        await play_file(consts.self_deaf, after_vc, after_vc.guild)
    #Play sound if user undeafens himself
    if (before.self_deaf and not after.self_deaf):
        await play_file(consts.self_undeaf, after_vc, after_vc.guild)
    #Play sound if user leaves voice channel
    if ((before_vc != after_vc) and (after_vc is None)):
        await play_file(consts.leave, before_vc, before_vc.guild)
    #Play join sound if member has one
    if ((after_vc is not None) and (before_vc != after_vc)):
        fileName = pickSoundJoin(id)
        if (fileName is not None):
            await play_file(fileName, after_vc, after_vc.guild)
    #Disconnect bot if he's the only member on the channel
    if (voice is not None and voice.channel == before_vc and isBotAlone(before_vc)):
        await voice.disconnect()
        voice = None
        print(f'Bot disconnected from {before_vc.name} in guild {voice.guild.name} because it was the only member connected')
    return
#-----------------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// MEMEBER JOIN /////////////////////////
#////////////////////////////////////////////////////////////////
#on_member_join
@bot.event
async def on_member_join(member):
    await give_roles(member)
    await change_nickname(member)
    return
#-----------------------------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#////////////////////////// PLAY FILE ///////////////////////////
#////////////////////////////////////////////////////////////////
#play_sound
async def play_file(fileName, ch, server):
    global voice
    inited = 1
    if (voice == None):
        inited = 0
        voice = get(bot.voice_clients, guild=server)
        voice = await ch.connect()
    voice.play(discord.FFmpegPCMAudio(fileName,executable='ffmpeg'))
    while(voice.is_playing()):
        await asyncio.sleep(1)
    if (inited == 0 and not (voice.is_playing() or voice.is_paused())):
        await voice.disconnect()
        voice = None
    return




bot.run(TOKEN)
