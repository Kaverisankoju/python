#sum of elements in the nested list
#find missing elemensts in the number
#shocks 
#Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'], how many days can I sustain if I can wear only one matching pair of socks per day and each pair can be used only once?"
li = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
days = 0
sock_count = {}
for color in li:
    sock_count[color] = sock_count.get(color,0)+1
print(sock_count)
    
for color in sock_count:
    days += sock_count[color]//2
print("number of days ",days)

#finding missing elements in the number
n = 34571
li = []
while n>0:
    digits = n%10
    li.append(digits)
    n //=10
print(li)
max_val = max(li)
min_val = min(li)
for i in range(min_val,max_val+1):
    if i not in li:
        print(i,"missing")
#matrix addition using range
matrix = [
    [1,2,3],
    [2,3,4],
    [1,1,3]
]
sum_val = 0   
for row in range(len(matrix)):
    for num in range(len(matrix[row])):
        sum_val += matrix[row][num]
print("sum of matrix",sum_val)