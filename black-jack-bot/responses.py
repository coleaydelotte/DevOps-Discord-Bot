from blackjack import Blackjack
def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if 'play blackjack' in lowered:
        game = Blackjack()
        return "Starting a new Blackjack game!\n" + game.dealCards()
    else:
        return 'Not working'
