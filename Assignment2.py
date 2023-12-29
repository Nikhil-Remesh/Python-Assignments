#Write a program to  create a list of fruits and copy only 'e' letter fruits to the new list
"""
fruits=["apple","mango","pineapple","banana","orange"]
e_fruits=[]
for i in fruits:
    for j in i:
        if(j=="e"):
            e_fruits.append(i)
            break        
print(e_fruits)
"""


#prime or not
flag=0
n=int(input("Enter number: "))
for i in range(1,(n//2)):
    if(n%i==0):
        flag=1
    else:
        flag=0
if(flag==1):
    print("number is not prime")
else:
    print("number is prime")
