import encodings
import json 
import jieba
filename = "F:\\Desktop_From_C\\project\\Step3 Search\\a.json"  

with open(filename,encoding='utf-8') as data:
    Dictionary = json.load(data)

def TitleTurntoSet(Dictionary):
    SetDic = {}
    afterwords = []
    KeysTitle = list(Dictionary.keys())
    for i in range(0,len(KeysTitle)):
        words = jieba.cut_for_search(KeysTitle[i],HMM=True)
        afterwords=[w for w in words]
        afterwords.append(KeysTitle[i])
        SetDic.update({KeysTitle[i]:set(afterwords)})
        #print(afterwords)
        Dictionary[KeysTitle[i]]['0'] =afterwords  
    return SetDic
#print(Dictionary)
Copy = TitleTurntoSet(Dictionary)
#print(Copy)



