avg = 0

for i in range(5):
    score = int(input())
    if score < 40 :
        avg += 40
    else :
        avg += score
print(avg // 5)