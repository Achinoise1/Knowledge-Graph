import encodings
import json
from typing import Dict 
import math
import jieba
from pyparsing import Iterable
import re
str = "text"
str.upper()
KeysTitle = ['Web应用开发','yy','zz','aa','bb','cc']
words = jieba.cut_for_search(KeysTitle[0],HMM=True)
print(type(words))
for w in words:
    if re.match(r'[a-zA-Z]+',w) != None:
        w=w.lower()
        print(1)
    print(w)
print(type(str))
print(str)
