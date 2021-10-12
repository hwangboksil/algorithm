# 핸드폰 번호 가리기
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴

def solution(phone_number):
    answer = ''
    re_num = len(phone_number[:-4])
    return answer.rjust(re_num, '*') + phone_number[re_num:]

print(solution("027778888"))

# - 변수 answer를 빈 문자열로 선언 하고, 변수 re_num에 슬라이싱을 이용해 뒤 4자리를 제외한 수가 몇개인지 세어준다.
# - answer에 rjust() 함수를 사용하여 앞쪽은 re_num에서 가져 온 제외 할 수만큼 '*' 입력하고,
# - 나머지 4자리 수를 가져오기 위해 슬라이싱으로 re_num 만큼 제외한 값을 포함한다.