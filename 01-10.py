#ASSIGNMENT

#EASY
#1. Check if a number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        print(n,"is even")
    else:
        print(n,"is odd")
n = int(input("enter a number:"))
check_even_odd(n)

#2. Find the maximum and minimum element in a list.
def max_min_element(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
        max = li[0]
        min = li[-1]
    print(li)
    print("maximum value is",max)
    print("minimum value is",min)
li = [2,7,9,10,4,6,8,3]
max_min_element(li)

#3. Reverse a string without using slicing ([::-1] ).
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    print("reversed string is",rev)
s = 'python'
reverse_string(s)

#4. Check if a string is a palindrome.
def palindrom_check(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    if rev == s:
        print("given string is palindrome")
    else:
        print("not a palindrome")
s = 'madam'
palindrom_check(s)

#5. Find the factorial of a number (using loop).
def factorial_number(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(f"factorial of {n} is {fact}")
n = 5
factorial_number(n)

#6. Count the frequency of each character in a string.
def freq_of_characters(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
            
    print(freq)
s = 'python programming'
freq_of_characters(s)

#7. Find the second largest number in a list.
def second_large_number(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    
    second_largest = li[-2]
    print(li)   
    print("second largest numbers in the list",second_largest)
    
li = [2,7,9,10,4,6,8,3]
second_large_number(li)

#8. Count how many vowels and consonants are in a string.
def count_of_vowels_and_consonants(s):
    vowels = 'aeiouAEIOU'
    vowels_count = 0
    consonants_count = 0
    for ch in s:
        if ch in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    print("vowel count",vowels_count)
    print("consonants count",consonants_count)
s = 'hello world'
count_of_vowels_and_consonants(s)

#9. Calculate the sum of digits of a number.
def sum_of_digits(n):
    sum_val  = 0
    while n > 0:
        digit = n % 10
        sum_val += digit
        n //= 10
    print("sum of digits in the number:",sum_val)
n = 333
sum_of_digits(n)            
            
#10. Print the multiplication table of a number.
def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
n = 3
multiplication_table(n)

#11. Find the largest word in a given sentence.
def max_length_of_string(li):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if len(li[j]) > len(li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
    
    print(li)
    print("maximum length of string",li[-1])
    
li = ['hello','hi','python','java','os','programming']
max_length_of_string(li)

#12. Remove all duplicate elements from a list.
def remove_dublicates(li):
    unique = []
    for i in li:
        if i not in unique:
            unique.append(i)
    print("after removing the dublicates in the list",unique)
li = [1,1,1,2,3,2,4,3,5,6,6,5,4]
remove_dublicates(li)

#13. Sort a list without using Python’s built-in .sort() .
def sort_the_list(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    print(li)
li = [2,10,14,25,70,6,33]
sort_the_list(li)

#14. Merge two lists into a single sorted list.
def two_list_sort_into_single_list(li1,li2):
    merged_list = li1+li2
    for i in range(len(merged_list)-1):
       for j in range(len(merged_list)-1-i):
           if merged_list[j] > merged_list[j+1]:
               merged_list[j],merged_list[j+1] = merged_list[j+1],merged_list[j]
    print(merged_list)
li1 = [55,78,90]
li2 = [32,30,4]
two_list_sort_into_single_list(li1,li2)

#15. Check if a number is a prime number.
def check_prime(n):
    if n < 2:
        return 'invalid number'
    for i in range(2,int(n*0.5)+1):
        if n % i == 0:
            return 'not a prime'
    return 'prime'
n = 3
print(check_prime(n))

#MEDIUM
#1. Find all pairs in a list that sum up to a target value.
def sum_of_numbers(li):
    target = 9
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i] + li[j] == target:
                print(f"{li[i]} + {li[j]} = {target}")
    print('no such pairs are present in the list to get target')
li = [3,6,9,1,0,2,2,5,16,20,30]
sum_of_numbers(li)

#2. Implement a program to rotate a list by k positions.
def roated_list(li):
    n = len(li)
    k = 2
    rotated = []
    for i in range(len(li)):
        rotated.append(li[(i+n-k)%n])
    print(n)
    print("after 2 steps rottion",rotated)
li = [1,2,3,4,5]
roated_list(li)

#3. find the missing number in a list of consecutive integers.
def missing_number_in_list(li):
    n = len(li) + 1
    total_sum = n * (n + 1) //2
    actual_sum = sum(li)
    return total_sum - actual_sum
li = [1,2,3,5,6]
print(missing_number_in_list(li))

#4. Check if two strings are anagrams.
def anagrams_check(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    if sorted(str1) == sorted(str2):
        return 'Anagram'
    return 'not a anagram'
print(anagrams_check('listen','silent'))

#
def anagrams_check(str1,str2):
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)
print(anagrams_check('listen','silent'))

#5. Count the number of words in a sentence.
def count_words_in_sentence(s):
    count = 0
    in_word = False
    for ch in s:
        if ch.isalnum():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count
s = 'Python is an amazing programming language'
print(count_words_in_sentence(s))

#6. Remove all duplicate words from a sentence.
def remove_dublicate_words(s):
    words = s.split()
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return " ".join(result)
s = 'Python is great and Python is easy'
print(remove_dublicate_words(s))

#7. Given a dictionary, invert it (keys become values).
def inverted_dict(dict):
    inverted = {}
    for key,value in dict.items():
       inverted[value] = key
    print(inverted)
dict = {"a":1 ,"b":2,"c":3}
print(inverted_dict(dict))

#8. Find the intersection of two lists.
def intersection_of_two_lists(li1,li2):
    intersection = []
    for val in li1:
        if val in li2:
            intersection.append(val)
    print("intersection:",intersection)
li1 = [1,2,3,9,30,90,24]
li2 = [3,60,36,1,2]
intersection_of_two_lists(li1,li2)
        
#method-2
def intersection_list(li1,li2):
    return [x for x in li1 if x in li2]
li1 = [1,2,60]
li2 =  [30,60,1]
print(intersection_list(li1,li2))             
 
#9. Print the transpose of a matrix.
def transpose_of_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()
matrix = [
    [1,2,3],
    [4,5,6],
    [5,6,7]
]
transpose_of_matrix(matrix)

#10. Implement bubble sort.
li = [4,1,30,96,43,24,67,89,90]
for i in range(len(li)):
    for j in range(len(li)-1-i):
        if li[j] > li[j+1]:
            li[j],li[j+1] = li[j+1],li[j]
print(li)

#              
def bubble_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
     
    print(li)
li = [4,1,30,96,43,24,67,89,90]
bubble_sort(li)
             
#11. Find the first non-repeating character in a string.
def first_non_repeating_character(s):
    for ch in s:
        if s.count(ch) == 1:
            print(ch)
            break
s = 'programming'
first_non_repeating_character(s)

#12. Find the longest word in a sentence.
def largest_word_in_sentence(s):
    words = s.split()
    largest_word = s[0]
    for word in words:
        if len(word) > len(largest_word):
            largest_word = word
    print(largest_word)
s = 'Python is a very powerful programming language'
largest_word_in_sentence(s)

#13. Find the second smallest number in a list.
def second_smallest_num(li):
    for i in range(len(li)):
        for j in range(len(li)-1-i):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    print(li)
    print(li[1])
li = [10, 5, 20, 3, 7]
second_smallest_num(li)

#14. Implement a program to check if a number is an Armstrong number.
def check_amstrong(n):
    
    len_n = len(str(n))
    sum_val = 0
    temp = n
    while temp > 0:
        digit = temp%10
        sum_val += digit ** len_n
        temp //= 10
    if sum_val == n:
        return 'amstrong'
    return 'not a amstrong'
n = 153
print(check_amstrong(n))
 
#       
def check_amstrong(n):
    
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 10
    print(count)
    sum_val = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** count
        temp //= 10
    if sum_val == n:
        return 'amstrong'
    return 'not a amstrong'
n = 153
print(check_amstrong(n))
        