# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

dice = list(map(int, input().split()))

# 3개의 if문을 사용하여 각 주사위의 눈이 같은 경우, 다른 경우, 모두 다른 경우를 처리

if dice[0] == dice[1] == dice[2]:
    print(10000 + dice[0] * 1000)
elif dice[0] == dice[1] or dice[0] == dice[2]:
    print(1000 + dice[0] * 100)
elif dice[1] == dice[2]:
    print(1000 + dice[1] * 100)
else:
    print(max(dice) * 100)
