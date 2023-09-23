def stringAnagram(dictionary, query):
	Data = [sorted(i) for i in dictionary]
	Query = [sorted(i) for i in query]
	D = [''.join(i) for i in Data]
	Q = [''.join(i) for i in Query]

	result = list()
	for i in Q:
		c = 0
		for j in D:
			if(i == j):
				c = c + 1
	return result


def stringAnagram(dictionary, query):
	Data = [sorted(dictionary) for i in dictionary]
	Query = [sorted(query) for i in query]
	D = [''.join(i) for i in Data]
	Q = [''.join(i) for i in Query]

	result = list()
	for i in Q:
		c = 0
		for j in D:
			if(i == j):
				c = c + 1
				result.append(c)
	return result
