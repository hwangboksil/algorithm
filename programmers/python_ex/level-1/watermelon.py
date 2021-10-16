# 수박수박수박수박수박수?
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

def solution(n):
    answer = []
    wm = ('수', '박')
    
    for i in range(n):
        j = i % 2
        answer.append(wm[j])
        
    return ''.join(answer)

print(solution(1))
print(solution(100))

# 1. 변수 wm에 튜플로 수, 박을 하드코딩한다.
# 2. 입력값 n만큼 wm을 출력하기 위해 n만큼 반복문을 돌린다.
# 3. 변수 j에 i % 2 값을 저장하여 wm의 인덱스 값으로 사용해 answer에 append해준다.
# 4. 반복문이 끝나고 리스트인 answer를 join() 함수를 사용해 문자열로 반환한다.