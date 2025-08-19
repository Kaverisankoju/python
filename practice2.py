#sum of non prime numbers(ex:3239=o/p:9)
n = int(input("Enter a number: "))
sum_non_prime=0
while n>0:
    digit=n%10
    if digit not in [2,3,5,7]:
        sum_non_prime+=digit
    n//=10
print('sum of non-prime is:',sum_non_prime)

#sum of odd-numbers (ex:1456=>o/p:6)
n = int(input("Enter a number: "))
sum_odd_digit=0
while n>0:
    digit=n%10
    if digit not in [2,4,6,8,0]:
        sum_odd_digit+=digit
    n//=10
print('sum of odd-digits is:',sum_odd_digit)

# Wap to check whether a number is prime or not by using a function.
#Additional print a prime numbers up to 20.

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input('enter a number:'))
if is_prime(num):
    print(num,'it is prime')
else:
    print(num,'it is not a prime')
    
print('prime numbers up to 20:')
for i in range(2,21):
    if is_prime(i):
        print(i,end=" ")
#Amstrong check
num=int(input('enter a number:'))
original=num
result=0
digits=len(str(num))
while num>0:
    digit=num%10
    result+=digit**digits
    num//=10
if result==original:
    print(result,'is an amstrong number')
else:
    print(result,'is not an amstrong number')

# Armstrong numbers in a given range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print(f"Armstrong numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num, end=" ")
#Wap to check whether minimum is first or maximum is first.
#Sample inputs:6381                              	input : 7198
#output: min is first                           	output: max is first

num = input("Enter a number: ")
digits = [int(d) for d in num]

min_digit = min(digits)
max_digit = max(digits)

min_index = digits.index(min_digit)
max_index = digits.index(max_digit)

if min_index < max_index:
    print("min is first")
elif max_index < min_index:
    print("max is first")
else:
    print("min and max are at the same position")

#Wap to print the minimum prime digit in a number

num=int(input('enter a number:'))
prime_digit=[]
while num>0:
    digit=num%10
    if digit in [2,3,5,7]:
        prime_digit.append(digit)
    num//=10
if prime_digit:
    print('minimum prime digit is:',min(prime_digit))
else:
    print('no prime digits are found')
    
#Wap to print nearest prime number to the given input
#Sample inputs: 8                       	input: 21
#output: 7              	output: 19,23

# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# Get input
n = int(input("Enter a number: "))

# Search lower and higher primes
lower = n - 1
while lower >= 2 and not is_prime(lower):
    lower -= 1

higher = n + 1
while not is_prime(higher):
    higher += 1

# Compare distances
low_diff = abs(n - lower)
high_diff = abs(higher - n)

if low_diff < high_diff:
    print("Nearest prime:", lower)
elif high_diff < low_diff:
    print("Nearest prime:", higher)
else:
    print("Nearest primes:", lower, "and", higher)
    
#Sum of elements in a List.

list1=[6,8,9,3,4]
sum=0
for i in list1:
    sum+=i
    
print('sum of the digits in the list is:',sum)

#Finding the k Element which is present in a List.

list1=[6,8,9,5,3,4]
k=int(input('enter the searching element in the list:'))
found=False
    
for i in range(len(list1)):
     if list1[i]==k:
          print('u r serching value found at index:',i)
          found=True
if not found:
     print(f'{k} is not found in the list')
     
# Wap to print duplicates and unique numbers in an array/List.

list1=[5,6,3,2,2,3,8,3,9]
unique_values=[]
dublicate_values=[]
for i in list1:
    if list1.count(i)==1:
        unique_values.append(i)
    elif i not in dublicate_values:
        dublicate_values.append(i)
print('unique values in the list are:',unique_values)    
print('dublicat values in the list are:',dublicate_values)

#Find Unique and Duplicate Digits and If only one digit is duplicated,
#output: Duplicate is X.
#If multiple digits are duplicated, output: Duplicates are X, Y, ....
#input :1214
#output: 2,4
#output: duplicate is 1

num=input('enter the number:')
digit=list(num)
unique_digits=[]
duplicate_digits=[]

for d in digit:
    if digit.count(d)>1:
        if d not in duplicate_digits:
            duplicate_digits.append(d)
    else:
        unique_digits.append(d)
print("Unique digits are:", ", ".join(unique_digits))

if len(duplicate_digits)==1:
    print(f'duplicate digits is {duplicate_digits[0]}')
elif len(duplicate_digits)>1:
     
    print('duplicate digits are:', ', '.join(duplicate_digits))
else:
    print('their is no duplicate digits ')
#Count Occurrences of Each Digit
#input: 2788
#output: 2=> 1
#7=> 1
#8=> 2

num=input('enter a number:')
digits=list(num)
count_dict={}
for d in digits:
    if d in count_dict:
        count_dict[d]+=1
    else:
        count_dict[d]=1
for key in sorted(count_dict.keys()):
    print(f"{key}=>{count_dict[key]}")
#Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
#Input: [202,89,112,88]       	Output:[true ,false ,true ,true]

