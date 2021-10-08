import sys

N = int(sys.stdin.readline())

for i in range(N):
    star = '*' * (i+1)
    print(star.rjust(N))