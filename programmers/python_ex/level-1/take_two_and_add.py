def solution(numbers):
   answer = []
   n = 0
   for i in numbers:
       for j in range(len(numbers[:-2])):
           answer.append(numbers[n] + numbers[j])
       n += 1
   return print(list(set(answer)))

# 결과
# [Input]
# solution([2, 1, 3, 4, 1])
# [Output]
# [2, 3, 4, 5, 6, 7] 통과

# [Input]
solution([5,0,2,7])
# [Output]
# [0, 2, 5, 7, 10, 12] 탈락 

# 정답
# [2, 3, 4, 5, 6, 7]
# [2, 5, 7, 9, 12]