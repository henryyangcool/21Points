import random
import os


z = 8
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
        while playertotal < 21:
            # choose = int(input("\n[Hit:1,Stand:2,Double:3,Split:4]  "))
            choose = int(input("\n[Hit:1,Stand:2]  "))
            if choose == 1:
                # ----------------------------------
                # 派牌
                licensing(card8decks, cards, Playerscard)
                playerCurr += 1
                cardSum += 1
                cards -= 1
                # ----------------------------------
                playertotal = 0
                print("Player's card")
                for i in Playerscard:
                    if i == "K" or i == "Q" or i == "J":
                        print(i, end=" ")
                        playertotal += 10
                    elif i == "A":
                        print(i, end=" ")
                        playertotal += 1
                    else:
                        print(i, end=" ")
                        playertotal += int(i)
                print()
                # ----------------------------------
                if playertotal > 21:
                    print("You lose!")
                    bankerWin += 1
                    winrate = playerWin / (playerWin + bankerWin) * 100
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                    break
            elif choose == 2:
                print("Player's Card")
                for i in Playerscard:
                    print(i, end=" ")
                print()
                # ----------------------------------
                # 莊家派牌
                while bankertotal < 17:
                    licensing(card8decks, cards, Bankerscard)
                    bankerCurr += 1
                    cardSum += 1
                    cards -= 1
                    # ----------------------------------
                    print("Banker's Card")
                    bankertotal = 0
                    for i in Bankerscard:
                        if i == "K" or i == "Q" or i == "J":
                            print(i, end=" ")
                            bankertotal += 10
                        elif i == "A":
                            print(i, end=" ")
                            bankertotal += 1
                        else:
                            print(i, end=" ")
                            bankertotal += int(i)
                    bank17Flag = False
                    print()
                    if bankertotal > 21:
                        if bank17Flag:
                            print("\nBanker's Card")
                            for i in Bankerscard:
                                print(i, end=" ")
                            print()
                        print("You Win!")
                        playerWin += 1
                        winrate = playerWin / (playerWin + bankerWin) * 100
                        print("Win Rate:",winrate,"%")
                        print("目前使用牌數量",cardSum)
                        input()
                        break
                # ----------------------------------    
                if (bankertotal < 21 and bankertotal > playertotal) or (bankertotal == 21 and playertotal < 21):
                    if bank17Flag:
                        print("Banker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                        print()
                    print("You Lose!")
                    bankerWin += 1
                    winrate = playerWin / (playerWin + bankerWin) * 100
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                elif playertotal == bankertotal:
                    if bank17Flag:
                        print("Banker's Card")
                        for i in Bankerscard:
                            print(i, end=" ")
                        print()
                    print("Tie!")
                    print("Win Rate:",winrate,"%")
                    print("目前使用牌數量",cardSum)
                    input()
                break
        if playertotal == 21 and blackjack:
            print("The High")
            playerWin += 1
            winrate = playerWin / (playerWin + bankerWin) * 100
            print("Win Rate:",winrate,"%")
            print("目前使用牌數量",cardSum)
            input()
    print("牌不夠 結束遊戲")

if __name__ == "__main__":
    main()
    input()
    # print("End")