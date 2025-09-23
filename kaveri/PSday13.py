#DOC-8
#1.ADD AN ELEMENT TO LIST
# def add_an_element(li,a):
#     li.append(a)
#     print(li)
# li = [1,2,3]
# a = 4
# add_an_element(li,a)

#2.Remove element from set
#it removes what we want to remove exactly
# def remove_element(li,a):
#     li.remove(a)
#     print(li)
    
# li = [1,2,3,4]
# a = 3
# remove_element(li,a)

#pop will remove recent added element or last element
# def remove_element(li):
#     li.pop()
#     print(li)
    
# li = [1,2,3,4]
# remove_element(li)

#3.MAX ELEMENT IN THE LIST
# def max_value(li):
#     if len(li) == 0:
#         return 'invalid'
#     max = li[0]
#     for i in li:
#         if i > max:
#             max = i 
#     print("maximum value in the list",max)
# li =[4,7,1,9]    
# max_value(li)        
    
#4.MINIMUM IN LIST
# def max_value(li):
#     if len(li) == 0:
#         return 'invalid'
#     min = li[0]
#     for i in li:
#         if i < min:
#             min = i 
#     print("minimum value in the list",min)
# li =[4,7,1,9]    
# max_value(li)   

#5.SUM OF ALL ELEMENTS IN LIST
# def sum_of_all_elements_in_list(li):
#     sum_valu = 0
#     for i in li:
#         sum_valu += i
#     print("sum of all the elements in the list",sum_valu)
# li = [1,2,3]
# sum_of_all_elements_in_list(li)

#6.COUNT OCCURRENCEE OF AN ELEMENT
# def count_of_elements(li,input_value):
    
#     count = 0
#     for i in li:
#         if i == input_value:
#            count +=1
#     print(count)
# li = [1,2,2,3,2]
# input_value = int(input('enter a number'))
# count_of_elements(li,input_value)
    
#7.REVERSE OF LIST
# def reverse_list(li):
#     low = 0
#     high = len(li)-1
#     while low < high:
#         li[low],li[high] = li[high],li[low]
#         low +=1
#         high -=1
#     print(li)
# li= [1,2,3,4]
# reverse_list(li)

#8.Sort list=> method-1
# def sort_list(li):
#     for i in range(len(li)):
#         min_value = i
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_value]:
#                 min_value = li[j]
#         li[i],li[min_value] = li[min_value],li[i]
#     print(li)
# li = [4,1,3,2]
# sort_list(li)

# sort list=>method-2
# def sort_list(li):
#     li1 = []
#     while li:                     
#         min_val = li[0]           
#         for i in li:             
#             if i < min_val:
#                 min_val = i
#         li1.append(min_val)       
#         li.remove(min_val)       
#     print(li1)

# li = [4, 1, 3, 2]
# sort_list(li)

#9.Remove dublicates from list
# def remove_dublicates(li):
#     unique = []
#     for i in li:
#         if i not in unique:
#             unique.append(i)
#     print("after removing the dublicates from the list",unique)
# li = [1,2,3,2,3,1,4,5,6,6,4]
# remove_dublicates(li)
    
#10.Merge two lists
#Method-1
# def merge_of_two_lists(li1,li2):
#     print(li1 + li2)
# li1 = [1,2]
# li2 = [3,4]
# merge_of_two_lists(li1,li2)

#Method-2
# def list_merge(li1,li2):
#     merged = [*li1,*li2]
#     print(merged)
# li1 = [1,2]
# li2 = [3,4]
# list_merge(li1,li2)

#Method-3
# def list_merge(li1,li2):
#     li1.extend(li2)
#     print(li1)
# li1 = [1,2]
# li2 = [3,4]
# list_merge(li1,li2)

#11.Common Elements in a list
# def common_elements_of_lists(li1,li2):
#     common_elements = []
#     for i in li1:
#         for j in li2:
#             if i in li2 and j in li1:
#                 common_elements.append(i)
#                 break
#     print("common elements in the both lists",common_elements)
# li1 = [1,2,3]
# li2 = [2,3,4]
# common_elements_of_lists(li1,li2)

#12.Even numbers in a list
# def even_numbers_in_list(li):
#     even_numbers = []
#     for i in li:
#         if i % 2 ==0:
#             even_numbers.append(i)
#     print("even nubers in a list:",even_numbers)
# li = [2,3,8,33,90,56]
# even_numbers_in_list(li)
            
