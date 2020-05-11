 #soundLists.py
import os

from consts import joinSoundPath
#----------------------------------------------------------------


#Type : [folder path, [sound list]]
playDictionary = {
    "ariana" : ["audio//Ariana Grande//", []],
    "denied" : ["audio//PermissionDenied//", []],
    "highlander" : ["audio//Highlander//Play//", []],
    "highlanderv" : ["audio//Highlander//Victory//", []],
    "leave" : ["audio//VoiceUpdate//Leave//", []],
    "random" : ["audio//Sounds//", []],
    "selfDeaf" : ["audio//VoiceUpdate//Self//Deafen//", []],
    "selfUndeaf" : ["audio//VoiceUpdate//Self//Undeafen//", []]
}

#initSoundLists
def initSoundLists():
    for e in playDictionary.values():
        path = e[0]
        sounds = os.listdir(path)
        e[1] = sounds
#----------------------------------------------------------------
#serverID : memberInfo
serverMembers = {}

def initServerMembers(sv):
    svMembersInfo = initMemberInfo(sv)
    serverMembers[sv.id] = svMembersInfo

def initMemberInfo(sv):
    #ID : [[roles], nickname, [join sounds]]
    memberInfo = {}
    members = sv.members
    for m in members:
        info = []
        info.append(m.roles)
        info.append(m.nick)
        path = joinSoundPath + str(m.id) + "//"
        if (os.path.isdir(path)):
            joinSounds = os.listdir(path)
            info.append(joinSounds)
        else:
            info.append(None)
        memberInfo[m.id] = info
    return memberInfo

#serverID : voice state
voiceStates = {}

#serverID : [sounds to play]
queues = {}


#---------------------------- MUTED -----------------------------
#Keep muted
muted = []

#----------------------------------------------------------------
