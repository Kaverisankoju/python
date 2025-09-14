#PS
#USING WHILE LOOP FIND VALUE BY USING INDEX VALUE
def number_of_list(li,index):
    if index < -len(li) or index >= len(li):
        return 'invalid'
    if index < 0:
        index = len(li) + index
    idx=0
    while idx<len(li):
        if idx == index:
            print(li[index])
        idx+=1
li=[1,2,3,4,5,6,7,8]
index=int(input('enter index number:'))
print(len(li))
number_of_list(li,index)

#method-2 with edge cases
def find_element(input_list,input_index):
    if input_index < -len(input_list) or input_index >= len(input_list):
        return 'invalid index'
    return input_list[input_index]
index = int(input('enter a index:'))
li = [2,3,8,-98,67,86,354,54]
print(find_element(li,index))

#list sum
def sum_of_list(li):
    if len(li) == 0:
        print("invalid list")
    sum_val = 0
    for i in li:
        sum_val += i
    print("sum of list is",sum_val)
li = [4,5,6,7,9,23,45,2]
sum_of_list(li)

#MAX VALUE
#list max=>method-1
def max_elem(input_list):
    if len(input_list)==0:
        #if not input_list
        #if input_list==[]
        return 'empty list'
    input_list.sort()
    return input_list[-1]
li=[6,9,34,56,78,34,99,0,23]
print(max_elem(li))

#comparing method to find max element in list=>method-2
def max_ele(list):
    if len(list)==0:
        return 'invalid list'
    max_valu = list[0]
    for i in list:
        if i > max_valu:
            max_valu = i 
    print("maximum value in the list is:",max_valu)
list=[66,90,34,22,56,90,54,36]
max_ele(list)

#max = 0 (value)
def max_ele(list):
    if len(list)==0:
        return 'invalid list'
    max_valu = 0
    for i in list:
        if i > max_valu:
            max_valu = i 
    print("maximum value in the list is:",max_valu)
list=[66,90,34,22,56,90,54,36]
max_ele(list)

# takes any other index value except first index
def max_ele(list):
    if len(list)==0:
        return 'invalid list'
    max_valu = list[3]
    for i in list:
        if i > max_valu:
            max_valu = i 
    print("maximum value in the list is:",max_valu)
list=[66,111,90,34,22,56,90,9,54,36]
max_ele(list)

#MIN VALUE
#min element =>method-1
def min_elem(input_list):
    if len(input_list) == 0:
        return 'invalid'
    input_list.sort()
    return input_list[0]
li=[-6,98,76,54,90,-56,43,24]
print(min_elem(li)) 

#method-2
def min_value(input_list):
    if len(input_list) == 0:
        return 'invalid'
    min_val=input_list[0]
    for i in input_list:
        if i < min_val:
            min_val=i
        return f"min value is:{i}"
li1=[-100,89,0,45,67,39,-10,35]
print(min_value(li1))


#min takes as value like min=0
def min_value(input_list):
    if len(input_list) == 0:
        return 'invalid'
    min_val = 0
    for i in input_list:
        if i < min_val:
            min_val=i
        return f"min value is:{i}"
li1=[-100,89,0,45,67,39,-10,35]
print(min_value(li1))
        
#random index value within the range except first
def min_value(input_list):
    if len(input_list) == 0:
        return 'invalid'
    min_val = input_list[3]
    for i in input_list:
        if i < min_val:
            min_val=i
    return f"min value is:{i}"
li1=[-10,89,0,45,-100,67,39,-10,35]
print(min_value(li1))   #it does not work
        
#code for 3 conditions like sum,min,max in single code and handle all edge cases in functions
def sum_min_max(input_list):
    if len(input_list)==0:
        return 'invalid'
    max_value=input_list[0]
    min_value=input_list[0]
    sum_val=0
    for i in input_list:
        sum_val+=i
        if i >  max_value:
            max_value = i
        if i < min_value:
            min_value = i    
    print("sum of the values in the list",sum_val)
    print("maximum value in list",max_value)
    print("minimum value in the list",min_value) 
li=[45,60,-90,0,23,35,4,6,99,30]
li1=[]
sum_min_max(li)
print(sum_min_max(li1))

#start with 0 
# mx=0
# mi=0
# li[0] 
# li[4]


