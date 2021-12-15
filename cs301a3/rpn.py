def rpn(func):
	# split input string by spaces
	n = func.split()
	# try/catch due to string input possibly including characters
	try:
		# stack
		s = []
		# for each item in split string
		for f in n:
			# if each operator
			if f == '+':
				a = s.pop()
				b = s.pop()
				s.append(a + b)
			elif f == '-':
				a = s.pop()
				b = s.pop()
				s.append(a - b)
			elif f == '*':
				a = s.pop()
				b = s.pop()
				s.append(a * b)
			elif f == '/':
				a = s.pop()
				b = s.pop()
				s.append(a / b)
			# else, number
			else:
				s.append(float(f))
	# except catch
	except:
		print("invalid RPN function")
	# another try catch for return in case the return string is broken
	try:
		return(str(s[0]))
	except:
		return("invalid RPN function")
