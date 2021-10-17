# ACM 호텔
# [문제. BJ 10250 | ACM호텔](https://www.acmicpc.net/problem/10250)

for i in range(int(input())):
    H, W, N = map(int, input().split())
    ve = N%H
    ho = N//H+1
    if ve == 0:
        ve = H
        ho = N//H
    print(int('{0}{1}'.format(ve, str(ho).zfill(2))))

# ex2) 5 10 3 H가 N보다 큰 경우 3은 5로 나눌 수 없으니 몫은 0, 나머지는 3이다.
# 1. ve = 3%5 = 3 따라서 ve는 0이 아니므로 if문 패스
# 2. ho = 3//5+1 = 0 + 1 = 1
# 3. 결과 값은 301 된다.

# ex3) ve == 0일 때 8 20 8
# 1. 예외처리를 ve가 0인 경우에만 if문을 사용도록한다.
# 2. ve가 0이면 ve는 H로 바꿔 입력된 층 수를 바로출력하고, 호수는 N//H한 값을 출력한다.
# 3. 결과 값은 801 이다.