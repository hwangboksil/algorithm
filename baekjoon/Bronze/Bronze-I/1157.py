# 단어 공부
# 알파벳 대소문자로 단어가 주어지면 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

from collections import Counter

s = Counter(list(input().upper()))

max_num = max(s.values())

num_list = list(key for key, value in s.items() if value == max_num)

if len(num_list) >= 2:
    print('?')
else:
    print(*num_list)

# - 변수 s를 선언해 입력받은 문자열을 전부 대문자로 변환 후 리스트에 담고 Counter 모듈을 사용해 dict 타입으로 키와 값을 만들어준다.
# - 변수 max_num을 선언하고 s의 값 중에 제일 큰 수를 저장한다.
# - 변수 num_list를 선언하고 리스트 컴프리헨션을 이용해 s.items로 키와 값을 반복문으로 돌려 키와 값을 하나씩 가져온다.
# - 이때 조건문을 부여하여 max_num에서 나온 큰 값과 반복문에서 가져 온 value를 비교하고 같은 값이면 해당 값의 키를 list에 담아준다.
# - 반복문이 끝나고 num_list에 담긴 값이 2개 이상인 경우 문제의 조건에 따라 '?' 를 출력하고 아닌 경우 num_list를 언패킹 하여 많이 사용된 알파벳 키를 출력.