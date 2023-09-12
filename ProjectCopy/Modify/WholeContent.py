import encodings
import json
from typing import Dict 
import jieba
import copy
from pyparsing import Iterable

def Init(Title,Num,Pos):
    for i in range(0,3):
        Title[i] = ""
        Num[i] = 0
        Pos[i] = ["",""]      

def procedureContent(str:str):
    ContentTitle = ["","",""]
    ContentNum = [0,0,0]
    ContentPos = [["",""],["",""],["",""]]
    filename = "./templates/b.json"  
    file = "./templates/a.json"
    Init(ContentTitle,ContentNum,ContentPos)
    with open(filename,encoding='utf-8') as data:
        Dic = json.load(data)
    with open(file,encoding='utf-8') as data:
        DicOri = json.load(data)
    Copy = copy.deepcopy(Dic)
    Dic = ContentTurntoSet(Dic)
    str = str.lower()
    segment = jieba.cut_for_search(str,HMM=True)
    Set =set([s for s in segment])

    ContentSearchDealTitle(Set,Dic,ContentTitle,ContentNum,ContentPos)
    Display(Copy,ContentTitle,ContentNum,ContentPos)
    MatchWithOriginDic(Dic,DicOri,ContentTitle)
    return [ContentTitle,ContentNum,ContentPos]
         
    
def Split(List):
    for i in range(0,len(List)):
        words = jieba.cut_for_search(List[i],HMM = True)
        afterwords = [w for w in words]
        List[i] = set(afterwords)
    
def ContentTurntoSet(Dictionary):
    if type(Dictionary) == list:
        Split(Dictionary)
    else:
        Keys = list(Dictionary.keys())
        for i in range(0,len(Keys)):
            ContentTurntoSet(Dictionary[Keys[i]])
    return Dictionary

def sortThreeNum(Num:Iterable,Title:Iterable,POS:Iterable):
    temp = 0.0
    Temp = ""
    TEMP = ["","",""]
    if(Num[0]<Num[1]):
        temp = Num[1]
        Num[1] = Num[0]
        Num[0] = temp
        Temp = Title[1]
        Title[1] = Title[0]
        Title[0] = Temp
        TEMP = POS[1]
        POS[1] = POS[0]
        POS[0] = TEMP
    if(Num[0]<Num[2]):
        temp = Num[2]
        Num[2] = Num[0]
        Num[0] = temp
        Temp = Title[2]
        Title[2] = Title[0]
        Title[0] = Temp
        TEMP = POS[2]
        POS[2] = POS[0]
        POS[0] = TEMP
    if(Num[1]<Num[2]):
        temp = Num[2]
        Num[2] = Num[1]
        Num[1] = temp
        Temp = Title[2]
        Title[2] = Title[1]
        Title[1] = Temp
        TEMP = POS[2]
        POS[2] = POS[1]
        POS[1] = TEMP

def JaccardSimilarity(SetInput,SetContent):
    return len(set.intersection(SetInput,SetContent))/len(set.union(SetInput,SetContent))

def CountSimilarity(Set,List,Position,OrderPos,Title,Num,Pos):
    for i in range(0,len(List)):
        #print(JaccardSimilarity(Set,List[i]))
        if JaccardSimilarity(Set,List[i]) > Num[2]:
            Pos[2][0] = OrderPos
            Pos[2][1] = i+1
            Title[2] = Position
            Num[2] = JaccardSimilarity(Set,List[i])
            sortThreeNum(Num,Title,Pos)

def ContentSearchDealTitle(Set,Dictionary,Title,Num,Pos):
    Keys = list(Dictionary.keys())
    for i in range(0,len(Keys)):
        Position = Keys[i]
        ContentSearchTitle(Set,Dictionary[Keys[i]],Position,"",Title,Num,Pos)

def ContentSearchTitle(Set,Dictionary,Position,OrderPos,Title,Num,Pos):
    if type(Dictionary) == list:
        CountSimilarity(Set,Dictionary,Position,OrderPos,Title,Num,Pos)
    else:
        Keys = list(Dictionary.keys())
        for i in range(0,len(Keys)):
            ContentSearchTitle(Set,Dictionary[Keys[i]],Position,Keys[i],Title,Num,Pos)

def MatchWithOriginDic(Dic,DicOri,Title):
    KeysD = list(Dic.keys())
    KeysDO = list(DicOri.keys())
    for i in range(0,len(KeysD)):
        if Title[0] == KeysD[i]:
            Title[0] = KeysDO[i]
        if Title[1] == KeysD[i]:
            Title[1] = KeysDO[i]
        if Title[2] == KeysD[i]:
            Title[2] = KeysDO[i]

            
def Display(Dict,Title,Num,Pos):
    for i in range(0,3):
        if(Title[i]!=""):
            print(Title[i])
            print(Num[i])
            print(Pos[i][0])
            print(Pos[i][1])
            Num[i] *=100
            Num[i] = round(Num[i],1)
            print(Dict[Title[i]])
    

# str = input()
# procedureContent(str)