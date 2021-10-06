# OX퀴즈
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 문자열은 O와 X만으로 이루어져 있다.

T = int(input())

for i in range(T):
    s = input()
    n = 0
    result = 0
    for j in s:
        if j == 'O':
            n += 1
        else:
            n = 0
        result += n
    print(result)

# - 테스트 케이스(T)를 입력받는다.
# - for문을 사용하여 T만큼 s 값을 받고, 두 개의 변수에 값이 0이 되도록 선언한다.
# - 2중 for문으로 와서 입력받은 문자열 s를 반복값으로 부여하여 문자 하나씩 j에 저장하여 반복문을 돌린다.
# - 'O'인 경우 n += 1을하여 누적 수치를 만든다.
# - 'X'인 경우 n 값을 0으로 초기화하고 for문이 끝날 때 마다 result에 n 값을 더해준다.