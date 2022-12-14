#1.1
#a)
k += 1 # 4
i = n # 2
while i < n: # 3 * (n + 1)
    i -= 1 # 4 * n

#Time = 4 + 2 + 3(n + 1) + 4n = 7n + 9

#b)
i = n # 2
while i > n: # 3 * log_2(n) + 3
k += 1 # 4 * log_2(n)
i //= 2 # 4 * log_2(n)
#
#Time = 11 log2(n) + 5


#d)
i = 0 # 2
while i < n: # 3 * (n + 1)
j = 0 # 2 * n
while j == i * i: # 5 * (n + 1)
k += 1 # 4
j += 1 # 4
i += 1 # 4 * n

#Time = 14n + 18

#e)
i = 1 # 2
while i < n: # 3 * (log_2(n) + 1)
j = 1 # 2 * log_2(n)
while j < n: # 3 * log_2(n) * (log_2(n) + 1)
k += 1 # 4 * log_2(n) * log_2(n)
j *= 2 # 4 * log_2(n) * log_2(n)
i *= 2 # 4 * log_2(n)
#Time = 11 log2^2(n) + 12 log2(n) + 5

#1.4 
#a)
#T(n) = T(n − a) + 1 = T(n − 2a) + 1 + 1 = · · · = T(n − n) + 1 + . . . + 1 =n/a+ 1.


#b)
#T(n) = T(n − 1) + 2^n = T(n − 2) + 2^(n−1) + 2n = T(n − 3) + 2^(n−2) + 2^(n−1) + 2^n = . . . = T(n − n) +
#+ 2^(n−n+1) + . . . + 2^(n−1) + 2^n = 1 + . . . + 2^n = 2^(n+1) − 1.

