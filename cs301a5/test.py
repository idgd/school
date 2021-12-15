import unittest
import insertion
import bubble
import selection
import merge

from time import time
from itertools import permutations

class TestSort(unittest.TestCase):
	def bench(self,f):
		l = [f for f in range(-4,5)]
		a = 0
		c = 0
		for g in range(9):
			for h in permutations(l,g):
				h = list(h)
				s = h[:]
				s.sort()

				start = time()
				self.assertEqual(f(h),s)
				end = time()
				a += (end - start)
				c += 1

		a /= c
		print("\n" + str(f.__name__) + ": {:.8f}".format(a))

	def test_insert(self):
		self.bench(insertion.insertion)

	def test_bubble(self):
		self.bench(bubble.bubble)

	def test_selection(self):
		self.bench(selection.selection)

	def test_merge(self):
		self.bench(merge.merge)

unittest.main()
