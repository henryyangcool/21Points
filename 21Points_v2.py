import random
import os

card8decks = {"A": 4, "2": 4, "3": 4, "4": 4,
              "5": 4, "6": 4, "7": 4, "8": 4,
              "9": 4, "10": 4, "J": 4, "Q": 4,
              "K": 4}


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
    # 發牌
    cards = 52 * 4
    while cards > 0:
        os.system("cls")
        playertotal = 0
        bankertotal = 0
        Playerscard = []
        Bankerscard = []
        playerCurr = 0
        bankerCurr = 0
        bank17Flag = True
        # ----------------------------------
        # 玩家:第一張 第二張
        print("Player's Card")
        licensing(card8decks, cards, Playerscard)
        licensing(card8decks, cards, Playerscard)
        playerCurr = 2
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
        for i in Bankerscard:
            if i == "K" or i == "Q" or i == "J":
                bankertotal += 10
            elif i == "A":
                bankertotal += 1
            else:
                bankertotal += int(i)
        for i in Bankerscard:
            print(i, end=" ")
            break
        print("__")
        # ----------------------------------
        if playertotal == 21:
            print("\nBlack Jack!")
        while playertotal < 21:
            choose = int(input("\n[Hit:1,Stand:2,Double:3,Split:4]  "))
            if choose == 1:
                licensing(card8decks, cards, Playerscard)
                playerCurr += 1
                for i in Playerscard:
                    if i == "K" or i == "Q" or i == "J":
                        print(i, end=" ")
                        if i == Playerscard[playerCurr - 1]:
                            playertotal += 10
                    elif i == "A":
                        print(i, end=" ")
                        if i == Playerscard[playerCurr - 1]:
                            playertotal += 1
                    else:
                        print(i, end=" ")
                        if i == Playerscard[playerCurr - 1]:
                            playertotal += int(i)
                if playertotal > 21:
                    print("\nYou lose!")
                    input()
                    # break
            elif choose == 2:
                print("Player's Card")
                for i in Playerscard:
                    print(i, end=" ")
                print()
                while bankertotal < 17:
                    licensing(card8decks, cards, Bankerscard)
                    bankerCurr += 1
                    print("Banker's Card")
                    for i in Bankerscard:
                        if i == "K" or i == "Q" or i == "J":
                            print(i, end=" ")
                            if i == Bankerscard[bankerCurr - 1]:
                                bankertotal += 10
                        elif i == "A":
                            print(i, end=" ")
                            if i == Bankerscard[bankerCurr - 1]:
                                bankertotal += 1
                        else:
                            print(i, end=" ")
                            if i == Bankerscard[bankerCurr - 1]:
                                bankertotal += int(i)
                    bank17Flag = False
                    print()
                if (playertotal < bankertotal and bankertotal <= 21) or playertotal > 21:
                    if bank17Flag:
                        print("\nBanker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nYou Lose!")
                    input()
                elif playertotal > bankertotal or bankertotal > 21:
                    if bank17Flag:
                        print("\nBanker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nYou Win!")
                    input()
                elif playertotal == bankertotal:
                    if bank17Flag:
                        print("Banker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nTie!")
                    input()
                elif playertotal == 21:
                    if bank17Flag:
                        print("Banker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nThe High")
                    input()
                break
        # if playertotal > 21:
        #     print("\nYou lose")
        # elif playertotal == 21:
        #     print("\nThe High")
        # os.system("cls")
        # print("----------")
        


if __name__ == "__main__":
    main()
