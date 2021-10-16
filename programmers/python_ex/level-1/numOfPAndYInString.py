# 문자열 내 p와 y의 개수
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

def solution(s):
    s = s.upper()
    if s.count('P') != s.count('Y'): return False
    
    return True

print(solution('pPoooyY'))

# 1. 입력받은 문자열 s를 전부 대문자로 변경한다.
# 2. count()함수를 사용하여 문자열 내에 해당하는 알파벳을 세어 값이 틀리면 False를 반환한다.
# 3. if문에 해당하지 않으면 True를 반환한다.