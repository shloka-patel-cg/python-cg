# Q-1
i=1
while i<=5:
    print("hello")
    i+=1
# Q-2
i=0
while i<=9:
    print(i,end=" ")
    i+=1
#Q-3
i=1
while i<=10:
    print(i)
    i+=1
#Q-4
i=10
while i>=1:
    print(i)
    i=i-1
#Q-5
i=1
while i<=10:
    print(i*5)
    i+=1
#Q-6
i=2
while i<=20:
    if i%2 == 0:
        print(i)
    i+= 1  
#Q-7
i=1
while i<=19:
    if i%2 == 1:
        print(i)
    i+=1 
#Q-8
i=1
while i<=6:
    print(i*3,end=" ")
    i+=1   
#Q-9
i=20
while i>=2:
    if i%2 == 0:
        print(i,end=" ")
    i-=1    
#Q-10
n=int(input("enter the number n:"))
i=1
while i<=n:
    print(i)
    i+=1
#Q-11
n=int(input("enter the number n:"))
i=1
while i<=n:
    if i%2 == 0:
        print(i)
    i+=1 
# Q-12
n=int(input("enter the number n:"))
i=1
while i<=n:
    if i%2 == 1:
        print(i)
    i+=1  
#Q-13
n=int(input("enter the number n:"))
i=1
while i<=n:
    if i%3 == 0:
        print(i)
    i+=1
#Q-14
n=int(input("enter the number n:"))
i=1
while i<=n:
    if i%3 == 0 and i%2 == 0:
        print(i)
    i+=1
#Q-15
n=int(input("enter the number n:"))
count=0
i=1
while i<=n:
    if i%2 == 0:
        count+=1
    i+=1
print("count the even numbers:",count)
#Q-16
n=int(input("enter the number n:"))
sum=0
i=1 
while i<=n:
    sum+=i
    i+=1    
print("sum of nunber n:",sum)
#Q-17
n=int(input("enter the number n:"))
sum=0
i=1 
while i<=n:
    if i%2 == 0:
        sum+=i
    i+=1    
print("sum of even nunber n:",sum)
#Q-18
n=int(input("enter the number n:"))
sum=0
i=1 
while i<=n:
    if i%2 == 1:
        sum+=i
    i+=1    
print("sum of odd nunber n:",sum)
#Q-19
n=int(input("enter the number n:"))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1    
#Q-20
n=int(input("enter the number n:"))
result=1
i=1
while i<=n:
    result *= i
    i+=1
print(result)        
#Q-21
text=input("enter your string:")
i=0
while i<len(text):
    print(text[i])
    i+=1
#Q-22
text=input("enter your string:")
i=0
while i<len(text):
    print(text[i],end=" ")
    i+=1
#Q-23
text=input("enter your string:")
count=0
i=0
while i<len(text):
    count+=1
    i+=1
print("count the char:",count)
#Q-24
text=input("enter your string:")
count=0
i=0
while i<len(text):
    if text[i] == "a":
        count+=1
    i+=1    
print("count the number of a in string:",count)
# Q-25
text=input("enter your string:")
count=0
i=0
while i<len(text):
    if text[i].isupper():
        count+=1
    i+=1    
print("numbers of upper char in staring:",count)
#Q-26
i=1
while i<=3:
    j=1
    while j<=4:
        print("*",end="")
        j+=1
    print()    
    i+=1 
#Q-27
i=1
while i<=4:
    j=1
    while j<=4:
        print("*",end="")
        j+=1
    print()    
    i+=1