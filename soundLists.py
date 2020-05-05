#soundLists.py
import os

def initLists():
    initArianaList()
    initHighlanderList()
    initHighlanderVictoryList()
    initSoundList()
    initDanielList()
    initDavidList()
    initHenriqueList()
    initJoaoList()
    initKnightList()
    initPoseidonList()
    initRafaList()
    initTouretList()
    initValdemarList()
    initVerdeList()
    initWilsonList()
    initYusukeList()
    initZeList()

#List of Ariana Grande songs
arianaList = []

def initArianaList():
    global arianaList
    path = "audio//Ariana Grande//"
    arianaList = os.listdir(path)
#-----------------------------------------------------------------------------------

#Highlander Songs
highlanderList = []

def initHighlanderList():
    global highlanderList
    path = "audio//Highlander//Play//"
    highlanderList = os.listdir(path)

#Highlander Victory Songs
highlanderVictoryList = []

def initHighlanderVictoryList():
    global highlanderVictoryList
    path = "audio//Highlander//Victory//"
#-----------------------------------------------------------------------------------

#List of sounds
soundList = []

def initSoundList():
    global soundList
    path = "audio//Sounds//"
    soundList = os.listdir(path)
#-----------------------------------------------------------------------------------

#Join Sounds
#Daniel
danielList = []

def initDanielList():
    global danielList
    path = "audio//Join//Daniel//"
    danielList = os.listdir(path)

#David
davidList = []

def initDavidList():
    global davidList
    path = "audio//Join//David//"
    davidList = os.listdir(path)

#Henrique
henriqueList = []

def initHenriqueList():
    global henriqueList
    path = "audio//Join//Henrique//"
    henriqueList = os.listdir(path)

#Joao
joaoList = []

def initJoaoList():
    global joaoList
    path = "audio//Join//Joao//"
    joaoList = os.listdir(path)

#Knight
knightList = []

def initKnightList():
    global knightList
    path = "audio//Join//Knight//"
    knightList = os.listdir(path)

#Poseidon
poseidonList = []

def initPoseidonList():
    global poseidonList
    path = "audio//Join//Poseidon//"
    poseidonList = os.listdir(path)

#Rafa
rafaList = []

def initRafaList():
    global rafaList
    path = "audio//Join//Rafa//"
    rafaList = os.listdir(path)

#Touret
touretList = []

def initTouretList():
    global touretList
    path = "audio//Join//Touret//"
    touretList = os.listdir(path)

#Valdemar
valdemarList = []

def initValdemarList():
    global valdemarList
    path = "audio//Join//Valdemar//"
    valdemarList = os.listdir(path)

#Verde
verdeList = []

def initVerdeList():
    global verdeList
    path = "audio//Join//Verde//"
    verdeList = os.listdir(path)

#Wilson
wilsonList = []

def initWilsonList():
    global WilsonList
    path = "audio//Join//Wilson//"
    wilsonList = os.listdir(path)

#Yusuke
yusukeList = []

def initYusukeList():
    global yusukeList
    path = "audio//Join//Yusuke//"
    yusukeList = os.listdir(path)

#Ze
zeList = []

def initZeList():
    global zeList
    path = "audio//Join//Ze//"
    zeList = os.listdir(path)
#-----------------------------------------------------------------------------------
