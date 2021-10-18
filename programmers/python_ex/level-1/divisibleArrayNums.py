# 나누어 떨어지는 숫자 배열
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]

print(solution([2, 36, 1, 3], 10))

# 1. if문을 사용하지 않고 or를 사용하면 값이 없는 경우 [-1]을 반환한다.

# =========================================================
# def solution(arr, divisor):
#     answer = sorted([i for i in arr if i % divisor == 0])
#     if sum(answer) == 0:
#        answer.append(-1)
#     return answer

# 1. list comprehension을 사용해 배열 arr의 값을 하나씩 divisor로 나눠 나머지 값이 0인 경우 배수이므로 리스트에 담고 sorted() 함수로 오름차순으로 정렬하여 반환.
# 2. 만약 배열 answer에 값이 없는 경우 -1을 append하여 반환한다.