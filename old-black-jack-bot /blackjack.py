import random
class blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    playerBusted = False
    dealerBusted = False
    playerStood = False
    dealerStood = False
    cardValues = {
        "J" : 10,
        "Q" : 10,
        "K" : 10,
        "A" : 11
    }
    player = []
    dealer = []

    def __init__(self):
        print("Welcome to BlackJack!")
        self.dealCards()

    def dealCards(self):
        print("Dealing cards...")
        self.player.append(random.choice(self.cards))
        self.dealer.append(random.choice(self.cards))
        self.player.append(random.choice(self.cards))
        self.dealer.append(random.choice(self.cards))
        playerTotal, dealerTotal = self.checkValues()

        print("Your cards: ", self.player, "Total: ", playerTotal)
        print("Dealer's cards: ", self.dealer, "Total: ", dealerTotal)

        self.checkBlackJack()
        self.checkWinner()
        self.hitOrStand()
        self.checkWinner()

    def checkBust(self):
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal > 21:
            print("Player busted!")
            self.playerBusted = True
        elif dealerTotal > 21:
            print("Dealer busted!")
            self.dealerBusted = True
            return
        elif self.playerStood == True:
            return

    def checkValues(self):
        playerTotal = 0
        dealerTotal = 0
        for card in self.player:
            if card in self.cardValues:
                playerTotal += self.cardValues[card]
            else:
                playerTotal += card

        for card in self.dealer:
            if card in self.cardValues:
                dealerTotal += self.cardValues[card]
            else:
                dealerTotal += card
        
        return playerTotal, dealerTotal

    def checkWinner(self):
        if self.playerStood:
            playerTotal, dealerTotal = self.checkValues()
            if self.playerBusted:
                print("Dealer wins!")
                return
            elif self.dealerBusted:
                print("Player wins!")
                return
            if 21 - playerTotal < 21 - dealerTotal:
                print("Player wins!")
                return
            if playerTotal == dealerTotal:
                print("It's a tie!")
                return
            print("Dealer wins!")
        else:
            return
        
    def hitOrStand(self):
        while not self.playerBusted and not self.playerStood and not self.dealerBusted and not self.dealerStood:
            move = input("Do you want to hit or stand? ")
            if move == "hit":
                self.player.append(random.choice(self.cards))
                self.checkAces()
                print("Your cards: ", self.player, "Total: ", self.checkValues()[0])
                self.checkBust()
            elif move == "stand":
                self.playerStood = True
                self.dealerPlay()
                break
            else:
                print("Invalid move. Please type 'hit' or 'stand'.")

    def checkBlackJack(self):
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal == 21:
            print("BlackJack! Player wins!")
            self.playerStood = True
        elif dealerTotal == 21:
            print("BlackJack! Dealer wins!")
            self.dealerStood = True
        else:
            return

    def dealerPlay(self):
        while not self.dealerBusted and not self.dealerStood:
            playerTotal, dealerTotal = self.checkValues()
            if dealerTotal < 17:
                self.dealer.append(random.choice(self.cards))
                playerTotal, dealerTotal = self.checkValues()
                print("Dealer's cards: ", self.dealer, "Total: ", dealerTotal)
                self.checkAces()
                self.checkBust()
                self.dealerPlay()
            else:
                self.dealerStood = True

    def checkAces(self):
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal > 21:
            for card in self.player:
                if card == "A":
                    self.player[self.player.index("A")] = 1
                    playerTotal -= 10
                    print("Your cards: ", self.player, "Total: ", self.checkValues()[0])
                    break
        if dealerTotal > 21:
            for card in self.dealer:
                if card == "A":
                    self.dealer[self.dealer.index("A")] = 1
                    dealerTotal -= 10
                    print("Dealer's cards: ", self.dealer, "Total: ", self.checkValues()[1])
                    break

# def playAgain():
#     playAgainBool = True
#     playA = ""
#     while playAgainBool == False:
#         playA = input("Do you want to keep playing? (y/n)").lower
#         while playA.strip() not in ["y", "n"]:
#             playA = input("Incorrect (y/n)").lower()
#             if playA == "y":
#                 playAgainBool == True
#     if playAgainBool == True:
#         blackjack()
#         playAgain()

def main():
    # playAgain()
    blackjack()

if __name__ == "__main__":
    main()