print("vovels and consonents") 
#ab is the string name  
ab=input("enter string") 
vowels=0 
consonents=0 
for ch in ab: 
    if ch.isalpha(): 
        if ch.lower() in'aeiou': 
            vowels+=1 
        else: 
            consonents+=1 
print("vowels",vowels) 
print("consonents",consonents)