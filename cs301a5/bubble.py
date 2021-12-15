def bubble(l):
	# run through list n * n times (f,g)
	for f in range(len(l)):
		for g in range(len(l) - 1):
			# if the current one is greater than the next one
			if l[g] > l[g + 1]:
				# swap them
				l[g], l[g + 1] = l[g + 1], l[g]
	return(l)

# nested for loop
# worst case O(n^2)
