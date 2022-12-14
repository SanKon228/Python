a=int(input("A="))
b=int(input("B="))
def Shvmn(x,y):
    m=(len(str(x))//2)

    if len(str(x))==1 or len(str(y))==1:
        return x*y

    a = x // 10 ** m
    b = x % 10 ** m
    c = y // 10 ** m
    d = y % 10 ** m 
    a_c = Shvmn(a,c)
    b_d = Shvmn(b,d)
    ad_bc = Shvmn(a+b,c+d) - a_c - b_d
    res = 10**(2*m)*a_c + 10**m*ad_bc +b_d
    return res
print(Shvmn(a,b))