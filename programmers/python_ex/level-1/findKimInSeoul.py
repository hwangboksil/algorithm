# 서울에서 김서방 찾기
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

def solution(seoul):
    return '김서방은 {0}에 있다'.format(seoul.index('Kim'))

print(solution(["Jane", "Hwang", "Kim"]))

# 1. index() 메서드로 배열 Seoul에서 'Kim'의 인덱스를 찾아 format() 함수로 문자열에 넣고 반환한다.