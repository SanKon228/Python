import math
def sol(f,c,a,b):
    left=a
    right=b
    n=(right+left)/2
    while right != n and left != n:
        val=f(n)
        print(val)
        if val<c:
            left=n
        else:
            right=n
        n=(right+left)/2
    print(right,left,n)
    return left
        
eps = 0.000000001
def task5():
    f = lambda x: x**3+4*x**2+x-6
    a = 0
    b = 2
    c = 0
    r = sol(f, c, a, b)
    print(r)
task5()
