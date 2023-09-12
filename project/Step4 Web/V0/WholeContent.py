import encodings
import json
from typing import Dict 
import jieba
import copy
from pyparsing import Iterable

ContentTitle = ["","",""]
ContentNum = [0,0,0]
ContentPos = [["",""],["",""],["",""]]

def Init():
    for i in range(0,3):
        ContentTitle[i] = ""
        ContentNum[i] = 0
        ContentPos[i] = ["",""]      

def procedureContent(str):
    filename = "./templates/a.json"  
    Init()
    with open(filename,encoding='utf-8') as data:
        Dic = json.load(data)
    Copy = copy.deepcopy(Dic)
    Dic = ContentTurntoSet(Dic)

    segment = jieba.cut_for_search(str,HMM=True)
    Set =set([s for s in segment])

    ContentSearchDealTitle(Set,Dic)
    Display(Copy)     
    
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

def sortThreeNum(Num:Iterable,Title:Iterable,POS):
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

def CountSimilarity(Set,List,Position,OrderPos):
    for i in range(0,len(List)):
        #print(JaccardSimilarity(Set,List[i]))
        if JaccardSimilarity(Set,List[i]) > ContentNum[2]:
            ContentPos[2][0] = OrderPos
            ContentPos[2][1] = i+1
            ContentTitle[2] = Position
            ContentNum[2] = JaccardSimilarity(Set,List[i])
            sortThreeNum(ContentNum,ContentTitle,ContentPos)

def ContentSearchDealTitle(Set,Dictionary):
    Keys = list(Dictionary.keys())
    for i in range(0,len(Keys)):
        Position = Keys[i]
        ContentSearchTitle(Set,Dictionary[Keys[i]],Position,"")

def ContentSearchTitle(Set,Dictionary,Position,OrderPos):
    if type(Dictionary) == list:
        CountSimilarity(Set,Dictionary,Position,OrderPos)
    else:
        Keys = list(Dictionary.keys())
        for i in range(0,len(Keys)):
            ContentSearchTitle(Set,Dictionary[Keys[i]],Position,Keys[i])
            
def Display(Dict):
    for i in range(0,3):
        if(ContentTitle[i]!=""):
            print(ContentTitle[i])
            print(ContentNum[i])
            print(ContentPos[i][0])
            print(ContentPos[i][1])
            ContentNum[i] *=100
            ContentNum[i] = round(ContentNum[i],1)
            print(Dict[ContentTitle[i]])
    

# str = input()
# procedureContent(str)