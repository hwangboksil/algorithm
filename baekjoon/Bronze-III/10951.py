# A+B - 4
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

while True:
    try:
        x, y = map(int, input().split())
        print(x+y)
    except:
        break

# - break 사용을 위해 while로 무한루프를 돌린다
# - EOF 처리를 위해 try, except를 사용한다.
# - 예외가 발생하지 않을 경우 값을 입력 받고 계산된 값을 출력하고, 예외 발생 시 break된다.

# - EOF(End Of File) : 파일을 입,출력 시 입력이 끝날때 까지 읽어들이는 readline()과 같은 내장 함수 명령을 쓸 떄 사용. 문제에 여러 개의 테스트 케이스로 이루어져 있단 말.
# - 이런 경우 예외 처리를 위해 Try, except를 사용한다.