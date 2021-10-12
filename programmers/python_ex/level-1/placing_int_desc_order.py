# 정수 내림차순으로 배치하기
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴

def solution(n):
    answer = sorted(list(str(n)), reverse=True)
    return int(''.join(answer))
    
print(solution(12345))

# - answer 변수에 입력값 n을 str으로 변환 후 list에 담아 sorted() 함수를 사용해 reverse를 하여 값을 Descending(내림차순)하여 저장한다.
# - 저장된 answer의 리스트를 제거하기 위해 join을 사용하고, 값을 int로 변환하여 반환한다.