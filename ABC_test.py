import unittest

from ABC import BlockSet

class ABCTest(unittest.TestCase):
	
	def test_add_block(self):
		block_set = BlockSet()
		
		block_set.add_block("AB")
		
		self.assertEqual(len(block_set.blocks), 1)
		
if __name__ == '__main__':
	unittest.main()