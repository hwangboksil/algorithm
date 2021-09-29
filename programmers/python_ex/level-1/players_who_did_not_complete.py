# 완주하지 못한 선수
# 마라톤에 참여한 선수들의 이름 배열 participant, 완주한 선수들의 이름 배열 completion, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성

def solution(participant, completion):
   answer = ''
   for i in range(0, len(participant)):
       if participant[i] in completion :
           completion.remove(participant[i])
       else:
           answer = participant[i] 
   return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))