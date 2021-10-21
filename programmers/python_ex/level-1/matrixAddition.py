# 행렬의 덧셈
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수

def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
                                     for i in range(len(arr1))]
print(solution([[1],[2]], [[3],[4]]))
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

# 1. list comprehension을 이용하여 arr1만큼 반복문을 돌리고, 중첩 for문에 대괄호를 씌워 중첩 for문이 끝나면 리스트로 만든다.
# 2. 중첩 for문에서 j는 arr1의 첫번째 리스트의 값 개수만큼 가져올 수 있도록 [0]인덱스를 부여하고, i,j에 해당하는 인덱스를 가져와 더해준다.

# ===================================================
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         x = []
#         for j in range(len(arr1[0])):
#             x.append(arr1[i][j] + arr2[i][j])
#         answer.append(x)
            
#     return answer

# print(solution([[1],[2]], [[3],[4]]))
# print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

# 1. arr1의 길이를 세어 나온 값으로 리스트의 중첩 리스트를 선택할 수 있도록 하고, 빈 배열을 만들어 answer에 append 시 중첩리스트가 될 수 있도록 한다.
# 2. 조건문 사용없이 중첩 for문에 arr1의 중첩리스트 0번을 센 수를 사용하면 arr의 인덱스가 한정되어 벗어날 수 없다.

# ================== 틀린 코드 ================================
# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         x = []
#         if len(arr1[0]) >= 2:
#             for j in range(len(arr1)):
#                 x.append(arr1[i][j] + arr2[i][j])
#         else:
#             x = [sum(arr1[i] + arr2[i])]
#         answer.append(x)
                                
#     return answer

# print(solution([[1],[2]], [[3],[4]]))
# print(solution([[1,2],[2,3]], [[3,4],[5,6]]))

# 1. arr1의 길이를 세어 나온 값으로 리스트의 중첩 리스트를 선택할 수 있도록 한다.
# 2. 만약 arr1의 첫번째 배열의 값이 2개 이상이면 인덱스가 2개 이상이므로 중첩 for문을 돌려 중첩 리스트의 값을 가져올 수 있도록 인덱스[i][j]를 지정한다.
# 3. 아닌 경우 인덱스는 하나만 필요하므로 [i]만 지정한다.
# 4. 각 조건에 만족하는 값이 x에 저장되면 리스트에 담겨 answer에 append되어 answer는 중첩 리스트가 되고, 반환한다.