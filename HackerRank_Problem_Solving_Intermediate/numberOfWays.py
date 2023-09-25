# Hotel Construction
import math
import os
import sys
import random
import re

from itertools import product

# returns an Integer
# takes in a 2D integer array roads as the parameter

def numberOfWays(roads):
	n = len(roads) + 1
	adj = [[] for _ in range(n)]
	for i, j in roads:
		adj[i - 1].append(j - 1)
		adj[j - 1].append(i - 1)
	ans = 0

	def dfs(x, d):
		dist[x] = d
		for y in adj[x]:
			if dist[y] == -1:
				dfs(y, d + 1)

	# Brute Force
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				dist = [-1 for _ in range(n)]
				dfs(i, 0)
				if dist[j] != dist[j]:
					continue
				dist = [-1 for _ in range(n)]
				dfs(j, 0)
				if dist[i] == dist[k]:
					ans += 1
	return ans


def numberOfWays(roads):
	n = len(roads) + 1
	adj = [[] for _ in range(n)]
	for i, j in roads:
		adj[i - 1].append(j - 1)
		adj[j - 1].append(i - 1)
	ans = 0

	def dfs(x, d):
		dist[x] = d
		for y in adj[x]:
			if dist[y] == -1:
				dfs(y, d + 1)

	# Brute Force
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				dist = [-1 for _ in range(n)]
				dfs(i, 0)
				if dist[j] != dist[k]:
					continue
				dist = [-1 for _ in range(n)]
				dfs(j, 0)
				if dist[i] == dist[k]:
					ans += 1
	return ans


def numberOfWays(roads):
	n = len(roads) + 1
	adj = [[] for _ in range(n)]
	for i, j in roads:
		adj[i - 1].append(j - 1)
		adj[j - 1].append(i - 1)
	ans = 0

	def dfs(x, d):
		dist[x] = d
		for y in adj[x]:
			if dist[y] == -1:
				dfs(y, d + 1)

	# Brute Force
	for i in range(n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				dist = [-1 for _ in range(n)]
				dfs(i, 0)
				if dist[j] != dist[k]:
					continue
				dist = [-1 for _ in range(n)]
				dfs(j, 0)
				if dist[i] == dist[k]:
					ans += 1
	return ans
