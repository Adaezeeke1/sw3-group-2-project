## from project_knowledge import get_quote


class Card:
    def __init__(self, name, attribute_names, attribute_scores, category, quote = None):
        self.name = name
        self.attribute_names = attribute_names
        self.attribute_scores = attribute_scores
        self.category = category
        self.quote = quote

##    def fetch_quote(self):
##        self.quote = get_quote(self.name)


''' 
Example usage
attributes = ['Singing Voice', 'Creativity', 'Composing']
card_attribute_scores = {
    'Singing Voice': 8,
    'Creativity': 5,
    'Composing': 4
}

sample_card = Card("Beyonce", card_attributes, card_attribute_scores, 'Artist', None)
'''