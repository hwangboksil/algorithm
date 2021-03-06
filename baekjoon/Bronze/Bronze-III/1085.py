# 직사각형에서 탈출
# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
# 예제 입력 / 출력
# 6 2 10 3 / 1
# 100 99 98 97 / 2
# 4 9 10 10 / 1

x, y, w, h = map(int, input().split())
print(abs(min(x,y,w-x,h-y)))

# - 직사각형의 왼쪽아래 꼭짓점은 (0, 0) 이므로 0 - x = x 이다. 따라서 x, y는 그대로 사용되며,
# - 현수의 위치에서 w, h까지의 거리를 구해 (w-x or h-y) 계산된 값 중 min()을 사용해 최솟값을 가져온다.