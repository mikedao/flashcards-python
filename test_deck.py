from card import Card
from deck import Deck

def test_deck():
    """ Testing that a deck is created with the correct attributes """

    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    assert deck.__class__ == Deck
    assert deck.cards == cards

    assert card_1 in deck.cards
    assert card_2 in deck.cards
    assert card_3 in deck.cards

def test_count():
    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    assert deck.count() == 3

def test_cards_in_category():
    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    assert card_1 in deck.cards_in_category("Geography")
    assert card_2 not in deck.cards_in_category("Geography") 
    assert card_3 not in deck.cards_in_category("Geography") 

    assert card_1 not in deck.cards_in_category("STEM")
    assert card_2 in deck.cards_in_category("STEM")
    assert card_3 in deck.cards_in_category("STEM")

    assert [] == deck.cards_in_category("Pop Culture")
