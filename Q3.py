from Q3input import *

# Your code - begin
dic={}
for i in inp:
    if i.isalpha() :
        if i not in dic:
            dic[i]=1

        else:
            dic[i]+=1

            
for i in dic:
    if dic[i]>1 :
        output = False
        break
    else:
        output= True

    
# Your code - end
print output
