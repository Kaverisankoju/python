#LIST REVERSE
#method-1:using-built in 
li=[3,45,67,89,46,30]
li.reverse()
print(li)

#method-2:slicing
li=[3,45,67,89,46,30]
li=li[::-1]
print(li)

#method-3: use insert(index,element)
li=[3,45,67,89,46,30]
li1=[]
for i in li:
    li1.insert(0,i)
print(li1)

#method-4:using index
li=[3,45,67,89,46,30]
for idx in range(len(li)-1,-1,-1):
    print(li[idx],end=" ")

#method-5:using append
li=[3,5,97,90,35]
new_list=[]
for i in range(len(li)-1,-1,-1):
    new_list.append(li[i])
print(new_list)



#method-6:without using extra list(use two pointer approch)
#two pointer approch-> when we use 2 variables 
li=[3,45,67,89,46,30]
low=0
high=len(li)-1
while low<high:
    li[low],li[high]=li[high],li[low]
    low +=1
    high -=1
print(li)    #inplace reverse

#1st half reverse 2nd constant
li=[65,87,90,34,56,20,30]
low=0
high=len(li)//2
while low < high:
    li[low],li[high]= li[high],li[low]
    low +=1
    high -=1  
print(li)


#2nd half reverse and 1st half contant
li=[65,87,90,34,56,20,30]
low = len(li)//2
high = len(li)-1
while low < high:
    li[low],li[high] = li[high],li[low]
    low +=1
    high -=1
print(li)


#ASSIGNMENT Q'S
#reverse a string =>above all approches
#Method-1 
s='python'
s=s[::-1]
print(s)

#Method-2
s='python'
rev=""
for ch in s:
    rev = ch+rev
print(rev)

#Method-3
s='python'
new_s=[]
for ch in s:
    new_s.insert(0,ch)
print(new_s)

#Method-4
s='python'
for idx in range(len(s)-1,-1,-1):
    print(s[idx],end=" ")

#Method-5
s = 'python'
new_s=[]
for idx in range(len(s)-1,-1,-1):
    new_s.append(s[idx])
print(new_s)

#Method-6
s = 'python'
low = 0
high = len(s)-1
while low < high :
    s[low],s[high] = s[high],s[low]
    low +=1
    high -=1
print(s) #error:'str' object does not support item assignment


#sum of digits in the list output should be in the list
li=[356,123,341,89,14,16]
sum_value_li=[]
for i in li:
    sum_value = 0
    while i > 0:
        digit = i%10
        sum_value +=digit
        i //=10
    sum_value_li.append(sum_value)
print("sum of digits of each number in the list",sum_value_li)

#123 find max element in the number
n=563
max=0
while n>0:
    digit = n%10
    if digit > max:
        max = digit
    n //=10
print("maximum element in the number:",max)


#find max digit for every number in the given list[23,45,67]=>[3,5,7]
li = [23,45,67,89,30,43]
max_val=[]
for i in li:
    max = 0 
    while i > 0 :
        digit = i%10
        if digit > max:
            max = digit
        i //=10
    max_val.append(max)
print("max element in the each number in the list",max_val)
        

    
