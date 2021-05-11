import random

def evaluateScore(cards):
    score = 0
    for card in cards:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 21:
                score = score + 1
            else:
                score = score + 11
        else:
            score = score + int(card)

    return score



def blackjack(bet, action):
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4

    dealerCards = []
    myCards = []


    card1 = random.choice(deck)
    deck.remove(card1)
    myCards.append(card1)

    card2 = random.choice(deck)
    deck.remove(card2)
    dealerCards.append(card2)

    card3 = random.choice(deck)
    deck.remove(card3)
    myCards.append(card3)
    dealerCards.append(card3)


    if(evaluateScore(myCards) <= 16):
        card4 = random.choice(deck)
        deck.remove(card4)
        myCards.append(card4)


    # Dealer will always hit at or below 16, according to the rules.
    if(evaluateScore(dealerCards) <= 16):
        card4 = random.choice(deck)
        deck.remove(card4)
        dealerCards.append(card4)



    myScore = evaluateScore(myCards)
    dealerScore = evaluateScore(dealerCards)

    result = 0

    if(myScore == dealerScore):
        result =  0
    elif(myScore > 21 or myScore < dealerScore):
        result = -1 * bet
    elif(myScore == 21 or (myScore > dealerScore and myScore < 21)):
        result = bet


    if(action == "d"):
        result = result * 2

    return result
    


def simulation(num):
    standing = []
    for i in range(1, num):
        standing.append(blackjack(100, "s"))
    hitting = []
    for i in range(1, num):
        hitting.append(blackjack(100, "h"))
    doubling = []
    for i in range(1, num):
        doubling.append(blackjack(100, "d"))

    print("Standing")
    print(standing)
    print("Hitting")
    print(hitting)
    print("Doubling")
    print(doubling)

    print("\n'Intelligent' Standing/Hitting average : ", sum(standing)/len(standing))
    #print("Hitting average : ", sum(hitting)/len(hitting))
    print("Doubling average : ", sum(doubling)/len(doubling))


simulation(1000)