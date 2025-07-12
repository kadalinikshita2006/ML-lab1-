import random  
r=[random.randint(100,150) for i in range(100)] 
mean=sum(r)/len(r) 
r.sort() 
n=len(r) 
if n%2==0: 
    median=(r[n // 2 - 1]+r[n // 2])/2 
else: 
    median=r[n // 2] 
freq={} 
for num in r: 
    if num in freq: 
        freq[num]+=1 
    else: 
        freq[num]=1 
mode=max(freq,key=freq.get) 
print("mean",mean) 
print("mode",mode) 
print("median",median)