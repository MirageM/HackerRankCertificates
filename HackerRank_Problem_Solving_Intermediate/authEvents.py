# User Friendly Password System
import math
import os
import random
import re
import string
import sys

P = 132
M = 10**9 + 7
PP = [P**i for i in range(11)]
APPENDS = [""] + list(string.ascii_letters) + [str(d) for d in range(10)]

def calc_hash(pw):
	cur_h = 0
	for i in range(len(pw)):
		cur_h += ord(pw[-(i+1)]) * PP[i]
	return cur_h % M

def authEvents(events):
	cur_h = None
	good_hashs = None
	ans = []
	for event, value in events:
		if event == "setPassword":
			good_hashs = set(calc_hash(value + x) for x in APPENDS)
		else:
			assert event == "authorize"
			ans.append(1 if int(value) in good_hashs else 0)
	return ans

def authEvents(events):
	cur_h = None
	good_hashs = None
	ans = []
	for events, value in events:
		if event == "setPassword":
			good_hashs = set(calc_hash(value + x) for x in APPENDS)
		else:
			assert event == "authorize"
			ans.append(1 if int(value) in good_hashs else 0)
	return ans

def authEvents(events):
	cur_h = None
	good_hashs = None
	ans = []
	for event, value in events:
		if event == "setPassword":
			good_hashs = set(calc_hash(value + x) for x in APPENDS)
		else:
			assert event == "authorize"
			ans.append(1 if int(value) in good_hashs else 0)
	return ans

