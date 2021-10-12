# 하샤드 수
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. x가 하샤드 수인지 아닌지 검사하는 solution을 완성

def solution(x):
    y = [int(i) for i in list(str(x))]
    z = 0
    for i in y:
        z += i
    if  x % z == 0:
        return True
    else:
        return False
    
print(solution(110))

# - 입력 받은 x를 변수 y에 str으로 만들어 리스트에 담고 반복문을 돌려 한 개씩 가져온 뒤 해당 값을 int 타입으로 변환하여 리스트 컴프리헨션에 저장한다.
# - 변수 z를 0으로 선언하고, y를 반복문으로 돌려 값을 하나씩 가져와 z에 합해준다.
# - 입력값 x에 z를 나머지 연산하여 값이 0이 되면 조건이 충족되므로 True를 반환하고, 아닌 경우 False를 반환 한다.