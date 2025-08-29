#PRINT EVEN DIGITS IN THE NUMBER
#METHOD-1
def even_digits(num):
    temp=num
    even_numbers=[]
    while temp>0:
        digit=temp%10
        if digit%2==0:
            even_numbers.append(digit)
        temp//=10
    print("even digits in the number",even_numbers)
even_digits(15467)

#METHOD-2
num=int(input("enter a number:"))
temp=num
while(temp!=0):
    digit=temp%10
    if digit&1==0:
        print("even digit is",digit)
    temp//=10

#METHOD-3
n=int(input("enter a  number:"))
even_numbers=[int(ch) for ch in n if int(ch)%2==0]
print("even digits are",even_numbers)

#METHOD-4
n=int(input("enter a  number:"))
even_numbers=list(filter(lambda x:int(x)%2==0,num))
print("even digits are",even_numbers)

#METHOD-5
num = input("Enter a number: ")
print("Even digits are:", [d for d in num if int(d) % 2 == 0])

#PRIME DIGITS IN A NUMBER
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):   
        if n % i == 0:
            return False
    return True

def prime_digits(num):
    primes = []
    for digit in str(num):   
        d = int(digit)
        if is_prime(d):
            primes.append(d)
    print("Prime digits are:", primes)

prime_digits(2541379)

#PERFECT NUMBERS
#PRINTS PERFECT NUMBERS WITHIN RANGE
def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum==num
n1=int(input("enter a number between 1 to 1000:"))
for j in range(1,n1+1):
    if perfect_number(j):
        print(j,end=" ")

#CHECKS GIVEN NUMBER IS PERFECT NUMBER OR NOT
def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    print(sum," is perfect number") if sum==num else ('not a perfect number')
n1=int(input("enter any number:"))
perfect_number(n1)

#CHECKS GIVEN NUMBER IS PALINDROME OR NOT
def palindrome(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if rev==num:
        print(rev,"is a palindrome")
    else:
        print('not a palindrome')
n1=int(input("enter any number:"))
palindrome(n1)


#PRINTS ALL PALINDROME NUMBERS IN THE GIVEN RANGE
def palindrome(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    return rev==num
start_num=int(input("enter starting number:"))
end_num=int(input("enter ending number:"))
print("palindrome numbers are:")
for i in range(start_num,end_num+1):
    if palindrome(i):
        print(i,end=" ")

#PALINDROME CHECK FOR STRINGS
def palindrome(s):
    rev=""
    for i in s:
        rev=i+rev
    if s==rev:
         print(rev,"is a palindrome")
    else:
        print(rev,"is not a palindrome")
input_str=input("enter any string:")
palindrome(input_str)

#PRINTS REVERSE OF THE NUMBER
def reverse_of_number(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    print("reversed number is:",rev)
n1=int(input("enter a number:"))
reverse_of_number(n1)

#REVERSE OF THE STRING
def reverse_of_string(s):
    rev=""
    for i in s:
        rev=i+rev
    print("reversed string is:",rev)
s1=input("enter a string:")
reverse_of_string(s1)

    