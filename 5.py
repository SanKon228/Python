def cow():
    a=[]
    am=int(input("Amount:"))
    k=int(input("Amount of cows:"))
    if k<=am:
        for i in range(am):
            j=int(input("Cor:"))
            a.append(j)
            a.sort()
        left = 0
        right = a[-1] - a[0] + 1
        while left < right:
            mid = (left + right)//2
            print(mid)
            cows = 1
            first = a[0]
            for i in a[1:]:
                if i - first > mid:
                    cows += 1
            if cows == k:
                left = mid+1
            else:
                right = mid
        print(left)        
    else:
        print("error")
        cow()
    
cow()

