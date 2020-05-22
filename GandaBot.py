 # GandaBot.py
import asyncio
import os

import discord
from discord.ext import commands
from discord.utils import get

import aux
import lists
#----------------------------------------------------------------

bot = commands.Bot(command_prefix='?', case_insensitive=True, description='Ganda bot mano!')

#----------------------------- MAIN -----------------------------
def main():
    TOKEN = os.environ['DISCORD_TOKEN']
    bot.run(TOKEN)
#----------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#/////////////////////// BOT STARTED EVENT //////////////////////
#////////////////////////////////////////////////////////////////
#on_ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    servers = []
    for guild in bot.guilds:
        id = guild.id
        servers.append(guild.name)
        lists.queues[id] = []
        lists.init_server_members(guild)
        lists.init_ytdl_options(id)
    lists.init_sound_lists()
    print(f'connected to {len(servers)} guilds: {servers}')
    print('------')
    return


#////////////////////////////////////////////////////////////////
#/////////////////////////// COMMANDS ///////////////////////////
#////////////////////////////////////////////////////////////////
#error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        message = "Unfortunately Ganda bot doesn't have that feature yet :(. Use '?help' to check our existing features!"
        await ctx.send(message)
        return
    raise error


#----------------------------- FLIP -----------------------------
#flip
@bot.command(name='flip', help='Heads or tails? Flip a coin.')
async def flip(ctx):
    res = aux.coin_flip()
    await ctx.send(res)
    print(f'Member {ctx.author.name} flipped a coin in server {ctx.guild.name}')
    return


#-------------------------- HIGHLANDER --------------------------
#highlander
@bot.command(name='highlander', help='⛔ Kick every member from its current voice channel except for one chosen at random.')
async def highlander(ctx):
    fileName = aux.pick_file("highlander")
    VictoryFileName = aux.pick_file("highlanderv")
    ch = ctx.author.voice.channel
    sv = ctx.guild
    await aux.play_file(fileName, ch, sv)
    print(f'Member {ctx.author.name} started Highlander in server {sv.name}')
    await aux.roulette(bot, ctx, 2)
    await aux.play_file(VictoryFileName, ch, sv)
    return


#------------------------ INIT / DESTROY ------------------------
#init
@bot.command(name='init', help='Join your current voice channel and stay there.')
async def init(ctx):
    await ctx.message.delete(delay=1)
    ch = ctx.author.voice.channel
    sv = ctx.guild
    voice = ctx.voice_client
    if (voice and voice.is_connected()):
        await voice.move_to(ch)
        print(f'Bot moved to {ch.name} in server {sv.name}')
    else:
        voice = await ch.connect()
        print(f'Bot connected to {ch.name} in server {sv.name}')
    return

#destroy
@bot.command(name='destroy', help='Disconnect from its current voice channel.')
async def destroy(ctx):
    await ctx.message.delete(delay=1)
    sv = ctx.guild
    voice = ctx.voice_client
    if (voice and voice.is_connected()):
        ch = voice.channel
        await stop(ctx)
        await voice.disconnect()
        voice = None
        print(f'Bot disconnected from {ch.name} in server {sv.name}')
    else:
        print(f'Bot was told to disconnect but was not connected to any channel in server {sv.name}')
    return


#------------------------- MUTE / UNMUTE ------------------------
#mute
@bot.command(name='mute', help='Keep mentioned members muted (@user to mention)')
async def mute(ctx, arg):
    mentioned = ctx.message.mentions
    if (not mentioned):
        message = "You have to mention the user you want to mute (eg. \"?mute @user\")"
        await ctx.send(message)
        return
    else:
        author = ctx.author
        sv = ctx.guild
        for target in mentioned:
            if (author.top_role > target.top_role):
                lists.muted.append(target.id)
                await target.edit(mute=True)
                print(f'Bot is now keeping {target.name} muted in server {sv.name}')
            else:
                name = target.nick
                if (name is None):
                    name = target.name
                message = "⛔ You don't have permission to mute " + name + " ⛔"
                await aux.permission_denied(ctx, message)
    return

