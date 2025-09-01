#sort
#list1.sort()
#list1.sort(reverse=True)
#list1.sort(key=len) => for sort the elements according to length
#list1.sort(key=lambda l1:l1[0]) =>for list in inside a list
#list1.sort(key=lambda l1:(l1[0],li[1])) => 
# list1=['hello123','python432']
# list1.sort()
# print(list1)

#apply list operation to tuple
# tul=(2,3,4,5,-9,0.8,36,3)
# tul.append(99) #AttributeError: 'tuple' object has no attribute 'append'
# tul.extend([2,3,4]) #AttributeError: 'tuple' object has no attribute 'extend'
# tul.insert(1,6) #AttributeError: 'tuple' object has no attribute 'insert'
# print(tul.index(1,5,9)) #ValueError: tuple.index(x): x not in tuple
# print(tul.index(3))
# print(tul.count(3))
# tul.reverse() #AttributeError: 'tuple' object has no attribute 'reverse'
# tul.sort() #AttributeError: 'tuple' object has no attribute 'sort'
# tul.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'
# tul.clear() #AttributeError: 'tuple' object has no attribute 'clear'
# print(tul)

#copy=>shallow copy,deep copy

#SHALLOW COPY => if we change one thing in one list it will automitically reflect changes to second list
# l1=[1,2,3,4]
# l2=l1
# l1[0]=10
# l1.append(5)
# print(l1)
# print(l2)

# #DEEP COPY
# import copy
# l3=copy.deepcopy(l1)

#SET
#s.add()
#s.remove() #when remove element which is not in set then it throw an error
#s.discard()  #when remove element which is not in set then it is not throw an error
#s.pop()
#s.clear()
#print(s1.union(s2)) or print(s2.union(s1))
#print(s1.intersection(s2)) or print(s2.intersection(s1)) 
#print(s1.difference(s2)) is different from print(s2.difference(s1))
#print(s1.symmetric_difference(s2)) or  print(s2.symmetric_difference(s1)) 
# it returns  all elements except common elements
#subset,superset
#print(s1.issubset(s2))
#print(s1.issuperset(s2))
#print(s1.disjoint(s2))

fset1=frozenset({2,3,4,8,10,-8})
fset2=frozenset({2,99,4,1,10,-9})
# fset1.add(7) #AttributeError: 'frozenset' object has no attribute 'add'
# fset1.remove(3) #AttributeError: 'frozenset' object has no attribute 'remove'
# fset1.discard(3) #AttributeError: 'frozenset' object has no attribute 'discard'
# fset1.pop() #AttributeError: 'frozenset' object has no attribute 'pop'
# fset1.clear() #AttributeError: 'frozenset' object has no attribute 'clear'
print(fset1.union(fset2))
print(fset2.union(fset1))
print(fset1.intersection(fset2))
print(fset2.intersection(fset1))
print(fset1.difference(fset2))
print(fset1.isdisjoint(fset2))
print(fset1.issubset(fset2))
print(fset1.issuperset(fset2))
print(fset1.symmetric_difference(fset2))

