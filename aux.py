# aux.py
import os
import random
import discord
from discord.utils import get
import asyncio



from consts import *

#Keep muted
keep_muted = []

def getKeepMuted():
    return keep_muted

def addKeepMuted(id):
    global keep_muted
    if (id is not None):
        keep_muted.append(id)
    return

def removeKeepMuted(id):
    global keep_muted
    if (id is not None):
        keep_muted.remove(id)
    return


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


#getMemberIdFromCtxName
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
        rand = random.randint(0, len(catchFrase_list)-1)
        trackName = catchFrase_list[rand]
        return ("audio//" + trackName + ".mp3")
    elif (name == 'jajao' or name == 'rroulette'):
        return ("audio//last_surprise.mp3")
    elif (name =='highlander'):
        rand = random.randint(0, len(highlander_sounds)-1)
        return highlander_sounds[rand]
    elif (name == 'ariana'):
        path ='audio//Ariana Grande//'
        files = os.listdir('audio//Ariana Grande//')
        index = random.randrange(0, len(files))
        return (path + files[index])
    elif ((name in catchFrase_list) or (name + "⛔" in catchFrase_list)):
        return ("audio//" + name + ".mp3")
    return None
#-----------------------------------------------------------------------------------

#picSoundJoin
def pickSoundJoin(id):
    #DANIEL
    if (id == Daniel_id):
        rand = random.randint(0, len(join_sounds_daniel)-1)
        return join_sounds_daniel[rand]
    #DAVID
    elif (id == David_id):
        rand = random.randint(0, len(join_sounds_david)-1)
        return join_sounds_david[rand]
    #HENRIQUE
    elif (id == Henrique_id):
        rand = random.randint(0, len(join_sounds_henrique)-1)
        return join_sounds_henrique[rand]
    #JOAO
    elif (id == Joao_id):
        rand = random.randint(0, len(join_sounds_joao)-1)
        return join_sounds_joao[rand]
    #KNIGHT
    elif (id == Knight_id):
        rand = random.randint(0, len(join_sounds_knight)-1)
        return join_sounds_knight[rand]
    #POSEIDON
    elif (id == Poseidon_id):
        rand = random.randint(0, len(join_sounds_poseidon)-1)
        return join_sounds_poseidon[rand]
    #RAFA
    elif (id == Rafa_id):
        rand = random.randint(0, len(join_sounds_rafa)-1)
        return join_sounds_rafa[rand]
    #TOURET
    elif (id == Touret_id):
        rand = random.randint(0, len(join_sounds_touret)-1)
        return join_sounds_touret[rand]
    #VALDEMAR
    elif (id == Valdemar_id):
        rand = random.randint(0, len(join_sounds_valdemar)-1)
        return join_sounds_valdemar[rand]
    #VERDE
    elif (id == Verde_id):
        rand = random.randint(0, len(join_sounds_verde)-1)
        return join_sounds_verde[rand]
    #WILSON
    elif (id == Wilson_id):
        rand = random.randint(0, len(join_sounds_wilson)-1)
        return join_sounds_wilson[rand]
    #YUSUKE
    elif (id == Yusuke_id):
        rand = random.randint(0, len(join_sounds_yusuke)-1)
        return join_sounds_yusuke[rand]
    #ZE
    elif (id == Ze_id):
        rand = random.randint(0, len(join_sounds_ze)-1)
        return join_sounds_ze[rand]
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
    print(num_kicks)
    for i in range(num_kicks):
        rand = random.randint(0, len(members)-1)
        print(rand)
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
