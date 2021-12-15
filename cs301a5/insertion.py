def insertion(l):
	# return list
	r = []
	# while l exists
	while l:
		# value: pop the end
		v = l.pop()
		# index: 0
		i = 0
		# for f in return list
		for f in r:
			# until it finds where it's supposed to go, i++
			if f <= v:
				i += 1
		# insert it at the proper location
		r.insert(i,v)
	# return list
	return(r)

# while loop over one loop, for loop over another nested inside
# additionally, insert inside while loop, linear time
# since both lists will have the same maximum length: O(n^2)
