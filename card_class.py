from project_knowledge import get_quote
class Card:
    def __init__(self, name, attributes, quote=None):
        self.name = name
        self.attributes = attributes
        self.quote = quote

    def fetch_quote(self):
        self.quote = get_quote(self.name)