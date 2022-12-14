2.13
a)
T(n) = T(n−1)+O(1) = T(n−1)+C·(1) = T(n−2)+C·(2) = . . . = T(n−n)+C·n = C·n+1 = O(n).
2.14
a)
res = 0 # O(1)
for i in range (0, n + 1): # O(n)
res += i # O(n)

Time = O(n)

b)
res = 0 # O(1)
for i in range (0, n + 1): # O(n)
res += i*i # O(n)
Time = O(n)
c)
res = 0 # O(1)
a0 = 1 # O(1)
for i in range (0, n + 1): # O(n)
res += a0 # O(n)
a0 *= a # O(n)
Time = O(n)
d)
res = 0 # O(1)
for i in range (1, n + 1): # O(n)
a = 1 # O(n)
for j in range (1, i + 1): # O((n+1)*(n+2)/2) = O(n^(2))
a *= i # O(n^{2})
res += a # o(n)

Time = O(n^2)=11 + 2 + 3 + . . . + n + n + 1 =((n + 1)(n + 2))/2
