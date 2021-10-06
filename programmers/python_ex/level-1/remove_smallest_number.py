# 제일 작은 수 제거하기
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴

def solution(arr):
    answer = []
    if arr == [10]:
        answer.append(-1)
    else:
        arr.remove(min(arr))
        answer += arr
        
    return answer

# print(solution([4,3,2,1]))
print(solution([10]))

# - arr 값이 10인 경우 -1을 answer에 append 후 리턴한다.
# - else인 경우 remove 메서드를 사용하여 arr에서 제일 작은 값(min 메서드)을 지운 후 answer 리스트에 append 후 리턴한다.