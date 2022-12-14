def combo(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(len(lst)):
         
        m = lst[i]
        remLst = lst[0:i] + lst[i + 1:]
         
        remainlst_combo =combo(remLst, n-1)
        for p in remainlst_combo:
             l.append([m, *p])
    return l
 
if __name__=="__main__":
    n,m = int(input()),int(input())
    lst = []
    lst2=[]
    for i in range(n):
        j=int(input("n"))
        lst.append(j)
    for i in range(m):
        j=int(input("m"))
        lst2.append(j)
    lst3=[]
    
    for i in lst:
        perek=0
        ans=0
        for j in range(0,len(lst2)):
            l=combo(lst2,j+1)
            l1=l[:]
            for x in l:
                sum=0
                for z in x:
                    sum+=z
                if sum==i:
                    perek=1
                    for a in x:
                        lst2.remove(a)   
                    break
        if perek==1:
            ans=0
        else:
            ans=1
            break
    if ans==1:
        print("No")
    else:
        print("Yes")