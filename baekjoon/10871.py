import sys

N, X = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if X > num[i] :
        print(num[i], end=' ')