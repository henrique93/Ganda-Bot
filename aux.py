# aux.py
import asyncio
import random
import os

import discord
import youtube_dl

import consts
import lists
#----------------------------------------------------------------

#change_nickname
async def change_nickname(serverId, member):
    id = member.id
    memberInfo = lists.serverMembers[serverId]
    if (id in memberInfo):
        nickname = memberInfo[id][1]
        if (nickname is None):
            return
        try:
            await member.edit(nick = nickname)
            print(f'Bot changed nickname of member {member.name} in server {member.guild.name}')
        except Exception as e:
            print(f'❗❗❗ERROR: Failed to change nickname on user: {member.name} due to:\n{e}\n--------------------')
    return None
#----------------------------------------------------------------

#check_queue
async def check_queue(serverId, voice):
    if (lists.queues[serverId]):
        sound = lists.queues[serverId].pop(0)
        voice.play(sound)
        while(voice.is_playing() or voice.is_paused()):
            await asyncio.sleep(1)
        await check_queue(serverId, voice)
    else:
        path = consts.youtubePath + str(serverId)
        if (os.path.isdir(path)):
            files = os.listdir(path)
            for file in os.listdir(path):
                os.remove(path+"/"+file)
#----------------------------------------------------------------

#coin_flip
def coin_flip():
    rand = random.randint(0,1)
    if (rand):
        return "Heads!"
    else:
        return "Tails!"
#----------------------------------------------------------------

#give_roles
async def give_roles(serverId, member):
    id = member.id
    memberInfo = lists.serverMembers[serverId]
    roles = memberInfo[id][0]
    for r in roles:
        try:
            await member.add_roles(r)
            print(f'Bot gave roles to {member.name} in server {member.guild.name}')
        except Exception as e:
            print(f'❗❗❗ERROR: Failed to add role {r} to user: {member.name} due to:\n{e}\n--------------------')
    return
#----------------------------------------------------------------

#is_bot_alone
def is_bot_alone(ch):
    bots = 0
    num_members = len(ch.members)
    for m in ch.members:
        if (m.bot):
            bots += 1
    if ((num_members == 1) or (num_members == bots)):
        return True
    return False
#----------------------------------------------------------------

#permission_denied
async def permission_denied(ctx, message):
    sv = ctx.guild
    voiceState = lists.voiceStates[sv.id]
    await ctx.send(message)
    if (voiceState is not None):
        fileName = pick_file("denied")
        print(fileName)
        await play_file(fileName, ctx.author.voice.channel, sv)
    print(f'{ctx.author.name} does not have permission to perform this action in server {sv.name}')
    return
#----------------------------------------------------------------

#pick_file
def pick_file(name):
    if (name in lists.playDictionary):
        rand = random.choice(lists.playDictionary[name][1])
        fileName = lists.playDictionary[name][0] + rand
        return fileName
    elif (name == 'jajao' or name == 'rroulette'):
        return consts.jajao
    elif ((name + ".mp3") in lists.playDictionary["random"][1]):
        return (lists.playDictionary["random"][0] + name + ".mp3")
    return None
#----------------------------------------------------------------

#pick_sound_join
def pick_sound_join(serverId, id):
    memberInfo = lists.serverMembers[serverId]
    if (memberInfo[id][2]):
        path = consts.joinSoundPath + str(id) + "/"
        rand = random.choice(memberInfo[id][2])
        fileName = path + rand
        return fileName
    return None
#----------------------------------------------------------------

#pick_yt_file
def pick_yt_file(serverId, url):
    with youtube_dl.YoutubeDL(lists.ytdl_options[serverId]) as ydl:
        try:
            ydl.download([url])
        except youtube_dl.utils.DownloadError as e:
            print(f'❗❗❗ERROR: failed to download song from {url} due to:\n{e}\n\n--------------------')
            return None
    path = consts.youtubePath + str(serverId) + "/"
    for file in os.listdir(path):
        if file.endswith(".mp3"):
            path += file
            return path
#----------------------------------------------------------------

#play_file
async def play_file(fileName, authorVc, sv):
    serverId = sv.id
    voice = lists.voiceStates[serverId]
    if (authorVc is None):
        print('Member was not connected to any voice channel')
        return
    elif (voice is None):
        voice = await authorVc.connect()
        print(f'Bot connected to voice channel {authorVc.name} in server {sv.name}')
        lists.voiceStates[serverId] = voice
    elif (voice.channel != authorVc and not (voice.is_playing() or voice.is_paused())):
        await voice.move_to(authorVc)
        print(f'Bot moved to voice channel {authorVc.name} in server {sv.name}')
    elif (voice.is_playing() or voice.is_paused()):
        sound = discord.FFmpegPCMAudio(fileName,executable='ffmpeg')
        lists.queues[serverId].append(sound)
        print(f'Sound {fileName} has been queued in server {sv.name}')
        return
    sound = discord.FFmpegPCMAudio(fileName,executable='ffmpeg')
    try:
        voice.play(sound)
    except discord.errors.ClientException as e:
        print(f'❗❗❗ERROR: Failed to play sound in server {sv.name} due to: voice connection issues:\n{e}\n--------------------')
        lists.voiceStates[serverId] = None
        await play_file(fileName, authorVc, sv)
    except Exception as e:
        print(f'❗❗❗ERROR: Failed to play sound in server {sv.name} due to:\n{e}\n--------------------')
    print(f'Bot is playing {fileName} in server {sv.name}')
    while(voice.is_playing() or voice.is_paused()):
        await asyncio.sleep(1)
    await check_queue(serverId, voice)
#----------------------------------------------------------------

#roulette
async def roulette(bot, ctx, type):
    auth_id = ctx.author.id
    voice_ch = ctx.author.voice.channel
    members = voice_ch.members
    if (ctx.author.guild_permissions.kick_members):
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune"):
                members.remove(m)
    else:
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune" or m.guild_permissions.kick_members):
                members.remove(m)
    if (type == 1):
        end_message = "Rip "
        num_kicks = 1
    else:
        end_message = "It as been declared by highlander, that the one true fagget is: "
        num_kicks = len(members) - 1
    print(f'Users playing: {members}')
    for i in range(num_kicks):
        to_kick = random.choice(members)
        try:
            invite = await ctx.channel.create_invite(max_age = 3600, max_uses = 1)
            invite_msg = "You lost. Join us again bitch\n Click the link to join:" + invite.url
            members.remove(to_kick)
            dm_channel = await to_kick.create_dm()
            dm_message = await dm_channel.send(content=invite_msg)
            await to_kick.kick()
        except discord.Forbidden:
            await to_kick.move_to(None)
            await dm_message.delete()
            print(f'❗❗❗ERROR: failed to kick user {to_kick.name} due to lack of permissions')
        except Exception as e:
            print(f'❗❗❗ERROR: failed to kick user {to_kick.name} due to:\n{e}\n\n--------------------')
    if (type == 1):
        end_message += to_kick.name
    else:
        end_message += members[0].name
    await ctx.send(end_message)
    return
#----------------------------------------------------------------

#shuffle_members
async def shuffle_members(sv, ch):
    channelList = sv.voice_channels
    for m in ch.members:
        if (m.bot):
            continue
        randCh = random.choice(channelList)
        try:
            await m.move_to(randCh)
            print(f'Moved member {m.name} to voice channel {randCh.name} in server {sv.name}')
        except Exception as e:
            print(f'❗❗❗ERROR: failed to move user {m.name} to channel {randCh.name} due to:\n{e}\n\n--------------------')
#----------------------------------------------------------------
