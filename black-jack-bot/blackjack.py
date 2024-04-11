import random

class Blackjack:
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    playerBusted = False
    dealerBusted = False
    playerStood = False
    dealerStood = False
    cardValues = {
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11
    }
    player = []
    dealer = []

    def __init__(self):
        self.dealCards()

    def dealCards(self) -> str:
        self.player.append(random.choice(self.cards))
        self.dealer.append(random.choice(self.cards))
        self.player.append(random.choice(self.cards))
        self.dealer.append(random.choice(self.cards))
        playerTotal, dealerTotal = self.checkValues()

        game_state = f"Your cards: {self.player}, Total: {playerTotal}\n"
        game_state += f"Dealer's cards: [{self.dealer[0]}, X], Total: {dealerTotal - self.dealer[1] if self.dealer[1] in self.cardValues else dealerTotal - self.dealer[1]}"

        self.checkBlackJack()
        self.checkWinner()

        return game_state

    def checkBust(self) -> str:
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal > 21:
            self.playerBusted = True
            return "Player busted!"
        elif dealerTotal > 21:
            self.dealerBusted = True
            return "Dealer busted!"
        elif self.playerStood:
            return ""

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

    def checkWinner(self) -> str:
        if self.playerStood:
            playerTotal, dealerTotal = self.checkValues()
            if self.playerBusted:
                return "Dealer wins!"
            elif self.dealerBusted:
                return "Player wins!"
            if 21 - playerTotal < 21 - dealerTotal:
                return "Player wins!"
            if playerTotal == dealerTotal:
                return "It's a tie!"
            return "Dealer wins!"
        else:
            return ""

    def hitOrStand(self, move: str) -> str:
        if move.lower() == "hit":
            if self.playerBusted or self.playerStood or self.dealerBusted or self.dealerStood:
                return "The game has ended. Please start a new game."
            self.player.append(random.choice(self.cards))
            self.checkAces()
            playerTotal, _ = self.checkValues()
            bust_message = self.checkBust()
            if bust_message:
                return bust_message
            return f"Your cards: {self.player}, Total: {playerTotal}"
        elif move.lower() == "stand":
            if self.playerBusted or self.playerStood or self.dealerBusted or self.dealerStood:
                return "The game has ended. Please start a new game."
            self.playerStood = True
            self.dealerPlay()
            winner_message = self.checkWinner()
            playerTotal, dealerTotal = self.checkValues()
            return f"Player's cards: {self.player}, Total: {playerTotal}\nDealer's cards: {self.dealer}, Total: {dealerTotal}\n{winner_message}"
        else:
            return "Invalid move. Please type 'hit' or 'stand'."

    def checkBlackJack(self) -> str:
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal == 21:
            self.playerStood = True
            return "BlackJack! Player wins!"
        elif dealerTotal == 21:
            self.dealerStood = True
            return "BlackJack! Dealer wins!"
        else:
            return ""

    def dealerPlay(self) -> None:
        while not self.dealerBusted and not self.dealerStood:
            playerTotal, dealerTotal = self.checkValues()
            if dealerTotal < 17:
                self.dealer.append(random.choice(self.cards))
                self.checkAces()
                bust_message = self.checkBust()
                if bust_message:
                    break
            else:
                self.dealerStood = True

    def checkAces(self) -> None:
        playerTotal, dealerTotal = self.checkValues()
        if playerTotal > 21:
            for i, card in enumerate(self.player):
                if card == "A":
                    self.player[i] = 1
                    break
        if dealerTotal > 21:
            for i, card in enumerate(self.dealer):
                if card == "A":
                    self.dealer[i] = 1
                    break
