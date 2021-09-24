A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A//(C-B)+1)

# n = 1 # 판매 수

# while True:
#     total = A + B * n # 생산 비용
#     purchase = C * n # 판매 금액
    
#     if B >= C: # 가변 비용은 판매 금액보다 크거나 같으면 이익이 발생하지 않는다.
#         print(-1)
#         break
#     elif total >= purchase: # 손익분기점 미만인 경우
#         n += 1 # 판매 수 증가
#     elif total < purchase: # 손익분기점 이상
#         print(n)
#         break