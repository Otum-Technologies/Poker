import random

deck = {"2 ♡" : 2,"3 ♡" : 3,"4 ♡" : 4,"5 ♡" : 5,"6 ♡" : 6, "7 ♡" : 7, "8 ♡" : 8, "9 ♡" : 9, "10 ♡" : 10, "Jack ♡" : 10, "Queen ♡" : 10, "King ♡" : 10, "Ace ♡" : 11,
        "2 ♢" : 2,"3 ♢" : 3,"4 ♢" : 4,"5 ♢" : 5,"6 ♢" : 6, "7 ♢" : 7, "8 ♢" : 8, "9 ♢" : 9, "10 ♢" : 10, "Jack ♢" : 10, "Queen ♢" : 10, "King ♢" : 10, "Ace ♢" : 11,
        "2 ♧" : 2,"3 ♧" : 3,"4 ♧" : 4,"5 ♧" : 5,"6 ♧" : 6, "7 ♧" : 7, "8 ♧" : 8, "9 ♧" : 9, "10 ♧" : 10, "Jack ♧" : 10, "Queen ♧" : 10, "King ♧" : 10, "Ace ♧" : 11,
        "2 ♤" : 2,"3 ♤" : 3,"4 ♤" : 4,"5 ♤" : 5,"6 ♤" : 6, "7 ♤" : 7, "8 ♤" : 8, "9 ♤" : 9, "10 ♤" : 10, "Jack ♤" : 10, "Queen ♤" : 10, "King ♤" : 10, "Ace ♤" : 11}

def deck_draw_card(deck,removed_cards):
        card = random.choice(list(deck.keys()))
        value = deck[card]
        removed_cards[card] = value
        del deck[card]
        return card , value, deck , removed_cards
#okay so here we draw a card from deck and delete it, this card later is added to removed_cards dic that we will
#later connect with our deck so it reset the deck


def deck_reset(deck, removed_cards):
        deck.update(removed_cards)
        return deck