from Q4input import *

# Your code - begin
output = []
c=0
i=0
l=len(inp)
while(i<l):
	if(inp[i]==0):
		inp.remove (inp[i])
		c+=1
		l = l -1  
		continue
	i = i+1

output.extend(inp)

for i in range(c):
    output.append(0)

# Your code - end
print output
