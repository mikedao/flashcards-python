from turn import Turn

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []

    def take_turn(self, answer):
        turn = Turn(answer, self.deck.cards[0])
        self.turns.append(turn)
        self.deck.cards.append(self.deck.cards.pop(0))
        return turn

    def number_correct(self):
        number = 0
        for turn in self.turns:
            if turn.correct() == True : number += 1
        return number

    def current_card(self):
        return self.deck.cards[0]

    def number_correct_by_category(self, category):
        number = 0
        for turn in self.turns:
            if turn.card.category == category and turn.correct() == True : number += 1
        return number

    def percent_correct(self):
        return self.number_correct() / len(self.turns) * 100
    
    def number_of_cards_in_category(self, category):
        number = 0
        for turn in self.turns:
            if turn.card.category == category : number += 1
        return number
    
    def percent_correct_by_category(self, category):
        return self.number_correct_by_category(category) / self.number_of_cards_in_category(category) * 100
