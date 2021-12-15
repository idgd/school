from insertion import insertion

def merge_sorted(a,b):
	# reverse once so all other operations are constant
	a, b = a[::-1], b[::-1]
	r = []

	# empty a and b
	while a or b:
		# until at least 1 is empty
		if a and b:
			# pop smallest (last) item from whichever is smaller
			if a[-1] < b[-1]: r.append(a.pop())
			else: r.append(b.pop())
		# empty what's left
		elif a: r.append(a.pop())
		elif b: r.append(b.pop())

	return(r)

def merge(l):
	# if it's small
	if len(l) < 9:
		return(insertion(l))

	# split it in half
	m = len(l)//2
	a, b = merge(l[:m]), merge(l[m:])

	# utility function
	l = merge_sorted(a,b)

	return(l)

# merge_sorted is linear ([::-1] reverses)
# merge is log(n). n halves every recursive call, so log(n)
# since merge_sorted is called inside merge, runtime is O(n log(n))
