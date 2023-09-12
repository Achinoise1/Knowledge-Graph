import encodings
import re
import json
from typing import Dict 
import jieba
import copy
from pyparsing import Iterable

filename = "./templates/b.json"  
Set = set()
with open(filename,encoding='utf-8') as data:
    Dic = json.load(data)

KeysTitle = list(Dic.keys())
for i in range(0,len(KeysTitle)):
    KeysOrder = list(Dic[KeysTitle[i]].keys())
    for j in range (0,len(KeysOrder)):
        KeysContent = list(Dic[KeysTitle[i]][KeysOrder[j]])
        for l in range(0,len(KeysContent)):
            Dic[KeysTitle[i]][KeysOrder[j]][l] = Dic[KeysTitle[i]][KeysOrder[j]][l].lower()
            
            
with open("b.json", "w",encoding='utf-8') as f:
    f.write(json.dumps(Dic, ensure_ascii=False, indent=4, separators=(',', ':')))