#SUM OF DIGITS
def sum_of_digits(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    print('sum of digits is',sum)
n=int(input('enter a number:'))
sum_of_digits(n)

#COUNT OF DIGITS
def number_of_digits(n):
    count=0
    while n>0:
        count+=1
        n//=10
    print('number of digits is',count)
n=int(input('enter a number:'))
number_of_digits(n)

#REVERSE OF NUMBER
def reverse_of_number(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    print("reserved number",rev)
n=int(input('enter a number:'))
reverse_of_number(n)

# #PALINDROME CHECK
def reverse_of_number(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if temp==rev:
        print(temp,"is palindrome")
    else:
        print(temp,"is not palindrome")
n=int(input('enter a number:'))
reverse_of_number(n)

# #PERFECT NUMBER
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
       print(n,'is perfect number')
n=int(input('enter a number:'))
perfect_number(n)

# #PERFECT SQUARE
n=int(input('enter a number:'))
if n%(n**0.5)==0:
    print('perfect square')
else:
    print('not perfect')

# #sunny number
import math
n = int(input("Enter a number: "))
n1 = n + 1
sqrt_n1 = int(math.sqrt(n1))
if sqrt_n1 * sqrt_n1 == n1:
    print(n, "is a Sunny number")
else:
    print(n, "is not a Sunny number")

# #HARSHED NUMBER  
n=int(input('enter a number:'))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
if n%sum==0:
    print('harshed number')
else:
    print('not a harshed number')

# #NEON NUMBER    
n=int(input('enter a number:'))
square=n*n
digit_sum=0
while square>0:
    digit=square%10
    digit_sum+=digit
    square//=10  
if n==digit_sum:
    print('neon number')
else:
    print('not a neon number')
    
# #AUTOMARPHIC NUMBER
n=int(input('enter a number:'))
square=n*n
temp=n
digit=0
while temp>0:
    digit+=1
    temp//=10
last_digit=square%(10**digit)
if n==last_digit:
    print('automarphic')
else:
    print('not a automarphic')
        
# #SPY NUMBER
n=int(input('enter a number:'))
sum=0
prod=1
while n>0:
    digit=n%10
    sum+=digit
    prod*=digit
    n//=10
if sum==prod:
    print('spy number')
else:
    print('not a spy number')