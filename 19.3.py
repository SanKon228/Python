if __name__ == "__main__":
    with open("input.txt") as f:
        n = 7
        arr = [3,10,5,12,11,6,7]

        heap = True
        for i in range(1,n//2+1):
            if 2*(i)+1<=n:
                if arr[i]>arr[2*(i)+1]:
                    heap = False
                    break
                
            if 2*(i)<=n:
                if arr[i]>arr[2*(i)]:
                    heap = False
                    break
            


        if heap:
            print('YES')
        else:
            print('NO')
