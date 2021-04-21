#!/usr/bin/python3

def CountOnes(s):
    count = 0
    for i in s:
        if i=='1':
            count+=1
    return count

def DecimalToBinary(num):
    return bin(num).replace("0b", "")

n = int(input("number: "))
m = pow(n,2)

from collections import deque
arr= deque(maxlen=m)
v =deque(maxlen=m)

from collections import defaultdict
dictionary=defaultdict(list)

for i in range(m):
    arr.append(DecimalToBinary(i).zfill(n))
    k = input(arr[i]+": ").split(": ")
    v.append(k[0])
    
for key in arr:
    ones = CountOnes(key)
    for val in v:
        if val=='1':
            dictionary[ones].append(key)
        break
        
print(dictionary)
