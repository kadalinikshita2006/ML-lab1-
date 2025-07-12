print("give the transpose") 
m=[[1,2,3],[4,5,6]] 
tr=[] 
for i in range(len(m[0])): 
    row=[] 
    for j in  range(len(m)): 
        row.append(m[j][i]) 
    tr.append(row) 
print("transpose:",tr)