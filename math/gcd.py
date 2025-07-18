n1 = 12
n2 = 8

# BruteForce Approach
# T.C -> O(min(n1,n2))
# gcd = 1

# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         gcd = i

# print(gcd)

# Optimal Approach
# Euclidean Algorithm
# It says the gcd of two numbers will be same even if the smaller number subtracted from the larger number 
# gcd(n1, n2) = gcd(n1-n2, n2) where n1>n2
# repeat this until any one of them becomes 0 so that the other will be your gcd.
while n1>0 and n2>0:
    if n1 > n2:
        n1 = n1 % n2
    else:
        n2 = n2 % n1

if n1 == 0:
    print(n2)
else:
    print(n1)

    