def has_duplicate_digits(num):
    digits = list(str(num))
    return len(digits) != len(set(digits))  # True if duplicates exist

# Input list
numbers = [202, 89, 112, 88]

# Output list
result = []

for n in numbers:
    result.append(has_duplicate_digits(n))

print("Output:", result)
#Wap that takes an array of integers as input and calculates the sum of the digits of each number in the list.
#Input: [202,89,112,88]       	Output: [4,17,14,6]

# Function to calculate digit sum of a number
def digit_sum(num):
    return sum(int(d) for d in str(num))

# Input list
numbers = [202, 89, 112, 88]

# Result list to store digit sums
result = []

for n in numbers:
    result.append(digit_sum(n))

# Output result
print("Output:", result)
#Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
#Input: [568,89,112,88,571] 	Output: [true,true ,false,false ,false]

def is_increasing(num):
    digits = list(str(num))  # Convert number to list of digits
    return digits == sorted(digits)  # Check if digits are in increasing order

# Input list
numbers = [568, 89, 112, 88, 571]

# Result list
result = []

for n in numbers:
    result.append(is_increasing(n))

# Output result
print("Output:", result)
#Wap to check if the digits of each number in an list are in decreasing order and return an array of true otherwise false.Decreasing order -true
#Input: [538,111,200,652,]   	Output: [false,false,false,true]

# Function to calculate digit sum of a number
def is_decreasing(num):
    digit=list(str(num))
    return digit==sorted(digit,reverse=True)

# Input list
numbers = [202, 89, 112, 87]

# Result list to store digit sums
result = []

for n in numbers:
    result.append(is_decreasing(n))

# Output result
print("Output:", result)
#Find the missing numbers.
#Input: 34571  	Output : 26 missing

num = input("Enter a number: ")
all_digits = set("0123456789")
present_digits = set(num)

missing_digits = sorted(all_digits - present_digits)

print("Missing digits:", " ".join(missing_digits))

#Find Largest & Smallest element in an list.

n=[3,5,6,8,9,2,1]
largest=max(n)
smallest=min(n)
print('highest number is:',largest)
print('lowest number is:',smallest)

#Find Second Largest and Third Largest Element in list.
n=[3,5,6,8,9,2,1]
sorted_list=sorted(set(n),reverse=True)
if len(sorted_list)>=3:
    print('sencond largest number is :',sorted_list[1])
    print('third largest number is :',sorted_list[2])
else:
    print('no longer values are have in the list')

#)Find Second Smallest and Third Smallest in list.
n=[3,5,6,8,9,2,1]
sorted_list=sorted(set(n))
if len(sorted_list)>=3:
    print('sencond smallest number is :',sorted_list[1])
    print('third smallest number is :',sorted_list[2])
else:
    print('no longer values are have in the list')

#Reverse an Array.

arr=[3,5,6,8,9,2,1]
arr.reverse()
print('reversed array is:',arr)

#sorted of array index

arr = [20, 15, 26, 2, 98, 6]
# Sort and remove duplicates to get the rank order
sorted_arr = sorted(set(arr))
# Assign ranks starting from 1
ranked = [sorted_arr.index(x) + 1 for x in arr]
print("Output:", ranked)


# Finding the frequency of elements in an array.
#arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2

arr=[10,20,10,30,40,30,60,30,40]
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in sorted(freq):
    print(f"{key} => {freq[key]}")

# arrange first half in ascending order and second half in descending order
#input: 8 7 1 6 5 9       	output: 1 5 6 9 8 7

arr=[9,3,9,0,5,6,2]
n=len(arr)
mid=n//2
first_sorted=sorted(arr[:mid])
second_sorted=sorted(arr[mid:], reverse=True)
result=first_sorted+second_sorted
print(result)

#check if array is subset of another array or not 

arr1 = [1, 3, 4, 5, 2]
arr2 = [2, 4, 3, 1, 7, 5, 15]
# Check if all elements of arr1 are in arr2
if all(elem in arr2 for elem in arr1):
    print("arr1 is subset of arr2")
else:
    print("arr1 is not subset of arr2")
    
#Wap to print the number of pairs formed by the array of elements
#Input: 10 20 10 30 20 20   Output: 2 pairs

arr = [30, 50, 30, 50, 20, 50, 50, 20, 50, 50]

freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1

total_pairs = 0
for count in freq.values():
    total_pairs += count // 2

print("Output:", total_pairs, "pairs")

#ind all symmetric pairs in array
#inp: (1,2),(2.1),(3,4),(4,5,),(5,4)	output: (1,2)(4,5)

inp = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
seen = set()
symmetric_pairs = []

for a, b in inp:
    if (b, a) in seen:
        symmetric_pairs.append((min(a, b), max(a, b)))
    else:
        seen.add((a, b))
# Remove duplicates and print
unique_pairs = list(set(symmetric_pairs))
for pair in unique_pairs:
    print(pair, end=' ')
    
#transpose matrix
matrix =[
    [1,1,1],
    [2,2,2],
    [3,3,3]
    ]
transpose=[list(row) for row in zip(*matrix)]
print("transposed matrix:")
for row in transpose:
    print(*row)










