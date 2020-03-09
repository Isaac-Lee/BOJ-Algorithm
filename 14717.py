from itertools import permutations

card = list(range(1, 11)) * 2
my_card = [int(k) for k in input().split()]
card.remove(my_card[0])
card.remove(my_card[1])

rank = list(permutations(card, 2))
rank.sort(key=lambda x: (x[0] == x[1], (x[0] + x[1]) % 10, x[0]))

if my_card[0] == my_card[1]:
    print('%.3f' % (1 - ((10 - my_card[0]) * 2) / len(rank)))
else:
    c = 0
    for r in rank:
        if sum(r) % 10 >= sum(my_card) % 10:
            break
        else:
            c += 1
    print('%.3f' % (c / len(rank)))