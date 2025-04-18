#꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
List = list(map(int, input().split()))

if 1 <= List[0] <= 1000000000000 and 1 <= List[1] <= 1000000000000 and 1 <= List[2] <= 1000000000000:
    print(List[0] + List[1] + List[2])
else:
    print("범위 초과")

