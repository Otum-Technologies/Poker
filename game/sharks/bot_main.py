from game.deck_main import deck, deck_draw_card

removed_cards = {}
card, value, deck, removed_cards = deck_draw_card(deck, removed_cards)
print(card)