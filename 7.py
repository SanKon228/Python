from collections import Counter
def task3(t,n,w):
    res=0
    for i in w:
        print(Counter(i) , Counter(t))
        print(Counter(i) | Counter(t), Counter(t))
        if Counter(i) | Counter(t) == Counter(t):
            res+=1
    return res
print(task3('moloko',6,['m','mo','mol','molo','molok','moloko']))
