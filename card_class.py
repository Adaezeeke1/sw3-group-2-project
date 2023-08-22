from project_knowledge import get_quote
class Card:
    def __init__(self, name, attribute_names, attribute_scores, category, quote = None):
        self.name = name
        self.attributes = attributes
        self.quote = quote

    def fetch_quote(self):
        self.quote = get_quote(self.name)

