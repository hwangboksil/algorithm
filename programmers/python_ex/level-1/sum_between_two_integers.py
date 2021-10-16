# 두 정수 사이의 합
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 5, b = 3인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b):
    if a > b:
        a, b = b, a        
        pass

    return sum([int(i) for i in range(a, b+1)])

print(solution(5, 3))

# 1. 만약 a가 b보다 크면 a와 b를 Swap 후 return에서 a부터 b까지의 합을 반환한다.
# 2. a가 b보다 작다면 return에서 a부터 b까지의 합을 반환한다.