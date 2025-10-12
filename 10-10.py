#Output:a+b-c*d/e
s = "(a+b-c*(d/e))"
s1 = ""
for ch in s:
    if ch not in '()[]{}':
        s1 += ch 
    
print(s1)

#reverse of string
#method-1
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#method-2
s = 'python'
rev = ""
for ch in range(len(s)-1,-1,-1):
    rev += s[ch]
print(rev)

#method-3
def reversed_string(s):
    if len(s) == 0:
        return s
    # return  reversed_string(s[1:]) + s[0]
    return s[-1] + reversed_string(s[:-1])
s = 'python'
print(reversed_string(s))

#print first vowel which is not repeated
s = 'python programming'
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
for key,value in freq.items():
    if (key in 'aeiou') and value == 1:
        print(key)

#vowel, consonant, spaces count in a string
s = 'python programming is user friendly language'
vowels_count = 0
consonants_count = 0
spaces_count = 0
vowels = 'aeiou'
for ch in s:
    if ch in vowels:
        vowels_count += 1
    elif ch in " ":
        spaces_count += 1
    else:
        consonants_count += 1
print("vowels count is",vowels_count)
print("consonants count is",consonants_count)
print("spaces count is ",spaces_count) 


    