from Q6input import *

# Your code - begin

l=len(inp)
dic={}
lkey=[]
lval=[]
output=[]
for i in inp:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for key, value in sorted(dic.items(), key=lambda item: item[1]):
    lkey.append(key)
    lval.append(value)

lval1=[]
lkey1=[]
for i in lval: 
    if i not in lval1: 
            lval1.append(i) 
lval1.sort(reverse=True)

find = lval1[N-1]

for i in dic:
    if dic[i]==find:
        lkey1.append(i)
    
output=lkey1[0]
# Your code - end
print output
