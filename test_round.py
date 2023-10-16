from card import Card
from deck import Deck
from turn import Turn
from round import Round

def test_round():
    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards) 
    round = Round(deck)

    assert deck == round.deck
    assert [] == round.turns

def test_new_turn():
    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards) 
    round = Round(deck)

    new_turn = round.take_turn("Juneau")

    assert new_turn.__class__ == Turn
    assert new_turn.correct() == True
    assert new_turn in round.turns
    assert 1 == round.number_correct()
    assert card_2 == round.current_card()

def test_multiple_turns():
    card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards) 
    round = Round(deck) 
    new_turn = round.take_turn("Juneau")
    round.take_turn("Venus")

    assert len(round.turns) == 2
    assert round.turns[-1].feedback() == "Incorrect."
    assert round.number_correct() == 1
    assert round.number_correct_by_category("Geography") == 1
    assert round.number_correct_by_category("STEM") == 0
    assert round.percent_correct() == 50.0
    assert round.percent_correct_by_category("Geography") == 100.0
    assert round.current_card() == card_3

