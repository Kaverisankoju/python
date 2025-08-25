#frozenset
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

#SET

# set1={1,2,3}
# set1.add(4)
# print(set1)

# set1={1,2,3,4}
# set1.remove(3)
# print(set1)
# set1.remove(5) #error
# print(set1)

# set1={1,2,3,4}
# set1.discard(3)
# print(set1)
# set1.discard(6)
# print(set1)

# set1={1,2,3,4}
# set1.pop()
# print(set1)

# set1={1,2,3,4}
# set1.clear()
# print(set1)

set1={1,2,3,4,5}
set2={3,2,4,5,6}
print(set1.union(set2))

set1={1,2,3,4,5}
set2={3,2,4,5,6}
print(set1.intersection(set2))

set1={1,2,3,4,5}
set2={3,2,4,5,6}
print(set1.difference(set2))
print(set2.difference(set1))

set1={1,2,3,4,5}
set2={3,2,4,5,6}
print(set1.union(set2))
print(set1.symmetric_difference(set2)) 
# it returns  all elements except common elements

set1={1,2,3,4,5}
set2={3,2,4,5,6}
set3={2,3,4}
print(set1.issubset(set2))
print(set3.issubset(set2))

set1={1,2,3,4,5}
set2={3,2,4,5,6}
set3={2,3,4}
print(set1.issuperset(set2))
print(set2.issuperset(set3))


set1={1,2,3,4,5}
set2={3,2,4,5,6}
set3={2,3,4}
set4={5,6,7}
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))
