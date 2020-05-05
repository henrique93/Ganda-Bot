# aux.py
import os
import random
import discord
from discord.utils import get
import asyncio



from consts import *
import lists

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
#-----------------------------------------------------------------------------------

#getNickname
def getNickname(ID):
    if (ID == Daniel_id):
        return "Maverick 🐧"
    elif (ID == Frangueiro_id):
        return "ZeFrangueiro 🌌"
    elif (ID == Henrique_id):
        return "M4ST3R 🌊"
    elif (ID == Joao_id):
        return "Mr.WOLF 🐺"
    elif (ID == Touret_id):
        return "RKO 💩"
    elif (ID == Valdemar_id):
        return "Like Always 🔥"
    elif (ID == Verde_id):
        return "MrVerdinsky 💚"
    elif (ID == Wilson_id):
        return "Wilson 🌈"
    elif (ID == Yusuke_id):
        return "Yusukeeee 🎸"
    return None
#-----------------------------------------------------------------------------------

#give_roles
async def give_roles(member):
    try:
        if member.id in Mini_Boss:
            await member.add_roles(mini_boss_role)
            await member.add_roles(bot_commander_role)
            await member.add_roles(a_team_role)
        if member.id in Magician:
            await member.add_roles(magician_role)
        if member.id in CS:
            await member.add_roles(CS_role)
        if member.id in Dead_by_Daylight:
            await member.add_roles(Dead_by_Dayilight_role)
        if member.id in Dota2:
            await member.add_roles(Dota2_role)
        if member.id in League_of_Legends:
            await member.add_roles(League_of_Legends_role)
        if member.id in Sea_of_Thieves:
            await member.add_roles(Sea_of_Thieves_role)
        if member.id in Warframe:
            await member.add_roles(Warframe_role)
    except Exception as e:
        print(f'❗❗❗ERROR: Failed to add roles to user: {member.name} due to:\n{e}\n--------------------')
    return None
#-----------------------------------------------------------------------------------


#getMemberFromCtxName
def getMemberFromCtxName(ctx, arg):
    members = ctx.guild.members
    for m in members:
        if arg in m.name:
            return m
    return None
#-----------------------------------------------------------------------------------


#change_nickname
async def change_nickname(member):
    nickname = getNickname(member.id)
    if (nickname is not None):
        try:
            await member.edit(nick = nickname)
        except Exception as e:
            print(f'❗❗❗ERROR: Failed to change nickname on user: {member.name} due to:\n{e}\n--------------------')
    return None
#-----------------------------------------------------------------------------------

#pickFile
def pickFile(name):
    if (name == 'random'):
        rand = random.randint(0, len(lists.sounds)-1)
        trackName = "audio//Sounds//" + lists.sounds[rand]
        return trackName
    elif (name == 'jajao' or name == 'rroulette'):
        return (jajao)
    elif (name =='highlander'):
        rand = random.randint(0, len(lists.highlander)-1)
        trackName = "audio//Highlander//Play//" + lists.highlander[rand]
        return trackName
    elif (name == 'ariana'):
        rand = random.randrange(0, len(lists.ariana)-1)
        trackName = "audio//Ariana Grande//" + lists.ariana[rand]
        return trackName
    elif ((name + ".mp3") in lists.sounds):
        return ("audio//Sounds//" + name + ".mp3")
    return None
#-----------------------------------------------------------------------------------

#picSoundJoin
def pickSoundJoin(id):
    #DANIEL
    if (id == Daniel_id):
        rand = random.randint(0, len(lists.daniel)-1)
        trackName = "audio//Join//Daniel//" + lists.daniel[rand]
        return trackName
    #DAVID
    elif (id == David_id):
        rand = random.randint(0, len(lists.david)-1)
        trackName = "audio//Join//David//" + lists.david[rand]
        return trackName
    #HENRIQUE
    elif (id == Henrique_id):
        rand = random.randint(0, len(lists.henrique)-1)
        trackName = "audio//Join//Henrique//" + lists.henrique[rand]
        return trackName
    #JOAO
    elif (id == Joao_id):
        rand = random.randint(0, len(lists.joao)-1)
        trackName = "audio//Join//Joao//" + lists.joao[rand]
        return trackName
    #KNIGHT
    elif (id == Knight_id):
        rand = random.randint(0, len(lists.knight)-1)
        trackName = "audio//Join//Knight//" + lists.knight[rand]
        return trackName
    #POSEIDON
    elif (id == Poseidon_id):
        rand = random.randint(0, len(lists.poseidon)-1)
        trackName = "audio//Join//Poseidon//" + lists.poseidon[rand]
        return trackName
    #RAFA
    elif (id == Rafa_id):
        rand = random.randint(0, len(lists.rafa)-1)
        trackName = "audio//Join//Rafa//" + lists.rafa[rand]
        return trackName
    #TOURET
    elif (id == Touret_id):
        rand = random.randint(0, len(lists.touret)-1)
        trackName = "audio//Join//Touret//" + lists.touret[rand]
        return trackName
    #VALDEMAR
    elif (id == Valdemar_id):
        rand = random.randint(0, len(lists.valdemar)-1)
        trackName = "audio//Join//Valdemar//" + lists.valdemar[rand]
        return trackName
    #VERDE
    elif (id == Verde_id):
        rand = random.randint(0, len(lists.verde)-1)
        trackName = "audio//Join//Verde//" + lists.verde[rand]
        return trackName
    #WILSON
    elif (id == Wilson_id):
        rand = random.randint(0, len(lists.wilson)-1)
        trackName = "audio//Join//Wilson//" + lists.wilson[rand]
        return trackName
    #YUSUKE
    elif (id == Yusuke_id):
        rand = random.randint(0, len(lists.yusuke)-1)
        trackName = "audio//Join//Yusuke//" + lists.yusuke[rand]
        return trackName
    #ZE
    elif (id == Ze_id):
        rand = random.randint(0, len(lists.ze)-1)
        trackName = "audio//Join//Ze//" + lists.ze[rand]
        return trackName
    return None
#-----------------------------------------------------------------------------------


#roulette
async def roulette(bot, ctx, type):
    auth_id = ctx.author.id
    voice_ch = ctx.author.voice.channel
    members = voice_ch.members
    guild = ctx.guild
    if (auth_id in privileged_id_list):
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune"):
                members.remove(m)
    else:
        for m in members[:]:
            if (m.bot or m.top_role.name == "Immune" or m.id in privileged_id_list):
                members.remove(m)
    if (type == 1):
        end_message = "Rip "
        num_kicks = 1
    else:
        end_message = "It as been declared by highlander, that the one true fagget is: "
        num_kicks = len(members) - 1
    print(f'Users playing: {members}')
    for i in range(num_kicks):
        rand = random.randint(0, len(members)-1)
        to_kick = members[rand]
        try:
            invite = await ctx.channel.create_invite(max_age = 3600, max_uses = 1)
            invite_msg = "You lost. Join us again bitch\n Click the link to join:" + invite.url
            del members[rand]
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
#-----------------------------------------------------------------------------------


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
#-----------------------------------------------------------------------------------
