# 정수 제곱근 판별
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

import math

def solution(n):
    if n % math.sqrt(n) == 0:
        return int((math.sqrt(n)+1)**2)
    return -1

print(solution(3))
print(solution(121))

# 1. math함수의 sqrt() 메서드를 사용하여 n의 제곱근을 구한 뒤 n과 나눈 나머지 값이 0과 같다면 (n의 제곱근+1)**2를 계산 후 float 타입 -> int 타입으로 변환 후 반환.
# 2. n과 나눈 나머지 값이 0과 같지 않다면 -1을 반환

# ====================================
# def solution(n):
#     answer = 0
#     n = n / 2
#     i = 1
#     while n-i >= 0:
#         n -= i
#         i += 1
#     answer = (i+1)**2
    
#     if i != n*2:
#         answer = -1
    
#     return answer

# print(solution(3))
# print(solution(121))

# 1. 제곱근 구하는 공식 
#     121 / 2 = 60.5 -> 60.5 - 1 ~ 음수가되기 전까지의 정수
#     60.5 - 1 = 59.5 - 2 = 57.5 - 3 = 54.5 ~~ 10 = 5.5(1번의 결과 값) : 11(i)을 뺴면 음수니까 종료.
# 2. 1번의 결과값 5.5 x 2를 한 값이 더이상 뺼 수 없는 수 i와 같다면 i는 제곱근이므로 (i+1)^2를 계산 후 반환한다.
# 3. 만약 i 값이 결과값과 같지 않다면 -1을 반환한다.