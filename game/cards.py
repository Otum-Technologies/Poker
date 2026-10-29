from enum import Enum
from random import Random


class CardSuit(Enum):
    CLUB = "♧"
    DIAMOND = "♢"
    HEART = "♡"
    SPADE = "♤"

class CardValue(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

def get_card_value_by_value(value: int):
    return {2: CardValue.TWO,
            3: CardValue.THREE,
            4: CardValue.FOUR,
            5: CardValue.FIVE,
            6: CardValue.SIX,
            7: CardValue.SEVEN,
            8: CardValue.EIGHT,
            9: CardValue.NINE,
            10: CardValue.TEN,
            11: CardValue.JACK,
            12: CardValue.QUEEN,
            13: CardValue.KING,
            14: CardValue.ACE}[value]

class Card:
    def __init__(self, value: CardValue, suit: CardSuit):
        self.value = value
        self.suit = suit


    def __str__(self) -> str:
        figures = {11:"J", 12:"Q", 13:"K", 14:"A"}
        return f"{figures.get(self.value.value,self.value.value)} {self.suit.value}"

class Deck:
    def __init__(self):
        self.cards = []

    def put_cards(self,cards: list[Card]):
        for card in cards:
            if card not in self.cards:
                self.cards.append(card)

    def draw_random(self):
        return self.cards.pop(Random().randint(0,len(self.cards) - 1))

    def draw(self, card: Card):
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            raise IndexError(f"Card {card} not found in {self}")


    def generate_deck(self, min_card_value: int = 2, max_card_value: int = 14):
        self.cards = []
        if min_card_value < 2 or min_card_value > 14:
            min_card_value = 2
        if  max_card_value < 2 or max_card_value > 14:
            max_card_value = 14
        for suit in CardSuit:
            for i in range(min_card_value, max_card_value + 1):
                self.cards.append(Card(get_card_value_by_value(i), suit))

    def __str__(self) -> str:
        result = []
        for card in cards:
                result.append(str(card))
        return ", ".join(result)