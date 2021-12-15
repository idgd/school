def mi(l,i):
	m = l[i]
	n = i
	for f in range(i,len(l)):
		if l[f] < m: m, n = l[f], f
	return(n - i)

def selection(l):
	for f in range(len(l) - 1):
		i = mi(l,f)
		l[f + i], l[f] = l[f], l[f + i]
	return(l)

# mi(l,i) is linear (n - k), worst case O(n), nested inside forloop
# since both will have the same max length: O(n^2)
