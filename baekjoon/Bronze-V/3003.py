import sys

import sys

S = [1, 1, 2, 2, 2, 8]
C = list(map(int, sys.stdin.readline().split()))

answer = [-(C[i] - S[i]) for i in range(6)]

print(*answer)

# S = [1, 1, 2, 2, 2, 8]
# C = list(map(int, sys.stdin.readline().split()))
# answer = []

# for i in range(6):
#     answer.append(-(C[i] - S[i]))
    
# print(*answer)