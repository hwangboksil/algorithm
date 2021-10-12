# x만큼 간격이 있는 n개의 숫자
# 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴

def solution(x, n):
    answer = [i*x for i in range(1, n+1)]
    return answer

print(solution(-4, 2))

# - 리스트 컴프리헨션을 사용하여 1부터 입력값 (n+1)의 값을 반복하여 나온 값에 x를 곱하여 준다.