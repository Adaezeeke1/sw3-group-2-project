
# import random
# from card_class import Card
#
# class ChallengeDeck:
#     def __init__(self):
#         self.cards = [
#             Card("Make the world better with music", "music.jpg", {'Singing Voice': 8, 'Creativity': 5, 'Composing': 4}, None),
#             Card("Justice System needs reform!", "justice.png", {'Intelligence': 6, 'Political Influence': 7, 'Rebellious': 8}, None),
#             Card("Mathematical mind", "math.png", {'Intelligence': 8, 'Good at maths': 10, 'Research': 6}, None),
#             Card("Lead the way", "leadership.png", {'Leadership': 9, 'Empowerment': 6, 'Inspiration': 7}, None),
#             Card("Change minds, Change Lives", "influence.jpg", {'Political Influence': 8, 'Social Influence': 8, 'Activism': 7}, None),
#             Card("Science Enthusiast", "science.jpg", {'Science': 8, 'Chemistry': 6, 'Physics': 7}, None),
#             Card("Think it. Create it.", "innovation.png", {'Engineering': 6, 'Creativity': 7, 'Innovation': 8}, None),
#             Card("Never give up", "nevergiveup.jpg", {'Resilience': 7, 'Determination': 9, 'Confidence': 6}, None),
#             Card("Take centre stage", "stage.jpg", {'Acting': 7, 'Charisma': 8, 'Comedy': 7}, None),
#             Card("Environmentally Conscious", "environment.jpg", {'Solar Energy': 8, 'Activism': 7, 'Social Influence': 6}, None),
#         ]
#         # fetching quote to apply to card
#         self.fetch_quotes()
#         self.shuffle()
#
#     def fetch_quotes(self):
#         for card in self.cards:
#             card.fetch_quote()
#
#     def shuffle(self):
#         random.shuffle(self.cards)
#
#     def draw(self):
#         return self.cards.pop(0)
#
