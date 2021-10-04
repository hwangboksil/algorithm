# 숫자의 개수
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성

result = []
a,b,c = [int(input()) for _ in range(3)]
nums = list(str((lambda a,b,c: a*b*c)(a,b,c)))

for i in range(10):
    result.append(nums.count(str(i)))
print(*result, sep='\n')

# - 빈 배열 result 선언, a,b,c를 한 줄씩 입력 받을 수 있도록 list comprehension을 사용
# - 변수 nums에 lambda를 사용해 입력 받은 값들을 곱하여 리스트로 만든다.
# - for문에 range(10)을 주고 i 값을 int -> str로 변환 후 '0'인경우 nums에서 count를 사용하여 '0'의 개수를 세어 도출된 값을 빈 배열인 result에 차례대로 넣어준다.
# - 리스트 result를 언 패킹 하기위해 *를 붙여주고 도출된 값들이 한 줄씩 출력되어야 하므로 sep을 사용한다.