#unmute
@bot.command(name='unmute', help='Stops keeping the mentioned members muted (@user to mention). Admins can use "?unmute all" to unmute everyone being kept muted')
async def unmute(ctx, arg):
    mentioned = ctx.message.mentions
    author = ctx.author
    if (arg == "all" and author.guild_permissions.administrator):
        while lists.muted:
            id = lists.muted.pop()
            user = get(bot.get_all_members(), id=id)
            await user.edit(mute=False)
        print(f'Bot is no longer keeping anyone muted in server {ctx.guild.name}')
    elif (mentioned):
        sv = ctx.guild
        for target in mentioned:
            if (author.top_role > target.top_role):
                lists.muted.remove(target.id)
                await target.edit(mute=False)
                print(f'Bot is no longer keeping {target.name} muted in server {sv.name}')
            else:
                name = target.nick
                if (name is None):
                    name = target.name
                message = "⛔ You don't have permission to unmute " + name + " ⛔"
                await aux.permission_denied(ctx, message)
    else:
        message = "You have to mention the user you want to unmute (eg. \"?unmute @user\")"
        await ctx.send(message)
    return


#----------------------- RUSSIAN ROULETTE -----------------------
#rroulette
@bot.command(name='rroulette', aliases = ['russian roulette', 'rroulete', 'rroullete'], help='⛔ Kick one random member from its current voice channel.')
async def rroulette(ctx):
    fileName = aux.pick_file("rroulette")
    ch = ctx.author.voice.channel
    sv = ctx.guild
    await aux.play_file(fileName, ch, sv)
    print(f'Member {ctx.author.name} started Russian Roulette in server {sv.name}')
    await aux.roulette(bot, ctx, 1)
    return


#--------------------------- SHUFFLE ----------------------------
#shuffle
@bot.command(name='shuffle', aliases = ['Shuff'], help='Send every member on your current voice channel to random voice channels')
async def shuffle(ctx):
    authorVcState = ctx.author.voice
    voiceState = ctx.voice_client
    sv = ctx.guild
    if (not ctx.author.guild_permissions.move_members):
        message = "⛔ You don't have permission to shuffle ⛔"
        await aux.permission_denied(ctx, message)
    elif (authorVcState is None):
        message = "You have to be connected to a voice channel"
        await ctx.send(message)
        return
    else:
        await aux.shuffle_members(sv, authorVcState.channel)


#---------------------------- SOUNDS ----------------------------
#play
@bot.command(name='play', help='Play a sound. Follow by the sound name to play a specific sound, a youtube URL to play that audio, "list" to get the list of sounds, "random" to play a random sound or "ariana" to play a random Ariana Grande song')
async def play(ctx, arg):
    await ctx.message.delete(delay=1)
    authorVcState = ctx.author.voice
    sv = ctx.guild
    if (authorVcState is None):
        message = "You must be connected to a voice channel to use the play command"
        await ctx.send(message)
        return
    elif (arg == "random"):
        fileName = aux.pick_file("random")
    elif (arg == "ariana"):
        fileName = aux.pick_file("ariana")
    #elif (arg == "list"):
        #send sound list
    elif (arg.startswith("https://www.youtube.com/")):
        fileName = aux.pick_yt_file(sv.id, arg)
        if (fileName is None):
            message = "Bad url. Please provide a youtube.com url"
            await ctx.send(message)
            return
    else:
        fileName = aux.pick_file(arg)
        if (fileName is None):
            message = "Ganda bot can't play \"" + arg + "\""
            await ctx.send(message)
            return
    ch = authorVcState.channel
    await aux.play_file(fileName, ch, sv)
    return

