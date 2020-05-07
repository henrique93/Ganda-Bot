 #soundLists.py
import os

#IP - [folder path, nickname, [join sound list], [roles]]
idDictionary = {
    190917034173923328 : ["audio//Join//Castanheira//", "Castanheira", [], []],
    170845221452513280 : ["audio//Join//Daniel//", "Maverick 🐧", [], []],
    150575793603477505 : ["audio//Join//David//", "Daskdadi", [], []],
    181219804537946112 : ["audio//Join//Henrique//", "M4ST3R 🌊", [], []],
    269850685497933824 : ["audio//Join//Joao//", "Mr.WOLF 🐺", [], []],
    269955800489918464 : ["audio//Join//Knight//", "Kanight", [], []],
    194896718570061825 : ["audio//Join//Poseidon//", "Posidon", [], []],
    203679276309020672 : ["audio//Join//Rafa//", "Rafa", [], []],
    178282201325109248 : ["audio//Join//Touret//", "RKO 💩", [], []],
    155258382557773825 : ["audio//Join//Valdemar//", "Like Always 🔥", [], []],
    231787245307297794 : ["audio//Join//Verde/", "MrVerdinsky 💚", [], []],
    181433562875035648 : ["audio//Join//Wilson//", "Will 🌈", [], []],
    179334253002227712 : ["audio//Join//Yusuke//", "Yusukeeee 🎸", [], []],
    158979279592488962 : ["audio//Join//Ze/", "Ze", [], []]
}

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

rolesDictionary = {}

#user roles
def initRoles(sv):
    members = sv.members
    for m in members:
        rolesDictionary[m.id] = m.roles

#----------------------------- INIT -----------------------------
def initLists():
    initAriana()
    initHighlander()
    initHighlanderVictory()
    initJoinSounds()
    initPermissionDenied()
    initSounds()
    initVoiceUpdate()
    

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

#-------------------------- JOIN SOUNDS -------------------------
#Init join sounds
def initJoinSounds():
    initDaniel()
    initDavid()
    initHenrique()
    initJoao()
    initKnight()
    initPoseidon()
    initRafa()
    initTouret()
    initValdemar()
    initVerde()
    initWilson()
    initYusuke()
    initZe()

#Daniel
def initDaniel():
    path = "audio//Join//Daniel//"
    daniel = os.listdir(path)
    idDictionary[170845221452513280][2] = daniel

#David
def initDavid():
    path = "audio//Join//David//"
    david = os.listdir(path)
    idDictionary[150575793603477505][2] = david

#Henrique
def initHenrique():
    path = "audio//Join//Henrique//"
    henrique = os.listdir(path)
    idDictionary[181219804537946112][2] = henrique

#Joao
def initJoao():
    path = "audio//Join//Joao//"
    joao = os.listdir(path)
    idDictionary[269850685497933824][2] = joao

#Knight
def initKnight():
    path = "audio//Join//Knight//"
    knight = os.listdir(path)
    idDictionary[269955800489918464][2] = knight

#Poseidon
def initPoseidon():
    path = "audio//Join//Poseidon//"
    poseidon = os.listdir(path)
    idDictionary[194896718570061825][2] = poseidon

#Rafa
def initRafa():
    path = "audio//Join//Rafa//"
    rafa = os.listdir(path)
    idDictionary[203679276309020672][2] = rafa

#Touret
def initTouret():
    path = "audio//Join//Touret//"
    touret = os.listdir(path)
    idDictionary[178282201325109248][2] = touret

#Valdemar
def initValdemar():
    path = "audio//Join//Valdemar//"
    valdemar = os.listdir(path)
    idDictionary[155258382557773825][2] = valdemar

#Verde
def initVerde():
    path = "audio//Join//Verde//"
    verde = os.listdir(path)
    idDictionary[231787245307297794][2] = verde

#Wilson
def initWilson():
    path = "audio//Join//Wilson//"
    wilson = os.listdir(path)
    idDictionary[181433562875035648][2] = wilson

#Yusuke
def initYusuke():
    path = "audio//Join//Yusuke//"
    yusuke = os.listdir(path)
    idDictionary[179334253002227712][2] = yusuke

#Ze
def initZe():
    path = "audio//Join//Ze//"
    ze = os.listdir(path)
    idDictionary[158979279592488962][2] = ze
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

def addMuted(id):
    global muted
    if (id is not None):
        muted.append(id)
    return

def removeMuted(id):
    global muted
    if (id is None):
        return
    else:
        muted.remove(id)
        return
#----------------------------------------------------------------
