T = int(input())

if T % 10 != 0: # 다 합쳤을 떄 최소로 나울 수 있는 수 찾기
    print(-1)
else:
    A = B = C = 0
    A = T // 300 # 몫
    B = (T % 300) // 60 # 나머지 // 초
    C = (T % 60) // 10
    print(A, B, C)