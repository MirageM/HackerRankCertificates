def reverse_words_order_and_swap_cases(sentence):
	string = ""
	for word in sentence.split(" "):
		string += word[::-1] + ' '
	return string[-2::-1].swapcase()