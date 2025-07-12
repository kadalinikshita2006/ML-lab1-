print("common elements in lists") 
l1=[1,2,3] 
l2=[2,3,4] 
s1=set(l1) 
s2=set(l2) 
common=s1.intersection(s2) 
count=len(common) 
print("common elements",count)