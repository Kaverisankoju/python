#
for i in range(1,100):
    print(i)



#
n=int(input('enter any number:'))
sum=0
for i in range(1,n+1):
 
    sum+=i
print(sum)


#
i=1
while i<=51:
    if i%2==0:
        print(i)
    i+=1



#    
n=int(input('enter any number:'))
for i in range(1,21):
    print(f"{n}x{i}={n*i}")
    
#
n=125
rev=0
sum=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    sum+=digit
    n=n//10
print(rev)
print(sum)

#
n=int(input('enter the number:'))
count=0
while n>0:
    n=n//10 
    count+=1 
print(count)

#
n=int(input('enter a number:'))
while n>0:
    n=int(input('enter the number please:'))
    if n<0:
        break;
    print(n)
    
    
    #or
    
#
while True:
    n=int(input('enter the number please:'))
    if n<0:
        break;
    print(n)
    
    
#
a,b=0,1
print('first 10 fibonacci series:')
for i in range(1,11):
    print(a, end=" ")

    a,b=b,a+b
    
    
#
n=int(input('enter a number:'))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print('it is not a prime')
            break;
    else:
       print('prime')
       
       
#
num=10
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(fact)


#
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i,end=" ")
   
   
#
while True:
    print("\nMenu:")
    print("1. Find Square of a number")
    print("2. Find Cube of a number")
    print("3. Exit")
    
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        num = int(input("Enter a number: "))
        print("Square of", num, "is", num ** 2)
        
    elif choice == 2:
        num = int(input("Enter a number: "))
        print("Cube of", num, "is", num ** 3)
        
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
    
    
#
i=1
while i<=3:
    password=input('enter your password:')
    i+=1
print(password)


#using while loop
correct_password= "kaveripython"
i=1
while i<=3:
    entered_password=input('enter your password:')
    if correct_password==entered_password:
        print('login successfully....')
        break;
    else:
        i+=1
        print('incorrect password ! please enter again:')
        

if i>3:
    print('too many chances please try after some time')
    
    
    
#using for loop
correct_password= "kaveripython"
for i in range(3):
    entered_password=input('enter your password:')
    if correct_password==entered_password:
        print('login successfully....')
        break;
    else:
        
        print('incorrect password ! please enter again:')
        

else :
    print('too many chances please try after some time')
    
    
#reverse of number
n=143
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)
    
    
#by using for loop
n="143"
rev=""
for i in n:
    rev=i+rev
print(int(rev))

#palindrome
n=121
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if rev==original:
    print('palindrome')
 
else:
     print('not a palindrome')
     
#using for loop
n=121
original=str(n)
rev=''
for i in original:
    
    rev=i+rev
    
if rev==original:
    print('palindrome')
 
else:
     print('not a palindrome')
     
     
#fibonacci by using while loop
a,b=0,1
count=0
while count<10:
    print(a,end=' ')
    a,b=b,a+b
    count+=1
    
#using for loop
a,b=0,1

for i in range(10):
    print(a,end=' ')
    a,b=b,a+b
    
#perfect  number 
n=int(input('enter the number:'))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,'is a perfect number')
else:
    print(n,'not a perfect number')
    
    
#fibonacci series by taking user input
n=int(input('enter a number:'))

a,b=0,1
count=0
print('fibonacci series:')
while count<n:
    print(a,end=' ')
    
    a,b=b,a+b
    count+=1

#non-fibonacci series
n = int(input("Enter how many non-Fibonacci numbers you want: "))
a, b = 0, 1
count = 0
num = 1

print("Non-Fibonacci numbers:")

while count < n:
    c = a + b
    while num < c:
        print(num, end=" ")
        count += 1
        if count == n:
            break
        num += 1
    a = b
    b = c
    num = c


# Wap to print nth non -Fibonacci number. {input : 10  Output : 16}
    
n = int(input("Enter the value of N: "))

a, b = 1, 2  # start from 1, 2 to avoid duplicate 1
count = 0
num = 1

while True:
    c = a + b
    while num < c:
        if num != a and num != b:  # make sure it's not a Fibonacci number
            count += 1
            if count == n:
                print("The", n, "th non-Fibonacci number is:", num)
                exit()
        num += 1
    a = b
    b = c
    num = c
    
    
# Wap to print the below series based on the input.
#Sample Inputs: enter a number: 13
#4 6 7 9 10 11 12

n = int(input("Enter a number: "))

a, b = 0, 1

print("Non-Fibonacci numbers:")

while True:
    c = a + b
    for i in range(a + 1, c):
        if i >= n:
            exit()
        print(i, end=" ")
    a = b
    b = c
    
#
i=10
while i>=0:
    print(i)
    i-=1
    
#
for i in range(-1,-11,-1):
    print(i)
    
#
i=-1
while i!=-11:
    print(i)
    i-=1
    
#
i=123
sum=0
while i>0:
    digit=i%10
    sum+=digit
    i//=10
  
print('sum of digits is:',sum)


#
n=int(input('enter a number:'))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
        
print('sum of even numbers are:',sum)

#
n=1
if n>1:
    for i in range(2,n):
         if n%i==0:
            print('it is not  prime number')
            break;
        
    else:
        print('it is prime')
else:
    print('it is a prime')
    
    
# Print prime numbers up to a given number && Wap to print the prime number between 1-100

n = int(input("Enter a number: "))
print(f"Prime numbers up to {n} are:")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # efficient check up to sqrt(num)
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


    
    
    