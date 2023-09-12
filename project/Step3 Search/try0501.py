import encodings
import json 
import jieba
from pyparsing import Iterable
filename = "F:\\Desktop_From_C\\project\\Step3 Search\\a.json"  

with open(filename,encoding='utf-8') as data:
    Dic = json.load(data)
    
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

Copy = Dic.copy()
print(Copy)
Copy = ContentTurntoSet(Copy)
#print(Copy)

str = input()
segment = jieba.cut_for_search(str,HMM=True)
Set = set([s for s in segment])
Set.remove(' ')

ContentTitle = ["","",""]
ContentNum = [0,0,0]
ContentPos = ["","",""]     

def sortThreeNum(Num:Iterable,Title:Iterable):
    temp = 0.0
    Temp = ""
    if(Num[0]<Num[1]):
        temp = Num[1]
        Num[1] = Num[0]
        Num[0] = temp
        Temp = Title[1]
        Title[1] = Title[0]
        Title[0] = Temp
    if(Num[0]<Num[2]):
        temp = Num[2]
        Num[2] = Num[0]
        Num[0] = temp
        Temp = Title[2]
        Title[2] = Title[0]
        Title[0] = Temp
    if(Num[1]<Num[2]):
        temp = Num[2]
        Num[2] = Num[1]
        Num[1] = temp
        Temp = Title[2]
        Title[2] = Title[1]
        Title[1] = Temp

def JaccardSimilarity(SetInput,SetContent):
    return len(set.intersection(SetInput,SetContent))/len(set.union(SetInput,SetContent))

def CountSimilarity(Set,List,Position):
    for i in range(0,len(List)):
        #print(JaccardSimilarity(Set,List[i]))
        if JaccardSimilarity(Set,List[i]) > ContentNum[2]:
            ContentTitle[2] = Position
            ContentNum[2] = JaccardSimilarity(Set,List[i])
            sortThreeNum(ContentNum,ContentTitle)

def ContentSearchDealTitle(Set,Dictionary):
    Keys = list(Dictionary.keys())
    for i in range(0,len(Keys)):
        Position = Keys[i]
        ContentSearchTitle(Set,Dictionary[Keys[i]],Position)

def ContentSearchTitle(Set,Dictionary,Position):
    if type(Dictionary) == list:
        CountSimilarity(Set,Dictionary,Position)
    else:
        Keys = list(Dictionary.keys())
        for i in range(0,len(Keys)):
            ContentSearchTitle(Set,Dictionary[Keys[i]],Position)
            
def Display(Num:Iterable,Title:Iterable,Dictionary:dict):
    #Keys = list(Dictionary.keys())
    if Num[0] != 0:
        print(Num[0])
        print(Title[0])
        print(Dictionary[Title[0]])
    if Num[1] != 0:
        print(Num[1])
        print(Title[1])
        print(Dictionary[Title[1]])
    if Num[2] != 0:
        print(Num[2])
        print(Title[2])
        print(Dictionary[Title[2]])
    #print(555)

ContentSearchDealTitle(Set,Copy)
Display(ContentNum,ContentTitle,Dic)