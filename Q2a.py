from Q2input import *

# Your code - begin
output = {}
for i in Dic1:
    output[i]=Dic1[i]
    
for i in Dic2:
    if i not in output:
        output[i]=Dic2[i]
    else:
        output[i]+=Dic2[i]
        
    

# Your code - end
print output
