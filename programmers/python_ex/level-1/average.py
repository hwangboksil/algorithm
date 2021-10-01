# 평균 구하기
# 정수를 담고 있는 배열 arr의 평균값을 return

from functools import reduce

def solution(arr):
    answer = (reduce(lambda x, y: x + y, arr)) / len(arr)
    return answer

# def solution(arr):
#     answer = 0
#     answer = sum(arr) / len(arr)
#     return answer