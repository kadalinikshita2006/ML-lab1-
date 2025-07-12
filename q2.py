print("A,B -> two matrix if we cannot moutiply ,error") 
A=[[1,2,3],[1,2,3],[1,2,3]] 
B=[[4,5,6],[4,5,6],[4,5,6]] 
#checks if both len is eq 
if len(A[0])!=len(B): 
    print("error") 
#if yes multiply both matrix 
else: 
    r=[] 
    for i in range (len(A)): 
        row=[] 
        for j in range(len(B[0])): 
            total=0 
            for k in range(len(B)): 
                total+=A[i][k] * B[k][j] 
                row.append(total) 
        r.append (row) 
    for row in  r: 
        print (row)