import unittest

from main import *


class Test(unittest.TestCase):
	def test_findMinRooms(self):
		self.assertEqual(3, findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0]))
		self.assertEqual(2, findMinRooms([1.2, 3.4], [2.3, 5.0], [4.1, 8.0]))
		self.assertEqual(4, findMinRooms([1.2, 3.4], [2.3, 5.0], [3.1, 8.0], [1.0, 10.0]))

	def test_findMinRoomsWithError(self):
		tests = [
			[
				[],
				0,
			],
			[
				[(0, 0)],
				1,
			],
			[
				[(0, 0), (0, 1)],
				2,
			],
			[
				[(0, 3), (0, 1), (1, 2)],
				3,
			],
		]

		for i, test in enumerate(tests):
			self.assertEqual(test[1], findMinRoomsWithError(test[0]))

		with self.assertRaises(Exception):
			findMinRoomsWithError([(1, 0)])

	def test_overlapping(self):
		tests = [
			[
				[],
				0,
				0,
			],
			[
				[(0, 0)],
				2,
				0,
			],
			[
				[(0, 0)],
				0,
				1,
			],
			[
				[(0, 0), (0, 1)],
				0,
				2,
			],
			[
				[(0, 0), (0, 1)],
				1,
				1,
			],
			[
				[(0, 2), (1, 2)],
				0,
				2,
			],
			[
				[(0, 3), (1, 2)],
				0,
				2,
			],
			[
				[(0, 0), (1, 2)],
				0,
				1,
			],
			[
				[(0, 3), (0, 1), (1, 2)],
				0,
				3,
			],
		]

		for i, test in enumerate(tests):
			self.assertEqual(test[2], overlapping(test[0], test[1]), i)


if __name__ == '__main__':
	unittest.main()
