# 모의고사
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer1 = sum([1 for i in range(len(answers)) if person1[i%5] == answers[i]])
    answer2 = sum([1 for i in range(len(answers)) if person2[i%8] == answers[i]])
    answer3 = sum([1 for i in range(len(answers)) if person3[i%10] == answers[i]])

    answer_arr = [answer1, answer2, answer3]
    
    return [i+1 for i in range(len(answer_arr)) if max(answer_arr) == answer_arr[i]]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([5,5,5,1,4,1]))

# 1. 각 수포자의 답은 규칙이있어 규칙이 적용되는 부분까지 변수에 저장한다.
# 2. 인자 answers의 길이를 구하여 인덱스로 사용하고 만약 각 수포자의 답과 answer의 답이 같다면 1을 저장하여 반복문이 종료된 후 sum()을 하여 저장한다.
# 3. 이때, 조건문에서 수포자의 인덱스가 인자 answers의 길이보다 작을 수 있어 % 연산자를 사용하여 인덱스가 초과되어도 0부터 시작할 수 있도록 작성한다.
# 4. 비교를 위해 각 수포자가 맞춘 총 개수를 배열에 담아 변수에 저장한다.
# 5. 저장된 변수 answer_arr 중 가장 큰 값을 가져와 대조하여 같은 경우 해당 인덱스를 저장하고 반환값이 1,2,3으로 지정되어 있어 결과 값 i에 +1을 하여 반환한다.