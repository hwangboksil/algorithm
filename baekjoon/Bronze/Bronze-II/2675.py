# 문자열 반복
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성
# 예제 입력 1 : 
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1 :
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

T = int(input())

for i in range(T):
    R, S = list(input().split())
    R = int(R)
    for j in range(len(S)):
        print(S[j] * R, end='')
    print('')

# - 테스트 케이스 T를 for문의 반복 횟수로 지정하고 R, S 변수 값을 문자열 list로 입력 받은 뒤 R은 int 타입으로 변환 한다
# - 2중 for문을 열어 S길이 만큼 반복하고, S의 인덱스 j 별로 R을 곱해주며, 여기서 end를 ''으로 지정하여 문자열을 이어준다.
# - 2중 for문에서 end를 지정하여 쉘에서 상위 for문 입력 값을 같은 줄에서 입력받게 되므로 상위 for문에 print('')을 지정해 다음 줄로 넘겨준다.