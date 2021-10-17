# 같은 숫자는 싫어
# 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
# 예, arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# 제한 사항 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

def solution(arr):
    answer = []
    n = 10
    for i in arr:
        if n != i:
            answer.append(i)
        n = i  
        
    return answer

print(solution([4,4,4,3,3]))
print(solution([1,1,3,3,0,1,1]))

# 1. 임의의 정수 10을 변수 n에 담아둔다
# 2. for문으로 arr를 하나씩 가져오고, 가져온 값인 i를 n과 비교 후 같지 않으면 answer에 append한다.
# 3. 비교값을 바꾸기 위해 for 마지막에 n값을 i 값으로 바꿔준다.