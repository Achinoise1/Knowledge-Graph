import jieba
str = "希望疫情快点结束"
alist = jieba.cut(str,cut_all = False)
print(",".join(alist))