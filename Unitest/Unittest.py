def calc(expr):
    allowed ="+-/*"
    if not any( sign in expr for sign in allowed):
        raise ValueError('Хоть один знак')
    for sign in allowed:
        if sign in expr:
            try:
                l,r=expr.split(sign)
                l,r=int(l),int(r)
                if sign=="+":
                    return l+r
                elif sign=="-":
                    return l-r
                elif sign=="/":
                    return l/r
                elif sign=="*":
                    return l*r
            except(ValueError, TypeError):
                raise ValueError("Need 2 numbers and 1 sign")
                


if __name__=='__main__':
    #print(calc('4+4+4'))
    [a,b]=[4,'fred']
    print(b)