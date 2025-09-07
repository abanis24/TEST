string = "This is a python language"

s = string.split(' ')
# for i in s:
#     if len(i)%2==0:
#         print(i, end=" ")

# even_length_words = [x for x in s if len(x)%2==0]
# print(even_length_words)


even_length_words = list(filter(lambda word : len(word)%2==0, s))
print(even_length_words)
