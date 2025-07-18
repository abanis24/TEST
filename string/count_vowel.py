# In a string count no of vowels present
s = "AbaniSenapati"
s = s.lower()

vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count+=1

print(f"count of vowels present in the string is: {count}")