import encodings
import json 
import jieba
from pyparsing import Iterable
filename = "F:\\Desktop_From_C\\project\\Step3 Search\\a.json"  

with open(filename,encoding='utf-8') as data:
    Dictionary = json.load(data)

def ContentTurntoSet(Dictionary):
    SetDic = {}
    afterwords = []
    KeysTitle = list(Dictionary.keys())
    for i in range(0,len(KeysTitle)):
        KeysOrder = list(Dictionary[KeysTitle[i]].keys())
        for j in range(0,len(KeysOrder)):
            KeysContent = list(Dictionary[KeysTitle[i]][KeysOrder[j]])
            for l in range(0,len(KeysContent)):              
                words = jieba.cut_for_search(Dictionary[KeysTitle[i]][KeysOrder[j]][l],HMM = True)
                #print(Dictionary[KeysTitle[i]][KeysOrder[j]])
                afterwords = afterwords + [w for w in words]
                SetDic.update({KeysTitle[i]:set(afterwords)})
    return SetDic

Copy = ContentTurntoSet(Dictionary)
print(Copy)

for i in range(0,1):
    print(Copy[list(Dictionary.keys())[i]])




#改用struct应该更好吧
def sortThreeNum(array:Iterable,Name:Iterable):
    if(array[0]<array[1]):
        tempnum = array[1]
        array[1] = array[0]
        array[0] = tempnum
        Tempstr = Name[1]
        Name[1] = Name[0]
        Name[0] = Tempstr
    if(array[0]<array[2]):
        tempnum = array[2]
        array[2] = array[0]
        array[0] = tempnum
        Tempstr = Name[2]
        Name[2] = Name[0]
        Name[0] = Tempstr
    if(array[1]<array[2]):
        tempnum = array[2]
        array[2] = array[1]
        array[1] = tempnum
        Tempstr = Name[2]
        Name[2] = Name[1]
        Name[1] = Tempstr

def SearchContentWithWords(Set:set,Dictionary,Origin):
    Correspond = ["","",""]
    Array = [0,0,0]
    KeysTitle = list(Dictionary.keys()) 
    for i in range(0,len(KeysTitle)):
        if Set.issubset(Dictionary[KeysTitle[i]]) == False:
            continue
        else:
            if len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]]))>Array[2]:
                num = len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]]))
                Correspond[2] = KeysTitle[i]
                Array[2] = num
                sortThreeNum(Array,Correspond)
            
    if(Correspond[0] != ''):
        print(Correspond[0])
        print(Origin[Correspond[0]])
    if(Correspond[1] != ''):  
        print(Correspond[1]) 
        print(Origin[Correspond[1]])
    if(Correspond[2] != ''):
        print(Correspond[2])
        print(Origin[Correspond[2]])





#Set.add("数据结构与算法")
'''str = input()
segment = jieba.cut_for_search(str,HMM=True)
Set = set([s for s in segment])

if ' ' in Set:
    Set.remove(' ')
print(Set)
SearchContentWithWords(Set,Copy,Dictionary)'''
#输入根据空格切分
#SearchTitleWithWords(Set,CopyTitle,Dictionary)
