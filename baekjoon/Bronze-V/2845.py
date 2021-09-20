import sys

L, P = map(int, sys.stdin.readline().split())
people = list(map(int, sys.stdin.readline().split()))

for i in people:
    print(i - (L*P), end=' ')