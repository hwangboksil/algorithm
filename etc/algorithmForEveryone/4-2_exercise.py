# 최댓값을 구하는 재귀함수 구현
# [참고. Python | 재귀(Recursion)함수](https://velog.io/@sz3728/Python-%EC%9E%AC%EA%B7%80Recursion%ED%95%A8%EC%88%98)

def find_max(a, n):
    if n == 1:
        return a[0]
    
    max_n = find_max(a, n-1)
    if max_n > a[n-1]:
        return max_n
    else:
        return a[n-1]

v = [7, 10, 15, 25, 1, 7, 9]
print(find_max(v, len(v)))

# 1. 값이 담긴 리스트를 v에 담아 저장한다.
# 2. 변수 v를 함수의 인자값으로 넣어준다.
# 3. v의 길이(n)가 1이면 a[0]을 반환한다.
# 4. n이 1이 아닌 경우 변수 max_n을 생성하여 find_max를 재귀 호출한다. 이때 n에 8부터 1까지 수가 거꾸로 누적이 된다.
# 4-1. 재귀함수가 종료조건에 의해 끝나면 n의 숫자인 8부터 1까지 인덱스로 사용되고 a에서 인덱스n에 해당하는 값을 max_n에 저장한다.
#     max_n = 42 33 7 58 33 18 92 17
# 5. max_n의 값을 마지막부터 하나씩 가져온다. 따라서 현재 목적은 최대값을 구하는 식이므로 조건문을 지정하여 값을 비교한다
# 6. 조건문에 따라 최종적으로 큰 수를 반환한다.