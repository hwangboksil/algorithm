# 음계
# 첫째 줄에 8개 숫자가 주어진다. 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
# 예제 입력 1 : 1 2 3 4 5 6 7 8 / 예제 출력 1 : ascending

import sys
i = list(map(int, sys.stdin.readline().split()))
n = [1,2,3,4,5,6,7,8]

if i == n:
    print("ascending")
elif list(reversed(i)) == n:
    print("descending")
else:
    print("mixed")

# - 변수 i에 입력 받은 값들을 list로 저장한다.
# - i가 미리 선언된 변수 n과 같으면, 만약 i가 n의 순서 반대로 입력됐다면, 그 외의 입력이면
# - 각 조건에 맞는 문자열을 출력한다.