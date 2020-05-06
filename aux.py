# aux.py
import asyncio
import os
import random

import discord
from discord.utils import get

import consts
import lists
#----------------------------------------------------------------

#Sopas_de_cafe Roles
magician_role = None
mini_boss_role = None
bot_commander_role = None
a_team_role = None
CS_role = None
Dead_by_Dayilight_role = None
Dota2_role = None
League_of_Legends_role = None
Sea_of_Thieves_role = None
Warframe_role = None

#set_roles
def set_roles(roles):
    global magician_role
    global mini_boss_role
    global bot_commander_role
    global a_team_role
    global CS_role
    global Dead_by_Dayilight_role
    global Dota2_role
    global League_of_Legends_role
    global Sea_of_Thieves_role
    global Warframe_role
    
    magician_role = discord.utils.get(roles, name = "Magician")
    mini_boss_role = discord.utils.get(roles, name = "Mini Boss")
    bot_commander_role = discord.utils.get(roles, name = "Bot Commander")
    a_team_role = discord.utils.get(roles, name = "A-Team")
    CS_role = discord.utils.get(roles, name = "CS")
    Dead_by_Dayilight_role = discord.utils.get(roles, name = "Dead by Daylight")
    Dota2_role = discord.utils.get(roles, name = "Dota2")
    League_of_Legends_role = discord.utils.get(roles, name = "LoL")
    Sea_of_Thieves_role = discord.utils.get(roles, name = "Aaaargh")
    Warframe_role = discord.utils.get(roles, name = "Warframe")
    
    return None
#----------------------------------------------------------------

#give_roles
async def give_roles(member):
    try:
        if member.id in consts.Mini_Boss:
            await member.add_roles(mini_boss_role)
            await member.add_roles(bot_commander_role)
            await member.add_roles(a_team_role)
        if member.id in consts.Magician:
            await member.add_roles(magician_role)
        if member.id in consts.CS:
            await member.add_roles(CS_role)
        if member.id in consts.Dead_by_Daylight:
            await member.add_roles(Dead_by_Dayilight_role)
        if member.id in consts.Dota2:
            await member.add_roles(Dota2_role)
        if member.id in consts.League_of_Legends:
            await member.add_roles(League_of_Legends_role)
        if member.id in consts.Sea_of_Thieves:
            await member.add_roles(Sea_of_Thieves_role)
        if member.id in consts.Warframe:
            await member.add_roles(Warframe_role)
    except Exception as e:
        print(f'❗❗❗ERROR: Failed to add roles to user: {member.name} due to:\n{e}\n--------------------')
    return None
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
    elif ((name + ".mp3") in lists.sounds):
        return ("audio//Sounds//" + name + ".mp3")
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
    guild = ctx.guild
    if (auth_id in consts.privileged_id_list):
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune"):
                members.remove(m)
    else:
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune" or m.id in consts.privileged_id_list):
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
    return None
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
