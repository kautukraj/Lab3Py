from Q6input.py import *
# Your code - begin
l=len(inp)
dic={}
lkey=[]
lval=[]
lval1=[]
lkey1=[]
output=[]
for i in inp:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for i in dic:
    lkey.append(i)
    lval.append(dic[i])
l1=len(lval)    
for i in range(l1):
    for j in range(l1-i-1):
        if lval[j]<lval[j+1]:
            t=lval[j]
            lval[j]=lval[j+1]
            lval[j+1]=t
            t1=lkey[j]
            lkey[j]=lkey[j+1]
            lkey[j+1]=t1
            
for i in lval: 
    if i not in lval1: 
      lval1.append(i)
      
find = lval1[N-1]

for i in dic:
    if dic[i]==find:
        lkey1.append(i)
    
output=lkey1[0]
# Your code - ends
print output
