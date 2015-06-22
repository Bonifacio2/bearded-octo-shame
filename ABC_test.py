import unittest

class ABCTest(unittest.TestCase):
	
	def test_something(self):
		self.assertEqual(1,2)
		
if __name__ == '__main__':
	unittest.main()