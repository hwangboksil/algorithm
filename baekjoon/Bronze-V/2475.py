import sys

a = list(map(int, sys.stdin.readline().split())) # 고유번호 입력
b = 0 # 고유번호 각각 제곱 후 더한 값

for i in a:
    b += i**2
    
print(b % 10)