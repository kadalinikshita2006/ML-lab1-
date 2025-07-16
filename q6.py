import numpy as np
A=np.array([[20,6,2],[16,3,6],[27,6,2],[19,1,2],[24,4,2],[22,1,5],[15,4,2],[18,4,2],[21,1,4],[16,2,4]])
#vector c
C=np.array([386,289,393,110,280,167,271,274,148,198])
#dimentionality
dimentionality=A.shape[1]
#num=number of vectors in vector space 
num=A.shape[0]
rank=np.linalg.matrix_rank(A)
#pseudo inverse ->cost
A_pinv=np.linalg.pinv(A).dot(C)
print("dimentionality: ",dimentionality)
print("number of vectors :",num)
print("Estimated costs:")
print(f"Candies: Rs {A_pinv[0]:.2f}")
print(f"Mangoes: Rs {A_pinv[1]:.2f}")
print(f"Milk Packets: Rs {A_pinv[2]:.2f}")