s = "AbaniSenapati"
s = s.lower()

d = {}
for char in s:
    if char in d:
        d[char]+=1
    else:
        d[char] = 1

list_of_dup_char = [i for i,count in d.items() if count>1]

print(list_of_dup_char)