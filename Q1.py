from Q1input import *

# Your code - begin
output={}
for i in l:
    if i not in output:
        output[i]=1

    else:
        output[i]+=1


# Your code - end

print output
