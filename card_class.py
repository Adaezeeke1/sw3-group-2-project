## from project_knowledge import get_quote


class Card:
    def __init__(self, name, image, attributes, quote=None):

        self.name = name
        self.attributes = attributes
        self.quote = quote
        self.image = image
