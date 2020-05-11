 #soundLists.py
import os

from consts import joinSoundPath
from consts import youtubePath
#----------------------------------------------------------------


#Type : [folder path, [sound list]]
playDictionary = {
    "ariana" : ["audio/Ariana Grande/", []],
    "denied" : ["audio/PermissionDenied/", []],
    "highlander" : ["audio/Highlander/Play/", []],
    "highlanderv" : ["audio/Highlander/Victory/", []],
    "leave" : ["audio/VoiceUpdate/Leave/", []],
    "random" : ["audio/Sounds/", []],
    "selfDeaf" : ["audio/VoiceUpdate/Self/Deafen/", []],
    "selfUndeaf" : ["audio/VoiceUpdate/Self/Undeafen/", []]
}

#initSoundLists
def init_sound_lists():
    for e in playDictionary.values():
        path = e[0]
        sounds = os.listdir(path)
        e[1] = sounds
#----------------------------------------------------------------
#serverID : memberInfo
serverMembers = {}

def init_server_members(sv):
    svMembersInfo = init_member_info(sv)
    serverMembers[sv.id] = svMembersInfo

def init_member_info(sv):
    #ID : [[roles], nickname, [join sounds]]
    memberInfo = {}
    members = sv.members
    for m in members:
        info = []
        info.append(m.roles)
        info.append(m.nick)
        path = joinSoundPath + str(m.id) + "/"
        if (os.path.isdir(path)):
            joinSounds = os.listdir(path)
            info.append(joinSounds)
        else:
            info.append(None)
        memberInfo[m.id] = info
    return memberInfo

#serverID : [sounds to play]
queues = {}

#serverID : voice state
voiceStates = {}


#---------------------------- MUTED -----------------------------
#Keep muted
muted = []

#----------------------------------------------------------------


#-------------------------- YOUTUBE-DL --------------------------
#serverID : ytdl_opts
ytdl_options = {}

def init_ytdl_options(serverId):
    path = youtubePath + str(serverId) + "/%(title)s-%(id)s.%(ext)s"
    ytdl_opts = {
        'format' : 'bestaudio/best',
        'outtmpl': path,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }]
    }
    ytdl_options[serverId] = ytdl_opts
