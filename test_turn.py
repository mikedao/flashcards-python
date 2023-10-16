from turn import Turn
from card import Card

def test_turn():
    """ Testing that a turn is created with the correct attributes """
    question = "What is the Capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card = Card(question, answer, category)

    turn = Turn("Juneau", card)

    assert turn.__class__ == Turn

def test_correct():
    """ Testing that the correct method returns True if the guess matches the answer """
    question = "What is the Capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card = Card(question, answer, category)

    turn = Turn("Juneau", card)

    assert turn.correct() == True

    turn = Turn("Albuquerque", card)

    assert turn.correct() == False

