# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수를 완성
def solution(num):
    answer = ''
    if num % 2 == 0 :
        answer = 'Even'
    else :
        answer = 'Odd'
    
    return answer

print(solution(int(input())))