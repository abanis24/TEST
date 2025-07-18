"""Write a function that counts the number of vowels (a, e, i, o, u) in a given string.
Input: “machine learning”
Output: 6"""

s = "machine learning"
# vowels = ['a','e','i','o','u']
vowels = 'aeiou'

count = 0
for char in s:
    if char in vowels:
        count+=1

print(count)

