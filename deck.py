class Deck:
    def __init__(self, cards):
        self.cards = cards

    def count(self):
        return len(self.cards)

    def cards_in_category(self, category):
        cards_in_category = []
        for card in self.cards:
            if card.category == category:
                cards_in_category.append(card)
        return cards_in_category
