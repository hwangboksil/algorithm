# 최댓값
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성

# comprehension 사용
data = [int(input()) for i in range(9)]
print(max(data), data.index(max(data))+1, sep='\n')

# 코드 원리는 리팩토링 전과 같고 comprehension만 적용하여 코드 수를 줄임.

# # ================================================
# data = []

# for i in range(9):
#    data.append(int(input()))
# print(max(data), data.index(max(data))+1, sep='\n')

# # for문을 사용하여 코드 작성
# # - 9번의 loop를 돌면서 값을 한 줄씩 입력 받고, 빈 배열인 data에 값을 바로 넣는다.
# # - 최댓값을 구하는 함수 max와 최댓값이 몇 번째 수인지 파악하기 위해 index 메서드를 사용한다.