import encodings
import json
from typing import Dict 
import math
import jieba
from pyparsing import Iterable

Correspond = ["","",""]
Array = [0,0,0]

def Init():
    for i in range(0,3):
        Correspond[i]=""
        Array[i]=0

def procedureTitle(str):
    filename = "./templates/a.json"  
    Init()
    with open(filename,encoding='utf-8') as data:
        Dictionary = json.load(data)
    
    CopyTitle = TitleTurntoSet(Dictionary)
    segment = jieba.cut_for_search(str,HMM=True)
    Set = set([s for s in segment])
    
    SearchTitleWithWords(Set,CopyTitle,Dictionary)
    Display(Dictionary)
    
def TitleTurntoSet(Dictionary):
    SetDic = {}
    afterwords = []
    totalCourse = []
    KeysTitle = list(Dictionary.keys())
    for i in range(0,len(KeysTitle)):
        words = jieba.cut_for_search(KeysTitle[i],HMM=True)
        afterwords=[w for w in words]
        totalCourse.append(KeysTitle[i])
        SetDic.update({KeysTitle[i]:set(afterwords)})
    SetDic.update({'total':set(totalCourse)})  
    return SetDic

def sortThreeNum(array:Iterable,Name:Iterable):
    if(array[0]<array[1]):
        temp = array[1]
        array[1] = array[0]
        array[0] = temp
        temp = Name[1]
        Name[1] = Name[0]
        Name[0] = temp
    if(array[0]<array[2]):
        temp = array[2]
        array[2] = array[0]
        array[0] = temp
        temp = Name[2]
        Name[2] = Name[0]
        Name[0] = temp
    if(array[1]<array[2]):
        temp = array[2]
        array[2] = array[1]
        array[1] = temp
        temp = Name[2]
        Name[2] = Name[1]
        Name[1] = temp

#start searching
def SearchTitleWithWords(Set,Dictionary,Origin):
    
    KeysTitle = list(Dictionary.keys())
    #直接输入全名
    if len(Set)==1 and list(Set)[0] in Dictionary['total']:
        print(Origin[list(Set)[0]])
        return
    #部分关键字
    for i in range(0,len(KeysTitle)):
        #不在结合内直接跳过
        if set.intersection(Set,Dictionary[KeysTitle[i]]) == None:
            continue
        #降序存3个，小于阈值直接break
        else:      
            #存在还未取到max直接break出去
            #阈值设置过高会导致输入关键字返回为空
            if len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]])) > Array[2]:
                #print(0)
                Correspond[2] = KeysTitle[i]
                Array[2] = len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]]))
                sortThreeNum(Array,Correspond)

def Display(Origin):
    for i in range(0,3):
        if(Correspond[i] != ''):
            Array[i] *= 100
            Array[i] = round(Array[i],1)
            print(Correspond[i])
            print(Origin[Correspond[i]])
 
# str = input() 
# procedureTitle(str)