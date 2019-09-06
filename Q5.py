from Q5input.py import *
import string
# Your code - begin
sets=[]
c=0

def ispangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True

for i in set1:
    for j in set2:
        sets.append(i+j)

for i in sets:
    f=ispangram(i)
    if f==True:
        c+=1
# Your code - end
print sets
print c

