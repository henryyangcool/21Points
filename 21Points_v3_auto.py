import random
import os
from tokenize import Double3


z = 2
card8decks = {"A": 4 * z, "2": 4 * z, "3": 4 * z, "4": 4 * z,
              "5": 4 * z, "6": 4 * z, "7": 4 * z, "8": 4 * z,
              "9": 4 * z, "10": 4 * z, "J": 4 * z, "Q": 4 * z,
              "K": 4 * z}


def l():
    cards = random.randint(1, 13)
    if cards == 1:
        return "A"
    elif cards == 11:
        return "J"
    elif cards == 12:
        return "Q"
    elif cards == 13:
        return "K"
    else:
        return str(cards)

def licensing(card8decks, cards, card):
    x = l()
    while card8decks[x] <= 0:
        x = l()
    card8decks[x] -= 1
    cards -= 1
    card.append(x)


def main():
    # ---------------------
    cards = 52 * z
    playerWin = 0
    bankerWin = 0
    winrate = 0
    cardSum = 0
    while cards > 10:
        os.system("cls")
        playertotal = 0
        bankertotal = 0
        Playerscard = []
        Bankerscard = []
        playerCurr = 0
        bankerCurr = 0
        bank17Flag = True
        blackjack = True
        # ----------------------------------
        # 玩家:第一張 第二張
        print("Player's Card")
        licensing(card8decks, cards, Playerscard)
        licensing(card8decks, cards, Playerscard)
        playerCurr = 2
        cardSum += 2
        cards -= 2
        # ----------------------------------
        for i in Playerscard:
            if i == "K" or i == "Q" or i == "J":
                print(i, end=" ")
                playertotal += 10
            elif i == "A":
                print(i, end=" ")
                playertotal += 11
            else:
                print(i, end=" ")
                playertotal += int(i)
        print()
        # ----------------------------------
        # 莊家:第一張 第二張
        print("Banker's Card")
        licensing(card8decks, cards, Bankerscard)
        licensing(card8decks, cards, Bankerscard)
        bankerCurr = 2
        cardSum += 2
        cards -= 2
        # ----------------------------------
        for i in Bankerscard:
            if i == "K" or i == "Q" or i == "J":
                bankertotal += 10
            elif i == "A":
                bankertotal += 11
            else:
                bankertotal += int(i)
        for i in Bankerscard:
            print(i, end=" ")
            break
        print("__")
        # ----------------------------------
        # 是否BlackJack
        if playertotal == 21:
            print("\nBlack Jack!")
            blackjack = False
        # ----------------------------------
        if (10 <= playertotal <= 11) and Bankerscard[0] != "A":
            # double
            break
        elif playertotal == 9 and (3 <= int(Bankerscard[0]) <= 6):
            # double
            break
        elif playertotal == 12 and (4 <= int(Bankerscard[0]) <= 6):
            # stand
            break
        elif (13 <= playertotal <= 16) and (2 <= int(Bankerscard[0]) <= 6):
            # stand
            break
        elif playertotal == 17 or playertotal == 18:
            # stand
            break
        else:
            licensing(card8decks, cards, Playerscard)
            playerCurr = 1
            cardSum += 1
            cards -= 1
        # ----------------------------------    
                

if __name__ == "__main__":
    main()
    print("End")