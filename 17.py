def binary(l):
    if len(l)==1:
        print("yes")
        return 
    if l[0]>l[1] and l[0]==max(l):
        binary(l[1:])
    elif l[0]<l[1] and l[0]==min(l):
        binary(l[1:])
    else:
        print("no")
        return
binary([5,1,3,2])
binary([5,2,3,1])