s = "AbaniSenapati"
s = s.lower()
print(f"s:{s}")
d = {}
for char in s:
    d[char] = d.get(char,0)+1

print(f"d:{d}")
res = min(d, key=d.get)
print(res)

# sort the d based on count of each character and find out the least char
least_count = min(d.values())

least_char = [char for char, count in d.items() if count ==least_count]

print(f"least_char: {least_char}")
# k=2
# for char in s:
#     if d.get(char)==1:
#         k-=1
#     if k==0:
#         print(char)
