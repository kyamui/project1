def rank_card(cards):
    str = "0123456789TJQKA"
    ranks = []
    for r,s in cards.split():
        print(r)
        print(s)
        ranks.append(str.index(r))
    ranks.sort(reverse=False)
    return ranks
if __name__=="__main__":
    cards = "5S JD 9H 9C 6S AD"
    print(cards.split())
    print(rank_card(cards))
