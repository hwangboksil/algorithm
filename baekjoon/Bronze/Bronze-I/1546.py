# 평균
# 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 각 점수들을 (점수/M*100)으로 고쳤다.
# 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성

import statistics

n = int(input())
M = list(map(int, input().split()))
a = []

for i in M:
    a.append(i/max(M)*100)
print(round(statistics.mean(a), 2))

# - statistics는 파이썬 내장 함수로 mean 메서드를 포함하며 평균을 구함. import 한다.
# - 첫 줄에 계산할 값을 입력 받기, 두번째 줄에 각 점수를 for문으로 돌리기 위해 리스트로 입력 받기, a를 빈 배열로 선언한다.
# - for문에 리스트 M을 반복하여 각 점수를 가져오고 각 점수/max(M)*100 식을 계산 후 빈 배열인 a에 append 한다.
# - 최종적으로 statistics.mean()을 사용하여 평균을 구하고, 해당 값의 소수점 자리를 지정하기 위해 round() 함수를 사용한다.