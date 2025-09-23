# print(5<<1)
# print(5>>1)

# actual_input="1234"
# i=1
# while i<=3:
#     input_num=input("enter a number:")
#     if input_num==actual_input:
#         print("Treasure chest opens")
#         break
#     else:
#         print("you have",3-i,"chances")
#         i+=1
# else:
#     print("locked")


# student_marks=[70,87,90,45,98]
# total=sum(student_marks)
# print("total marks in the list",total)
# avg_marks=total/len(student_marks)
# print("avg of marks",avg_marks)
# print("index of min marks in list",student_marks.index(min(student_marks)))

names=['ravi','karthik','ashok','akhil','rahul']
for name in names:
    print("hello!",{name})
if 'kaveri' in names:
    print("you are in party enjoy the party....")
else:
    print("you are not in party...")
count_A=sum(1 for guest in names if guest.startswith('a'))
print("number of names startswith A:",count_A)
