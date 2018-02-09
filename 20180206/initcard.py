import random

card = []
for i in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']:
    for j in ['S','H','D','C']:
        card.append(i+j)
print(card)
print(len(card))
random.shuffle(card)
print(card)