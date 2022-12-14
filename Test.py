def combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(len(lst)):
         
        m = lst[i]
        remLst = lst[0:i] + lst[i + 1:]
         
        remainlst_combo =combo(remLst, n-1)
        print(remainlst_combo,n-1,remLst)
        for p in remainlst_combo:
            
            l.append([m, *p])
    return l
m=[1,[[]],2,3,4]
a=[]
for i in m:
    a.append([1,*i])
print(a)

