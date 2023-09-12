import json
with open("./a.json",encoding='utf-8') as data:
        Dic = json.load(data)
DicCopy = {}
DicCopy.update({"信息安全基础":Dic["信息安全基础"]})
print(DicCopy)