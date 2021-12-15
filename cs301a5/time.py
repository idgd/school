import insertion
import bubble
import selection
import merge

from time import time
from random import shuffle

# likely mergesort will have the best runtime, as theoretically it's O(n log(n)) < O(n^2) of the rest

def bench(f,l):
	a = 0
	c = 8
	for g in range(c):
		nl = l[:]
		shuffle(nl)

		s = time()
		f(nl)
		e = time()

		a += (e - s)

	return(a / c)

l = [f for f in range(2048)]

t = bench(insertion.insertion,l)
print("Insertion time: {0:.8f}".format(t))

t = bench(bubble.bubble,l)
print("Bubble time:    {0:.8f}".format(t))

t = bench(selection.selection,l)
print("Selection time: {0:.8f}".format(t))

t = bench(merge.merge,l)
print("Merge time:     {0:.8f}".format(t))

# benchmark results:
# Insertion time: 0.09163362
# Bubble time:    0.55817613
# Selection time: 0.12464038
# Merge time:     0.00558105
# as expected, merge is the fastest
# bubble is slowest, selection second slowest, and insertion third
# bubble doesn't use builtin functions, it uses assignment
# probably why it's slowest vs selection
# selection creates a new list and inserts into it, so probably more ops than
# insertion
# insertion operates in place with insert, so uses builtins, so very fast
# merge has better big-O runtime, overwhelming any small optimizations over
# the long run
