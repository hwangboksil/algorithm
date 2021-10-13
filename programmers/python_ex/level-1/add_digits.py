# 자릿수 더하기
# N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 

def solution(n):
    # return sum([int(i) for i in list(str(n))])
    return sum([int(i) for i in str(n)])

print(solution(12345))

# - 입력값을 하나씩 가져오기 위해 str타입으로 변환 후 list에 담아 for문을 돌리고 가져 온 값을 다시 int로 변환하여 list comprehension에 담아둔다.
# - 반복문이 끝나면 sum() 함수를 사용해 리스트에 담긴 모든 값을 합하여 반환한다.

#- 입력값을 반복문에 넣기 전 list에 담지 않아도 str 타입이면 하나씩 가져온다.