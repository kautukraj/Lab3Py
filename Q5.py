
from Q5input import *

# Your code - begin

sets=[]
dic={}
flag=0
c=0
for i in set1:
    for j in set2:
        sets.append(i+j)

for i in sets:
    for j in i:
        if j not in dic:
            dic[j]=1

        else:
            dic[j]+=1

            
            
# Your code - end
print sets
print c
