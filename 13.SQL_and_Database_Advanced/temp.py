import itertools

N, M = map(int, input().split())
cards = list(map(int, input().split()))

three_cards = itertools.combinations(cards, N)

print("N: ", N)
print("M: ", M)
print("Cards :", cards)
print(three_cards)
