# 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    # return [int(i) for i in list(str(n))[::-1]]
    return list(map(int, reversed(str(n))))

print(solution(33435))

# - 입력값을 리스트에 담아 슬라이싱으로 마지막 값 부터 가져온다 가져온 값을 반복문에 넣고 돌려 하나씩 가져오고 str -> int 타입으로 변환하여 리스에 담아 반환한다.

# - list comprehension을 사용할 필요 없이 입력값을 str 타입으로 변환하여 reserved() 함수를 사용하면 값이 뒤집히고
# - 뒤집힌 값을 int로 변환하여 list에 담아주면 된다.