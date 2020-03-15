# if true
# *
# **
# ***
# ****
# else
# ****
# ***
# **
# *

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#         j+=1
#     print()
print("-----------------------------------------------------------")
# k=1
# for i in range(0,n):
#     for j in range(0,k):
#         print("*",end=" ")
#     k+=2
#     print()
print("------------------------------------------------------------")
n = 5
k = 8
for i in range(0, 5):
    for j in range(0, k):
        print(end="_")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()

