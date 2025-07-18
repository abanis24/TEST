# s = "geeksforgeeks"
s = "gfg123"

l = any(c.isalpha() for c in s)
c = any(c.isdigit() for c in s)

if l and c:
    print("True")
else:
    print("False")