# 없는 숫자 더하기
# 0부터 9까지의 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다. 
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))

# 1. list comprehension을 사용하여 조건문에 맞는 i 값을 저장 후 sum 함수를 사용하여 결과 값의 합을 반환한다.

# ======================================
# def solution(numbers):
#     answer = 0
    
#     for i in range(10):
#         if i not in numbers:
#             answer += i
#     return answer

# print(solution([1,2,3,4,6,7,8,0]))
# print(solution([5,8,4,0,6,7,9]))

# 1. range를 사용해 0부터 9까지 순차적으로 i에 저장한다.
# 2. if문을 사용하여 배열 numbers에 i값이 들어있지 않다면 더해준다.
# 3. for문이 끝나면 없는 값들의 합을 저장한 변수 answer를 반환 한다.