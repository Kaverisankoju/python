# s='ABC'
# print(s[0]+s[1]+s[2])
# print(s[0]+s[2]+s[1])
# print(s[2]+s[0]+s[1])
# print(s[1]+s[2]+s[0])
#PRINT ABC,ACB,CAB,BCA
s='ABC'
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            k=3-(i+j)
            word = s[i] + s[j] + s[k]
            if word in ["ABC", "ACB", "CAB", "BCA"]:
                print(word)
print()
#check given is a number circular prime or not 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
n = 197
s = str(n)
rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
if all(is_prime(num) for num in rotations):
    print(rotations, "are circular primes")
else:
    print(rotations, "are not circular primes")

# s='197'
# for i in range(len(s)):
#     # print(s[i:])
#     print(s[:i])
    