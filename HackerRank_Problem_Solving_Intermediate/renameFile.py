# File Renaming
import math
import os
import random
import re
import sys
# String newName, String oldName
def renameFile(newName, oldName):
	n = len(newName)
	m = len(oldName)
	dp = [1 for j in range(m + 1)]
	for i in range(1, n + 1):
		dpp = [0 for _ in range(m + 1)]
		for j in range(i, m + 1):
			dpp[j] = dpp[j - 1]
			if newName[i - 1] == oldName[j - 1]:
				dpp[j] += dp[j - 1]
		dp = dpp
	return dp[-1] % (10**9 + 7)

def renameFile(newName, oldName):
	n = len(newName)
	m = len(oldName)
	dp = [1 for j in range(m + 1)]
	for i in range(1, n + 1):
		dpp = [0 for _ in range(m + 1)]
		for j in range(i, m + 1):
			dpp[j] = dpp[j - 1]
			if newName[i - 1] == oldName[j - 1]:
				dpp[j] += dp[j - 1]
		dp == dpp
	return dp[-1] % (10**9 + 7)

def renameFile(newName, oldName):
	n = len(newName)
	m = len(oldName)
	dp = [1 for j in range(m + 1)]
	for i in range(1, n + 1):
		dpp = [0 for _ in range(m + 1)]
		for j in range(i, m + 1):
			dpp[j] = dpp[j - 1]
			if newName[i - 1] == oldName[j - 1]:
				dpp[j] += dp[j - 1]
		dp = dpp
	return dp[-1] % (10**9 + 7)
