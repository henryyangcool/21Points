import random
import os


z = 4
card8decks = {"A": z, "2": z, "3": z, "4": z,
              "5": z, "6": z, "7": z, "8": z,
              "9": z, "10": z, "J": z, "Q": z,
              "K": z}


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

def judgeEnd(card8decks):
    flag = 0
    for i in card8decks:
        if card8decks[i] == 0:
            flag += 1
    if flag == 13:
        return True
    else:
        return False

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
    cards = 13 * z
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
        # ----------------------------------
        # 玩家:第一張 第二張
        print("Player's Card")
        licensing(card8decks, cards, Playerscard)
        # if judgeEnd(card8decks) or :
        #     break
        licensing(card8decks, cards, Playerscard)
        playerCurr = 2
        cardSum += 2
        cards -= 2
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
                cardSum += 1
                cards -= 1
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
                    bankerWin += 1
                    winrate = playerWin / (playerWin + bankerWin) * 100
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
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
                    cardSum += 1
                    cards -= 1
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
                    bankerWin += 1
                    winrate = playerWin / (playerWin + bankerWin) * 100
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                elif playertotal > bankertotal or bankertotal > 21 or playertotal == 21:
                    if bank17Flag:
                        print("\nBanker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nYou Win!")
                    playerWin += 1
                    winrate = playerWin / (playerWin + bankerWin) * 100
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                elif playertotal == bankertotal:
                    if bank17Flag:
                        print("Banker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                    print("\nTie!")
                    # tie += 1
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                # elif playertotal == 21:
                #     if bank17Flag:
                #         print("Banker's Card")
                #         for i in Bankerscard:
                #             print(i, end=" ")
                #     print("\nThe High")
                #     input()
                break
        # if playertotal > 21:
        #     print("\nYou lose")
        #     bankerWin += 1
        #     winrate = playerWin / (playerWin + bankerWin) * 100
        #     print("Win Rate:",winrate,"%")
        #     print("目前使用牌數量",cardSum)
        #     input()
        if playertotal == 21:
            print("\nThe High")
            playerWin += 1
            winrate = playerWin / (playerWin + bankerWin) * 100
            print("Win Rate:",winrate,"%")
            print("目前使用牌數量",cardSum)
            input()
        # print("----------")        


if __name__ == "__main__":
    main()
    print("End")