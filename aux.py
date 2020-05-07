# aux.py
import asyncio
import os
import random

import discord
from discord.utils import get

import consts
import lists
#----------------------------------------------------------------

#give_roles
async def give_roles(member):
    id = member.id
    roles = lists.rolesDictionary[id]
    try:
        member.add_roles(roles)
    except Exception as e:
        print(f'❗❗❗ERROR: Failed to add roles to user: {member.name} due to:\n{e}\n--------------------')
    return
#----------------------------------------------------------------

#change_nickname
async def change_nickname(member):
    id = member.id
    if (id in lists.idDictionary):
        nickname = lists.idDictionary[id][1]
        try:
            await member.edit(nick = nickname)
        except Exception as e:
            print(f'❗❗❗ERROR: Failed to change nickname on user: {member.name} due to:\n{e}\n--------------------')
    return None
#----------------------------------------------------------------

#pickFile
def pickFile(name):
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

#picSoundJoin
def pickSoundJoin(id):
    if (id in lists.idDictionary):
        path = lists.idDictionary[id][0]
        rand = random.choice(lists.idDictionary[id][2])
        fileName = path + rand
        return fileName
    return None
#----------------------------------------------------------------

#roulette
async def roulette(bot, ctx, type):
    auth_id = ctx.author.id
    voice_ch = ctx.author.voice.channel
    members = voice_ch.members
    if (auth_id in lists.privilegedList):
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune"):
                members.remove(m)
    else:
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune" or m.id in lists.privilegedList):
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

#isBotAlone
def isBotAlone(ch):
    bots = 0
    num_members = len(ch.members)
    for m in ch.members:
        if (m.bot):
            bots += 1
    if ((num_members == 1) or (num_members == bots)):
        return True
    return False
#----------------------------------------------------------------

#coinFlip
def coinFlip():
    rand = random.randint(0,1)
    if (rand):
        return "Heads!"
    else:
        return "Tails!"
#----------------------------------------------------------------
