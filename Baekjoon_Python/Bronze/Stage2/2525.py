time1 = list(map(int, input().split()))
time2 = int(input())

if time1[0] >= 0 and time1[0] <= 23 and time1[1] >= 0 and time1[1] <= 59 and time2 >= 0 and time2 <= 1000:
    time1[1] += time2
    if time1[1] >= 60:
        time1[0] += time1[1] // 60
        time1[1] = time1[1] % 60
    if time1[0] >= 24:
        time1[0] = time1[0] % 24
    print(time1[0], time1[1])
else:
    print("범위 초과")
