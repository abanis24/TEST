s = "geeksforgeeks_is_best"
# s = s.replace("_"," ").title()

# s = " ".join([word.casefold() for word in s.split('_')])
# print(s)

list1 = s.split("_")
# list1 = ["geeksforgeeks","is","best"]

res=" "
for word in list1:
    word = word.capitalize()
    res = res +" "+ word

print(res)