#13.Odd numbers in a list
# def even_numbers_in_list(li):
#     odd_numbers = []
#     for i in li:
#         if i % 2 !=0:
#             odd_numbers.append(i)
#     print("even nubers in a list:",odd_numbers)
# li = [2,3,8,33,90,56]
# even_numbers_in_list(li)

#14.Check if list is Palindrome
# def palindrome_check(li):
#     temp = li
#     rev = []
#     if li == 0:
#         return 'invalid list'
#     for i in temp:
#         while i >0:
#             digit = i%10
#             rev.append(digit)
#             i//=10
#     if li == rev:
#         print("palindrome list")
#         print("reversed list",rev)
#     else:
#         print("not a palindrome")
# li = [1,2,1]
# palindrome_check(li)

#15.Count Positive, Negative, Zero
# def count_positive_negative_zero(li):
#     positive_count = 0
#     negative_count = 0
#     zero_count = 0
#     for i in li:
#         if i > 0:
#             positive_count += 1
#         elif i == 0:
#             zero_count += 1
#         else:
#             negative_count +=1
#     print("positive count",positive_count)
#     print("negative count",negative_count)
#     print("zero count",zero_count)
# li = [1,2,3,0,-9,-7,0,3,-5,30]
# count_positive_negative_zero(li)
        
#16.find second maximum in the list
# def second_largest(li):
#     for i in range(len(li)):
#         for j in range(0,len(li)-1-i):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#     print(li)
#     print("second largest in the list",li[-2])
# li = [23,45,60,2,89,65,70]
# second_largest(li)

#17.Find Second Smallest Number in List
# def second_smallest(li):
#     for i in range(len(li)):
#         for j in range(0,len(li)-1-i):
#             if li[j] < li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]
#     print(li)
#     print("second smallest element in the list",li[-2])
# li = [20,6,8,9,20,4,3,46]
# second_smallest(li)

#18.Copy List to Another List
# def copy_of_list(li):
#     li1 = []
#     for i in li:
#         li1.append(i)
#     print(li1)
# li = [1,2,3]
# copy_of_list(li) 

#method-2
#Copy List to Another List
# li = [1,2,3]
# li1 = li.copy()
# print(li)
# print(li1)

#19. Print All Prime Numbers in List
# def primes_of_list(li):
#     if not li:
#         return 'invalid'
#     prime = []
#     for i in li:
#         if i > 1:
#             for j in range(2,int(i**0.5)+1):
#                 if i%j == 0:
#                     break
#             else:
#                 prime.append(i)
#     return prime
# li = [1, 2, 3, 4, 5] 
# print(primes_of_list(li))
        
               
#20. Replace All Zeroes with a Given Number
# def replace_zeros(li,num):
#     for i in range(len(li)):
#         if li[i] == 0:
#             li[i] = num
        
#     print(li)
# li = [0,2,0,5]
# num = -1
# replace_zeros(li,num)

#21.Check if All Elements Are Same
# def check_all_elements_same(li):
#     first = li[0]
#     for i in li:
#         if i != first:
#             return 'False'
#     else:
#         return 'True'
# li = [3,3,3,3]
# li1 = [4,3,3,3]
# print(check_all_elements_same(li))
# print(check_all_elements_same(li1))

#method-2   
# def check_all_elements_same(li): 
#     for i in range(len(li)-1):
#         if li[i] != li[i+1]:
#             return 'False'
#     else:
#         return 'True'
# li = [3,3,3,3]
# li1 = [4,3,3,3]
# print(check_all_elements_same(li))
# print(check_all_elements_same(li1))
             
#22.Find Frequency of All Elements
# li = [1,2,2,1,3]
# freq = {}
# for i in li:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1
# # for key,value in freq.items():
# #     print({f"{key}:{value}"},end=" ")
# print(freq)

#Flatten a Nested List
# def nested_to_normal_list(li):
#     li1 = []
#     for sublist in li:
#         for item in sublist:
#               li1.append(item)
#     print(li1)
# li = [[1,2],[3,4]]
# nested_to_normal_list(li)

#
def split_list_even_and_odd(li):
    even_list = []
    odd_list = []
    for i in li:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print("even list",even_list)
    print("odd list",odd_list)
li = [1,2,3,4,5,6]
split_list_even_and_odd(li)