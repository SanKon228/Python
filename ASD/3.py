def binaryToDecimal(binar):
    binary=int(binar)
    print(binary)
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10

        decimal = decimal + dec * pow(2, i)
 
        binary = binary//10

        i += 1
    return(decimal) 
n=bin(int(input("n=")))
mass=[]
for i in n:
    if i!='b':
        mass.append(i)
print(mass)
mass.pop(0)
print(mass)
new=""
max=0

for i in range(len(mass)):
    a=mass.pop(0)
    mass.append(a)
    for i in mass:
        new+=str(i)
    val=binaryToDecimal(new)
    if val > max:
        max=val
    new=""
print(max)
