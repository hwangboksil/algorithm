# 주사위 세개
# 1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
# 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
# 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.

a,b,c = map(int, input().split())
if a == b == c:
    print(10000+a*1000)
elif a != b != c != a:
    print(max(a,b,c)*100)
else:
    if a == b or a == c:
        print(1000+a*100)
    else:
        print(1000+b*100)

# - a,b,c 를 각각 입력 받는다.
# - if문을 사용하여 조건을 지정한다. 
#     a,b,c의 값이 같은 경우, 
#     a,b,c의 값이 모두 다른 경우, 
#     두 개씩 값이 같은 경우로 나눠 계산한다.