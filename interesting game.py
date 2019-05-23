K, N = map(int, input().split())
cards = [i for i in map(int, input().split())]
Vasya_points, Petya_points = 0, 0

i = 0
while Vasya_points < K and Petya_points < K and i < N:
    if cards[i] % 7 == 0 and cards[i] % 10 == 0:
        Vasya_points += cards[i]
        Petya_points += cards[i]
    elif cards[i] % 7 == 0:
        Vasya_points += cards[i]
    elif cards[i] % 10 == 0:
        Petya_points += int(cards[i] / 2)
    i += 1

if Vasya_points == Petya_points:
    if i == N:
        print('Draw')
    else:
        while i < N:
            if cards[i] % 7 == 0 and cards[i] % 10 == 0:
                Vasya_points += cards[i]
                Petya_points += cards[i]
            elif cards[i] % 7 == 0:
                Vasya_points += cards[i]
                print('Vasya')
                break
            elif cards[i] % 10 == 0:
                Petya_points += int(cards[i] / 2)
                print('Petya')
                break
            i += 1
        if i == N:
            print('Draw')
elif Vasya_points > Petya_points:
    print('Vasya')
else:
    print('Petya')