#pause
@bot.command(name='pause', help='Pause the current sound')
async def pause(ctx):
    await ctx.message.delete(delay=1)
    voice = ctx.voice_client
    if (voice.is_playing()):
        voice.pause()
    else:
        print(f'Bot tried to pause but was not playing in server {ctx.guild.name}')
    return

#resume
@bot.command(name='resume', help='Resume the current sound')
async def resume(ctx):
    await ctx.message.delete(delay=1)
    voice = ctx.voice_client
    if (voice.is_paused()):
        voice.resume()
    else:
        print(f'Bot tried to resume the sound but was not playing in server {ctx.guild.name}')
    return

#stop
@bot.command(name='stop', help='Stop playing the current sound')
async def stop(ctx):
    await ctx.message.delete(delay=1)
    voice = ctx.voice_client
    if (voice.is_playing() or voice.is_paused()):
        lists.queues[ctx.guild.id] = []
        voice.stop()
    else:
        print('Bot tried to stop playing but nothing was playing before in server {ctx.guild.name}')
    return

#skip
@bot.command(name='skip', help='Skip the current sound')
async def skip(ctx):
    await ctx.message.delete(delay=1)
    voice = ctx.voice_client
    if (voice.is_playing() or voice.is_paused()):
        voice.stop()
    else:
        print('Bot tried to skip the sound but nothing was playing before in server {ctx.guild.name}')
    return
#----------------------------------------------------------------


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
#----------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// VOICE CHANNEL ////////////////////////
#////////////////////////////////////////////////////////////////
#on_voice_state_update
@bot.event
async def on_voice_state_update(member, before, after):
    #Check if state update's origin is a bot
    if (member.bot):
        return
    before_vc = before.channel
    after_vc = after.channel
    id = member.id
    sv = member.guild
    serverId = sv.id
    voice = sv.voice_client
    #Keep muting members in the keep_muted list
    if (member.id in lists.muted and not after.mute):
        await member.edit(mute=True)
        print(f'Bot muted member {member.name} in server {sv.name}')
    #Play sound if user deafens himself
    if (after.self_deaf and not before.self_deaf):
        fileName = aux.pick_file("selfDeaf")
        await aux.play_file(fileName, after_vc, sv)
        print(f'Member {member.name} deafened himself in server {sv.name}')
    #Play sound if user undeafens himself
    if (before.self_deaf and not after.self_deaf):
        fileName = aux.pick_file("selfUndeaf")
        await aux.play_file(fileName, after_vc, sv)
        print(f'Member {member.name} undeafened himself in server {sv.name}')
    #Play sound if user leaves voice channel
    if ((before_vc != after_vc) and (after_vc is None)):
        fileName = aux.pick_file("leave")
        await aux.play_file(fileName, before_vc, sv)
        print(f'Member {member.name} left voice channel {before_vc.name} in server {sv.name}')
    #Play join sound if member has one
    if ((after_vc is not None) and (before_vc != after_vc)):
        fileName = aux.pick_sound_join(serverId, id)
        if (fileName is not None):
            await aux.play_file(fileName, after_vc, sv)
            print(f'Member {member.name} joined voice channel {after_vc.name} in server {sv.name}')
    #Disconnect bot if he's the only member on the channel
    if (voice is not None and voice.channel == before_vc and aux.is_bot_alone(before_vc)):
        lists.queues[serverId] = []
        await voice.disconnect()
        voice = None
        print(f'Bot disconnected from {before_vc.name} in guild {sv.name} because it was the only member connected')
    return
#----------------------------------------------------------------


#////////////////////////////////////////////////////////////////
#///////////////////////// MEMEBER JOIN /////////////////////////
#////////////////////////////////////////////////////////////////
#on_member_join
@bot.event
async def on_member_join(member):
    print(f'Member {member.name} joined server {member.guild.name}')
    serverId = member.guild.id
    await aux.give_roles(serverId, member)
    await aux.change_nickname(serverId, member)
    return
#----------------------------------------------------------------


if __name__ == "__main__":
    main()
