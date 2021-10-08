menu = [int(input()) for i in range(5)] # list comprehension을 사용하여 리스트 생성 후 입력 값을 저장한다.
# menu = [입력값1, 입력값2, 입력값3, 입력값4, 입력값5]
combo = (min(menu[:3]) + min(menu[3:])) - 50 # 생성된 menu 리스트 1~3번 사이 중 작은 값과 4~5번 사이 작은 값을 찾은 후 더하여 50을 뺀다.
print(combo)