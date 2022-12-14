def task4(array):
    print(array)
    if len(array)>1:
        m=len(array)//2
        l=array[:m]
        r=array[m:]
        task4(l)
        task4(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                array[k]=l[i]
                i+=1
            else:
                array[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            array[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            array[k]=r[j]
            j+=1
            k+=1
    print(array)
    return array
print(task4([9,2,7,1,2]))
