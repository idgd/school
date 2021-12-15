from time import time
from random import randint
from generate import gen_list, gen_dict

n = 10000

print("All running times average of", n, "runs.")

test_l = gen_list(100)
test_d = gen_dict(100)

# generation
print("")

def generation(f):
	a = 0
	for g in range(n):
		s = time()
		h = f(100)
		e = time()
		a += e - s
	return(a/n)

print("Generating list of 100 items (from random integers).")
print(generation(gen_list))

print("Generating dictionary of 100 pairs (from random integers).")
print(generation(gen_dict))

# list[i], dict[key] access times
print("")

def access(o):
	a = 0
	for i in range(n):
		r = randint(0,99)
		s = time()
		h = o[r]
		e = time()
		a += e - s
	return(a/n)

print("Accessing nth item from list, where n is a random number.")
print("%.20f" % access(test_l))

print("Accessing nth value from dict, where n is a random number.")
print("%.20f" % access(test_d))

# membership
print("")

def membership_correct(o):
	a = 0
	e = 0
	for i in range(n):
		r = randint(0,99)
		s = time()
		if o[r] in o:
			e = time()
		a += e - s
	return(a/n)

def membership_incorrect(o):
	a = 0
	for i in range(n):
		r = randint(100,999)
		s = time()
		if r in o:
			print("I'll never print!")
		e = time()
		a += e - s
	return(a/n)

print("Checking if n is in list, where n is guaranteed to be in the list.")
print("%.20f" % membership_correct(test_l))

print("Checking if n is in dict, where n is guaranteed to be in the dict.")
print("%.20f" % membership_correct(test_d))

print("Checking if n is in list, where n is guaranteed to not be in the list.")
print("%.20f" % membership_incorrect(test_l))

print("Checking if n is in dict, where n is guaranteed to not be in the dict.")
print("%.20f" % membership_incorrect(test_d))

# append/key addition
print("")

def append_l(o):
	a = 0
	for f in range(n):
		r = randint(0,n)
		s = time()
		o.append(r)
		e = time()
		a += e - s
	return(a/n)

def append_d(o):
	a = 0
	for f in range(n):
		r = randint(0,f)
		i = f + n
		s = time()
		o[i] = r
		e = time()
		a += e - s
	return(a/n)

print("Appending", n, "items to a list.")
print("%.20f" % append_l(test_l))

print("Adding", n, "keys to a dict.")
print("%.20f" % append_d(test_d))

# length
print("")

def length(o):
	a = 0
	for f in range(n):
		s = time()
		l = len(o)
		e = time()
		a += e - s
	return(a/n)

print("Finding the length of a list.")
print("%.20f" % length(test_l))

print("Finding the length of a dict.")
print("%.20f" % length(test_d))

# del
print("")

def delet_this_l(oo):
	a = 0
	for f in range(n):
		o = list(oo)
		r = randint(0,99)
		s = time()
		del o[r]
		e = time()
		a += e - s
	return(a/n)

# this one is slightly broken, can't get it to repeat n times; can only del
# once even though I'm recreating the dict every time. Something's fucky.
def delet_this_d(oo):
	a = 0
	for g in range(100):
		o = dict(oo)
		s = time()
		del o[g]
		e = time()
		a += e - s
	return(a/100)

print("Deleting one item from a list. Guaranteed to be inside the list.")
print("%.20f" % delet_this_l(test_l))

print("Deleting one pair from a dict. Guaranteed to be inside the dict.")
print("%.20f" % delet_this_d(test_d))
