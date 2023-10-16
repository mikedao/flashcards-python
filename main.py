from card import Card
from deck import Deck
from round import Round

card_1 = Card("What is the Capital of Alaska?", "Juneau", "Geography")
card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
cards = [card_1, card_2, card_3]
deck = Deck(cards) 
round = Round(deck)

print(f"Welcome! You're playing with {len(round.deck.cards)} cards.")
print("-------------------------------------------------")

for i in range(len(round.deck.cards)):
    print(f"This is card number {i+1} out of {len(round.deck.cards)}.")
    print(f"Question: {round.current_card().question}")
    answer = input("Answer: ")
    round.take_turn(answer)
    print(round.turns[-1].feedback())
    print(f"Your score is {round.number_correct()} out of {i+1}.")
    print("-------------------------------------------------")

print("****** Game over! ******")
print(f"You had {round.number_correct()} correct guesses out of {len(round.deck.cards)} for a total score of {round.percent_correct()}%.")

for category in round.categories():
    print(f"{category} - {round.percent_correct_by_category(category)}% correct")
