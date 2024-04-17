import random

class BlackjackGame:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.card_values = {
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11  # Ace initially counts as 11
        }
        self.player = []
        self.dealer = []

    def check_values(self):
        player_total = sum(self.card_values.get(card, card) for card in self.player)
        dealer_total = sum(self.card_values.get(card, card) for card in self.dealer)
        if player_total > 21 and "A" in self.player:
            self.player[self.player.index("A")] = 1
            player_total = sum(self.card_values.get(card, card) for card in self.player)
        return player_total, dealer_total

    def deal_cards(self):
        self.player.extend(random.choices(self.cards, k=2))
        self.dealer.extend(random.choices(self.cards, k=2))
        return self.check_values()

    def hit(self):
        self.player.append(random.choice(self.cards))
        return self.check_values()
