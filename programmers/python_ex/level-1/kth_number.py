# k번째 수
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하고자함.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 결과를 배열에 담아 return

# 예시) commands[0][0]-1 == 2 == i, commands[0][1] == 5 == j, commands[0][2]-1 == 3 == k

def solution(array, commands):
    answer = []

    for s in commands:
        a = array[s[0]-1:s[1]]
        a.sort()
        answer.append(a[s[2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# - for문에서 range를 사용하지 않고 commands를 바로 사용하여도 실행 됨.
# - 풀이 과정은 아래 코드와 동일하고 불필요한 commands 값을 가져오는 코드는 삭제함.
# ============================================================

# ============================================================
# refactoring 전
# def solution(array, commands):
#     answer = []

#     for s in range(len(commands)):
#         a = array[commands[s][0]-1:commands[s][1]]
#         a.sort()
#         answer.append(a[commands[s][2]-1])
#     return answer

# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# - for문을 commands의 길이 만큼 반복할 수 있도록 range에 len()함수를 사용한다.
# - 변수 a에 array를 슬라이싱 후 담는다 
#     commands[s][0]-1 == i <- 문제 내에 인덱스는 1부터 시작해야하므로 인덱스를 -1 을 하여 줄여준다.
#     commands[s][1]]  == j <- j는 끝 인덱스를 가져오므로 그대로 사용한다.
# - i:j만큼 슬라이싱된 변수 a를 sort로 정렬한다.
# - 리스트 answer에 append 메서드를 사용하여 k 번째 수를 담고 리턴한다.
#     commands[0][2]-1 == k <- i와 동일한 이유로 -1을 연산한다.
# ============================================================