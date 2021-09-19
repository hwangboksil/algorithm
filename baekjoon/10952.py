import sys

while True :
    A, B = map(int, sys.stdin.readline().split())
    if (A and B) == 0 :
        break
    else :
        print(A+B)

# A = 1
# B = 1

# while A != 0 and B != 0 :
#     A, B = map(int, sys.stdin.readline().split())
#     if A+B == 0 :
#         pass
#     else :
#         print(A+B)