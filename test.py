import unittest
import main

class TestGame(unittest.TestCase):
	def test_input(self):
		answer = 5
		guess = 5
		result = main.run_guess(answer, guess)
		self.assertTrue(result)

if __name__ == '__main__':
	unittest.main()





