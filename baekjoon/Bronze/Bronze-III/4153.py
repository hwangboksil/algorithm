# 직각삼각형
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.

while True:
    a = list(map(int, input().split()))
    c = max(a)
    a.remove(c)
    b = a[0]**2 + a[1]**2

    if c == b == 0:
        break
    elif a[0]**2 + a[1]**2 == c**2:
        print('right')
    else:
        print('wrong')

# - x^2 + y^2 = z^2 일 떄 'right' 를 출력한다.
# - 여러개의 테스트 케이스가 주어지고 마지막 줄에는 0 0 0이 입력되니 while문으로 반복하여 해당 조건일 때 break를 해주고,
# - 변수 a를 선언해 int 타입의 값을 리스트에 담아 제일 큰 수 가 z^2이 될 수 있도록 변수 c에 담은 후 a에서 c만 제거한다.
# - 그 후 변수 b를 선언해 a에 담긴 값을 각각 제곱하여 더해준 후 c와 같다면 'right' 출력 아닌 경우 'wrong'을 출력한다.