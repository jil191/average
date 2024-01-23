fh = open('average.txt','w')
n = [1,34,56,78,95,34,21,67] 
i = 0 
sum = 0 
for i in n: 
    sum= sum + i 
average = sum / len(n) 
fh.write(str(average)) 
fh.close()