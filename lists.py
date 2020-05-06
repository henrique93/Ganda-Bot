 #soundLists.py
import os

#-------------------------------------- INIT ---------------------------------------
def initLists():
    initAriana()
    initHighlander()
    initHighlanderVictory()
    initSounds()
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

#---------------------------------- ARIANA GRANDE ----------------------------------
ariana = []

def initAriana():
    global ariana
    path = "audio//Ariana Grande//"
    ariana = os.listdir(path)
#-----------------------------------------------------------------------------------

#----------------------------------- HIGHLANDER ------------------------------------
highlander = []

def initHighlander():
    global highlander
    path = "audio//Highlander//Play//"
    highlander = os.listdir(path)

#Highlander Victory Songs
highlanderVictory = []

def initHighlanderVictory():
    global highlanderVictory
    path = "audio//Highlander//Victory//"
    highlanderVictory = os.listdir(path)
#-----------------------------------------------------------------------------------

#------------------------------------- SOUNDS --------------------------------------
sounds = []

def initSounds():
    global sounds
    path = "audio//Sounds//"
    sounds = os.listdir(path)
#-----------------------------------------------------------------------------------

#----------------------------------- JOIN SOUNDS -----------------------------------
#Daniel
daniel = []

def initDaniel():
    global daniel
    path = "audio//Join//Daniel//"
    daniel = os.listdir(path)

#David
david = []

def initDavid():
    global david
    path = "audio//Join//David//"
    david = os.listdir(path)

#Henrique
henrique = []

def initHenrique():
    global henrique
    path = "audio//Join//Henrique//"
    henrique = os.listdir(path)

#Joao
joao = []

def initJoao():
    global joao
    path = "audio//Join//Joao//"
    joao = os.listdir(path)

#Knight
knight = []

def initKnight():
    global knight
    path = "audio//Join//Knight//"
    knight = os.listdir(path)

#Poseidon
poseidon = []

def initPoseidon():
    global poseidon
    path = "audio//Join//Poseidon//"
    poseidon = os.listdir(path)

#Rafa
rafa = []

def initRafa():
    global rafa
    path = "audio//Join//Rafa//"
    rafa = os.listdir(path)

#Touret
touret = []

def initTouret():
    global touret
    path = "audio//Join//Touret//"
    touret = os.listdir(path)

#Valdemar
valdemar = []

def initValdemar():
    global valdemar
    path = "audio//Join//Valdemar//"
    valdemar = os.listdir(path)

#Verde
verde = []

def initVerde():
    global verde
    path = "audio//Join//Verde//"
    verde = os.listdir(path)

#Wilson
wilson = []

def initWilson():
    global Wilson
    path = "audio//Join//Wilson//"
    wilson = os.listdir(path)

#Yusuke
yusuke = []

def initYusuke():
    global yusuke
    path = "audio//Join//Yusuke//"
    yusuke = os.listdir(path)

#Ze
ze = []

def initZe():
    global ze
    path = "audio//Join//Ze//"
    ze = os.listdir(path)
#-----------------------------------------------------------------------------------


#------------------------------------- MUTED ---------------------------------------
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
#-----------------------------------------------------------------------------------
