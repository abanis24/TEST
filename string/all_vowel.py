s = "geeksforgeeks"

v = 'aeiou'

if all(i in s.lower() for i in v):
    print('yES')
else:
    print('No')

# help(all)
