from card import Card

def test_card():
    """ Testing that a card is created with the correct attributes """
    question = "What is the Capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card = Card(question, answer, category)

    assert card.__class__ == Card

def test_card_attributes():
    """ Testing that a card has its attributes """
    question = "What is the Capital of Alaska?"
    answer = "Juneau"
    category = "Geography"

    card = Card(question, answer, category)

    assert card.question == question
    assert card.answer == answer
    assert card.category == category
