day = int(input())
car = list(map(int, input().split()))
total = 0

for i in range(5):
    if day == car[i]:
        total += 1
print(total)