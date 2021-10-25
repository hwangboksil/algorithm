# 동명이인 찾기 p43
# 조건 : 두 번 이상 나온 이름 찾기
# 입력 : 이름이 n개 들어있는 리스트
# 출력 : 이름이 n개 중 반복되는 이름의 집합

def find_same_name(a):
    return set([i for i in set(a) if a.count(i) >= 2])

print(find_same_name(["Tom", "Jerry", "Mike", "Tom"]));

# 1. 아래 코드를 리스트 컴프리헨션으로 변경함.
# 2. 인자 a의 리스트 값을 set() 함수로 중복 제거하고 반복시켜 값을 i에 저장하고 i를 count() 메서드로 a에 들어있는 개수를 세어 2개 이상인 경우 i를 저장한다.
# 3. 결과값을 집합으로 리턴 한다.

# ======================================
# def find_same_name(a):
#     n = []
#     for i in set(a):
#         if a.count(i) >= 2:
#             n.append(i)

#     return set(n)

