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

#getNickname
def getNickname(ID):
    if (ID == consts.Daniel_id):
        return "Maverick 🐧"
    elif (ID == consts.Frangueiro_id):
        return "ZeFrangueiro 🌌"
    elif (ID == consts.Henrique_id):
        return "M4ST3R 🌊"
    elif (ID == consts.Joao_id):
        return "Mr.WOLF 🐺"
    elif (ID == consts.Touret_id):
        return "RKO 💩"
    elif (ID == consts.Valdemar_id):
        return "Like Always 🔥"
    elif (ID == consts.Verde_id):
        return "MrVerdinsky 💚"
    elif (ID == consts.Wilson_id):
        return "Wilson 🌈"
    elif (ID == consts.Yusuke_id):
        return "Yusukeeee 🎸"
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


#getMemberFromCtxName
def getMemberFromCtxName(ctx, arg):
    members = ctx.guild.members
    for m in members:
        if arg in m.name:
            return m
    return None
#----------------------------------------------------------------


#change_nickname
async def change_nickname(member):
    nickname = getNickname(member.id)
    if (nickname is not None):
        try:
            await member.edit(nick = nickname)
        except Exception as e:
            print(f'❗❗❗ERROR: Failed to change nickname on user: {member.name} due to:\n{e}\n--------------------')
    return None
#----------------------------------------------------------------

#pickFile
def pickFile(name):
    if (name == 'ariana'):
        rand = random.choice(lists.ariana)
        fileName = "audio//Ariana Grande//" + rand
        return fileName
    elif (name == 'denied'):
        rand = random.choice(lists.permissionDenied)
        fileName = "audio//PermissionDenied//" + rand
        return fileName
    elif (name =='highlander'):
        rand = random.choice(lists.highlander)
        fileName = "audio//Highlander//Play//" + rand
        return fileName
    elif (name == 'highlanderv'):
        rand = random.choice(lists.highlanderVictory)
        fileName = "audio//Highlander//Victory//" + rand
        return fileName
    elif (name == 'jajao' or name == 'rroulette'):
        return consts.jajao
    elif (name == 'random'):
        rand = random.choice(lists.sounds)
        fileName = "audio//Sounds//" + rand
        return fileName
    elif ((name + ".mp3") in lists.sounds):
        return ("audio//Sounds//" + name + ".mp3")
    return None
#----------------------------------------------------------------

#picSoundJoin
def pickSoundJoin(id):
    #DANIEL
    if (id == consts.Daniel_id):
        rand = random.choice(lists.daniel)
        fileName = "audio//Join//Daniel//" + rand
        return fileName
    #DAVID
    elif (id == consts.David_id):
        rand = random.choice(lists.david)
        fileName = "audio//Join//David//" + rand
        return fileName
    #HENRIQUE
    elif (id == consts.Henrique_id):
        rand = random.choice(lists.henrique)
        fileName = "audio//Join//Henrique//" + rand
        return fileName
    #JOAO
    elif (id == consts.Joao_id):
        rand = random.choice(lists.joao)
        fileName = "audio//Join//Joao//" + rand
        return fileName
    #KNIGHT
    elif (id == consts.Knight_id):
        rand = random.choice(lists.knight)
        fileName = "audio//Join//Knight//" + rand
        return fileName
    #POSEIDON
    elif (id == consts.Poseidon_id):
        rand = random.choice(lists.poseidon)
        fileName = "audio//Join//Poseidon//" + rand
        return fileName
    #RAFA
    elif (id == consts.Rafa_id):
        rand = random.randrange(0, len(lists.rafa))
        fileName = "audio//Join//Rafa//" + rand
        return fileName
    #TOURET
    elif (id == consts.Touret_id):
        rand = random.choice(lists.touret)
        fileName = "audio//Join//Touret//" + rand
        return fileName
    #VALDEMAR
    elif (id == consts.Valdemar_id):
        rand = random.choice(lists.valdemar)
        fileName = "audio//Join//Valdemar//" + rand
        return fileName
    #VERDE
    elif (id == consts.Verde_id):
        rand = random.choice(lists.verde)
        fileName = "audio//Join//Verde//" + rand
        return fileName
    #WILSON
    elif (id == consts.Wilson_id):
        rand = random.choice(lists.wilson)
        fileName = "audio//Join//Wilson//" + rand
        return fileName
    #YUSUKE
    elif (id == consts.Yusuke_id):
        rand = random.choice(lists.yusuke)
        fileName = "audio//Join//Yusuke//" + rand
        return fileName
    #ZE
    elif (id == consts.Ze_id):
        rand = random.choice(lists.ze)
        fileName = "audio//Join//Ze//" + rand
        return fileName
    return None
#----------------------------------------------------------------

#pickVoiceUpdateSound
def pickVoiceUpdateSound(name):
    #DANIEL
    if (name == 'leave'):
        rand = random.choice(lists.leave)
        fileName = "audio//VoiceUpdate//Leave//" + rand
        return fileName
    elif (name == 'selfDeaf'):
        rand = random.choice(lists.selfDeaf)
        fileName = "audio//VoiceUpdate//Self//Deafen//" + rand
        return fileName
    elif(name == 'selfUndeaf'):
        rand = random.choice(lists.selfUndeaf)
        fileName = "audio//VoiceUpdate//Self//Undeafen//" + rand
        return fileName
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
