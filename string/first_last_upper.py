s = "hello world"

s= s.split()


# result =' '.join(
#     [letter[0].upper()+ letter[1:-1]+letter[-1].upper() 
#     if len(letter)>1 else letter.upper()
#     for letter in s]
# )

# result = ' '.join(map(lambda x:x[0].upper()+x[1:-1]+x[-1].upper() 
#                       if len(x)>1 else x.upper(),s.split()))

result = ' '.join([word.capitalize() for word in s])

print(result)

