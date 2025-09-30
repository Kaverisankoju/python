# #reverse order
# def natural_numbers(n):
#     if n < 1:
#         return
#     print(n)
#     natural_numbers(n-1)
# natural_numbers(10)

# #first n natural numbers
# def natural_numbers(n):
#     if n < 1:
#         return
#     natural_numbers(n-1)
#     print(n)
    
# natural_numbers(10)

# #even numbers in first n natural numbers 
# def natural_numbers(n):
#     if n < 1:
#         return
  
#     natural_numbers(n-1)
#     if n % 2 == 0:
#      print(n)
    
# natural_numbers(10)

# list in reverse order
# def reverse_list(li,index = None):
#     if index is None:
#         index = len(li)-1
        
#     if index < 0:
#         return
    
#     print(li[index],end=" ")
#     reverse_list(li,index - 1)
    
# li = [1,2,3]
# reverse_list(li)

# Print exponent of two numbers without using double star operator & loops

# def exponent_of_numbers(num1,num2,power,exp = 2):
#     if power == 0:
#         return
#     print(f"{num1}^{exp} = {num1 * num1}")
#     print(f"{num2}^{exp} = {num2 * num2}")
#     exponent_of_numbers(num1*num1,num2*num2, power-1,exp+1)

# num1 = 3
# num2 = 4
# exponent_of_numbers(num1,num2,3)

#Binary serach using recursion
# def binary_search(li,target,low,high):
#     if low > high:
#         return -1
#     mid = (low+high)//2
#     if li[mid] == target:
#         return mid
#     elif li[mid] < target:
#         return binary_search(li,target,mid + 1,high)
#     else:
#         return binary_search(li,target, low,mid -1)
# li = [1, 3, 5, 7, 9]
# print(binary_search(li,7,0,len(li)-1))

#max element in the list using recursion
def max_val(li):
    if len(li) == 1:
        return li[0]
    return max(li[0],max_val(li[1:]))
li = [3, 7, 2, 9, 5]
print("maximum value in the list",max_val(li))
    