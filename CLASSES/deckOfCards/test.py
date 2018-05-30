from deck_of_cards import Deck, Card
import unittest

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("A", "Diamonds")
	def test_init(self):
		self.assertEqual(self.card.suit, "Diamonds")
		self.assertEqual(self.card.value, "A")

if __name__ == '__main__':
	unittest.main()
