#TEST
# print prime numbers in the given number 
n=23579812
primes=[]
while n>0:
    digit=n%10
    if digit>2:
        is_prime=True
        for i in range(2,int(digit**0.5)+1):
            if digit%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(digit)
    n//=10
print(primes)
     
#2. print VenkataNarayanaBattula
s='venkata_narayana_battula'
result=""
i=0
while i<len(s):
    if i==0 or s[i-1]=='_':
        if 'a'<=s[i]<='z':
            result+=chr(ord(s[i])-32)
    elif s[i]!='_':
        result+=s[i]
    i+=1
print(result)


#3 print WHO
s='World Health Organisation'
result=""
i=0
while i<len(s):
    if i==0:
          result+=s[i]
    elif s[i-1]==" ":
        result+=s[i]
    i+=1
print(result)
    
#Strong number
n=145
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    n//=10
if temp==sum:
    print('strong num')
else:
    print('not a strong number')
    
#