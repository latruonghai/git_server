import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiplt_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,"Monty Python")


#Test Case in Unittest
