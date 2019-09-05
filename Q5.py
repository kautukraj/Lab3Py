
from Q5input import *
import string
# Your code - begin

sets=[]
flag=0
c=0
val = False
alphabet = set(string.ascii_lowercase)
for i in set1:
    for j in set2:
        sets.append(i+j)

for i in sets:
    val = set(i.lower()) >= alphabet
    if val==True:
        c+=1
# Your code - end
print sets
print c
