import encodings
import json 
import jieba
from pyparsing import Iterable
filename = "F:\\Desktop_From_C\\project\\Step3 Search\\a.json"  

with open(filename,encoding='utf-8') as data:
    Dictionary = json.load(data)

def TitleTurntoSet(Dictionary):
    SetDic = {}
    afterwords = []
    totalCourse = []
    KeysTitle = list(Dictionary.keys())
    for i in range(0,len(KeysTitle)):
        words = jieba.cut_for_search(KeysTitle[i],HMM=True)
        afterwords=[w for w in words]
        totalCourse.append(KeysTitle[i])
        #afterwords.append(KeysTitle[i])
        SetDic.update({KeysTitle[i]:set(afterwords)})
        #print(afterwords)
        #Dictionary[KeysTitle[i]]['0'] =afterwords
    SetDic.update({'total':set(totalCourse)})  
    return SetDic

#print(Dictionary)
Copy = TitleTurntoSet(Dictionary)
#print(Copy)

#改用struct应该更好吧
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
    return array

def SearchTitleWithWords(Set,Dictionary,Origin):
    Correspond = ["","",""]
    Array = [0,0,0]
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
        #降序存10个，小于阈值直接break
        else:      
            #存在还未取到max直接break出去
            #阈值设置过高会导致输入关键字返回为空
            if len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]])) > Array[2]:
                print(0)
                Correspond[2] = KeysTitle[i]
                Array[2] = len(set.intersection(Set,Dictionary[KeysTitle[i]]))/len(set.union(Set,Dictionary[KeysTitle[i]]))
                sortThreeNum(Array,Correspond)
                #print(Origin[KeysTitle[i]])
    #Test
    if(Correspond[0] != ''):
        print(Correspond[0])
        print(Origin[Correspond[0]])
    if(Correspond[1] != ''):  
        print(Correspond[1]) 
        print(Origin[Correspond[1]])
    if(Correspond[2] != ''):
        print(Correspond[2])
        print(Origin[Correspond[2]])

Set = set()
#Set.add("数据结构与算法")
Set.add("算法")
#输入根据空格切分
SearchTitleWithWords(Set,Copy,Dictionary)


#teststr = "数据结构与算法课程设计"
#teststr = "计算机组成原理课程设计"
#teststr = "虚拟化与云计算项目实践"
#teststr = "毕业设计分析与综合实践"
#teststr = "Python程序设计高阶"
#print(list(jieba.cut_for_search(teststr,HMM=True)))
