#BUIT-IN FUNCTIONS/METHODS
#LIST=>
# len()
# list.append() 
List1=[4,6,8.9,10,6,[6,3,2,1]]
print(len(List1))
List1.append(55)
print(List1)
List1.append([90,65,78])
print(List1)
# List1.append([8,3,2,1],8) #error=>takes exactly one argument (2 given)
# print(List1)
List1.append((1,2,3))
print(List1)
print("append take only take one element\n it can append at the end of the list")

# list.extend()
List2=[4,6,8.9,10,6,[6,3,2,1]]
List2.extend([1,2,9,0,4]) 
print("it gives seperate values at the end")
print(List2)
List2.extend([[1,2,9,0,4]])
print("it give in the list type")
print(List2)
print("it is also extend at the last of list,but it can add multiple values")
# List1.extend([5,4,6],7) #error=>list.extend() takes exactly one argument (2 given)
# print(List1)

#list.insert(index,element)
List3=[1,3,6,[9,6,3],0.6,45,-9]
List3.insert(3,20)
print(List3)
List3.insert(20,99)
print("it is out of the index range so,this value insert at end of the list")
print(List3)
List3.insert(-100,111)
print("it is also out of the range so, it add value at the very start of list")
print(List3)
# List3.insert(-3,[9,0,7,6],5)
# print(List3) #TypeError: insert expected 2 arguments, got 3

#list.remove(element)
List4=[8,9,3,8,2,1,[8,9,6],0.8,50]
List4.remove(8)
print("it remove that particular value")
print(List4)
# List4.remove(8,2)#TypeError: list.remove() takes exactly one argument (2 given)
# print(List4)
# List4.remove(33)#ValueError: list.remove(x): x not in list
# print(List4)

#list.pop(index)
List5=[3,4,5,2,9,8,[6,5,4],0.6,60]
List5.pop(3)
print("it pop the value in the given index")
print(List5)
# List5.pop(10) #IndexError: pop index out of range
# print(List5)
# List5.pop(2,5)#TypeError: pop expected at most 1 argument, got 2
# print(List5)

#list.index(element)
List6=[4,5,6,8,[2,3,0],0.6,-90]
print(List6.index(5))
print("it print index of the element")
# print(List6.index(99))#ValueError: 99 is not in list

#list.index(element,start_index,end_index)
List7=[1,5,3,6,7,(7,8,9),[0,4,5],0.6]
print("index of element in the particular given range")
print(List7.index(3,1,5))
# print(List7.index(6,20,30))#ValueError: 6 is not in list
# print(List7.index(99,1,8))#ValueError: 99 is not in list

#list.reverse()
List8=[2,3,4,8,9,0,6,5,[1,2,3],99,30]
List8.reverse()
print(List8)