# BitWise
from collections import defaultdict

def countPairs(arr):
	po2 = lambda x: x > 0 and not(x &(x - 1))
	d = defaultdict(int)
	for x in arr:
		d[x] += 1
	d = list(d.items())
	ans = 0
	for i in range(len(d)):
		a, a_cnt = d[i]
		for j in range(i, len(d)):
			b, b_ cnt = d[j]
			if po2(a & b):
				if a == b:
					ans += (a_cnt * (a_cnt - 1)) // 2
				else:
					ans += a_cnt * b_cnt
	return ans

def countPairs(arr):
	po2 = lambda x: x > 0 and not (x & (x - 1))
	d = defaultdict(int)
	for x in arr:
		d[x] += 1
	d = list(d.items())
	ans = 0
	for i in range(len(d)):
		a, a_cnt = d[i]
		for j in range(i, len(d)):
			b, b_cnt = d[j]
			if po2(a & b):
				if a == b:
					ans += (a_cnt *(a_cnt - 1)) // 2
				else:
					ans += a_cnt * b_cnt
	return ans

def countPairs(arr):
	po2 = lambda x: x > 0 and not (x & (x - 1))
	d = defaultdict(int)
	for x in arr:
		d[x] += 1
	d = list(d.items())
	ans = 0
	for i in range(len(d)):
		a, a_cnt = d[i]
		for j in range(i, len(d)):
			b, b_cnt = d[j]
			if po2(a & b):
				if a == b:
					ans += (a_cnt * (a_cnt - 1)) // 2
				else:
					ans += a_cnt * b_cnt
	return ans