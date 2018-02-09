import sys
sys.path.append(r'C:/User/admin/PycharmProjects/project1/20180206')
import rank
# import rank_card from rank
def judge_straight(cards):
    ranks = rank.rank_card(cards)
    return (max(ranks)-min(ranks))==4 and len(set(ranks))==5

if __name__=="__main__":
    cards = "5S 6S 7S 9S 8S"
    print(judge_straight(cards))