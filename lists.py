 #soundLists.py
import os

from consts import joinSoundPath

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

#ID : [[roles], nickname, [join sounds]]
memberInfo = {}

def initMemberInfo(sv):
    members = sv.members
    for m in members:
        info = []
        info.append(m.roles)
        info.append(m.nick)
        path = joinSoundPath + str(m.id) + "//"
        if (os.path.isdir(path)):
            print(path)
            joinSounds = os.listdir(path)
            info.append(joinSounds)
        else:
            info.append(None)
        memberInfo[m.id] = info

#server ID : voice state
voiceStates = {}

#serverID : [sounds to play]
queues = {}

#----------------------------- INIT -----------------------------
def initLists():
    initAriana()
    initHighlander()
    initHighlanderVictory()
    initPermissionDenied()
    initSounds()
    initVoiceUpdate()
#----------------------------------------------------------------
    

#------------------------- ARIANA GRANDE ------------------------
def initAriana():
    path = "audio//Ariana Grande//"
    ariana = os.listdir(path)
    playDictionary["ariana"][1] = ariana
#----------------------------------------------------------------


#-------------------------- HIGHLANDER --------------------------
def initHighlander():
    path = "audio//Highlander//Play//"
    highlander = os.listdir(path)
    playDictionary["highlander"][1] = highlander

#Highlander Victory Songs
def initHighlanderVictory():
    path = "audio//Highlander//Victory//"
    highlanderVictory = os.listdir(path)
    playDictionary["highlanderv"][1] = highlanderVictory
#----------------------------------------------------------------


#---------------------- PERMISSION DENIED -----------------------
#Permission denied
def initPermissionDenied():
    path = "audio//PermissionDenied//"
    permissionDenied = os.listdir(path)
    playDictionary["denied"][1] = permissionDenied
#----------------------------------------------------------------


#---------------------------- SOUNDS ----------------------------
#Sounds
def initSounds():
    path = "audio//Sounds//"
    sounds = os.listdir(path)
    playDictionary["random"][1] = sounds
#----------------------------------------------------------------


#------------------------- VOICE UPDATE -------------------------
#Init voice update
def initVoiceUpdate():
    initLeave()
    initSelfDeaf()
    initSelfUndeaf()

#Leave channel
def initLeave():
    path = "audio//VoiceUpdate//Leave//"
    leave = os.listdir(path)
    playDictionary["leave"][1] = leave

#Self deafen
def initSelfDeaf():
    path = "audio//VoiceUpdate//Self//Deafen//"
    selfDeaf = os.listdir(path)
    playDictionary["selfDeaf"][1] = selfDeaf

#Self undeafen
def initSelfUndeaf():
    path = "audio//VoiceUpdate//Self//Undeafen//"
    selfUndeaf = os.listdir(path)
    playDictionary["selfUndeaf"][1] = selfUndeaf
#----------------------------------------------------------------


#---------------------------- MUTED -----------------------------
#Keep muted
muted = []

#----------------------------------------------------------------
