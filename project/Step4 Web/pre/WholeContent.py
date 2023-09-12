import encodings
import json 
import jieba
import copy
from pyparsing import Iterable

ContentTitle = ["","",""]
ContentNum = [0,0,0]
ContentPos = [["",""],["",""],["",""]]

def procedureContent():
    filename = "F:\\Desktop_From_C\\project\\Step3 Search\\a.json"  

    with open(filename,encoding='utf-8') as data:
        Dic = json.load(data)
    Copy = copy.deepcopy(Dic)
    #print(Copy)
    Dic = ContentTurntoSet(Dic)
    #print(Copy)
    
    str = input()
    segment = jieba.cut_for_search(str,HMM=True)
    Set = set([s for s in segment])
    if ' ' in Set:
        Set.remove(' ')

    ContentSearchDealTitle(Set,Dic)
    #print(Copy)
    Display(ContentNum,ContentTitle,Copy)     
    
def Split(List):
    for i in range(0,len(List)):
        words = jieba.cut_for_search(List[i],HMM = True)
        afterwords = set([w for w in words])
        List[i] = afterwords
    
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
            
def Display(Num:Iterable,Title:Iterable,Dictionary:dict):
    #Keys = list(Dictionary.keys())
    print("")
    if Num[0] != 0:
        #print(Num[0])
        Location(ContentPos,0,Title[0])
        print(Dictionary[Title[0]])
        print("")
    if Num[1] != 0:
        #print(Num[1])
        Location(ContentPos,1,Title[1])
        print(Dictionary[Title[1]])
        print("")
    if Num[2] != 0:
        #print(Num[2])
        Location(ContentPos,2,Title[2])
        print(Dictionary[Title[2]])
        print("")
    
def Location(List,num,Title):
    print("近似与您所查询的知识点位于",end=': ')
    print(Title,end =" 课程中第 ")
    print(List[num][0],end = " 章节第 ")
    print(List[num][1],end = " 个知识点中")
    print("     近似程度",end=': ')
    print(ContentNum[num]*100,end='')
    print("%")

procedureContent()