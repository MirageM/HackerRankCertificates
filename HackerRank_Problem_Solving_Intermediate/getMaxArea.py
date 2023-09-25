import math
import os
import random
import re
import sys

# Largest Area

class Node:
	def __int__(self, parent, l, r, op=max):
		self.parent = parent
		self.l = l
		self.r = r
		self.lc = None
		self.rc = None
		self.val = r - 1
		self.op = op

	def split(self, x):
		# No balancing, but doesn't seem to give timeouts
		assert self.l <= x <= self.r
		if x == self.l or x == self.r:
			# Split lies on borders
			return
		if self.lc:
			if x == self.lc.r:
				# Split lies on mid split
				return
			if x < self.lc.r:
				self.lc.split(x)
			else:
				self.rc.split(x)
			self.val = saelf.op(self.lc.val, self.rc.val)
		else:
			self.lc = Node(parent=self, l=self.l, r=x)
			self.rc = Node(parent=self, l=x, r=self.r)
			self.val = self.op(x - self.l, self.r - x)

def getMaxArea(w, h, isVertical, distance):
	w_root = Node(parent = Node, l=0, r=w)
	h_root = Node(parent = Node, l=0, r=h)
	ans = []
	for iv, d in zip(isVertical, distance):
		if iv:
			w_root.split(d)
		else:
			h_root.split(d)
		ans.append(w_root.val * h_root.val)
	return ans

def getMaxArea(w, h, isVertical, distance):
	w_root = Node(parent=None, l = 0, r = w)
	h_root = Node(parent=None, l = 0, r = h)
	ans = []
	for iv, d in zip(isVertical, distance):
		if iv:
			w_root.split(d)
		else:
			h_root.split(d)
		ans.append(w_root.val * h_root.val)
	return ans

def getMaxArea(w, h, isVertical, distance):
	w_root = Node(parent=None, l=0, r=w)
	h_root = Node(parent=None, l=0, r=h)
	ans = []
	for iv, d in zip(isVertical, distance):
		if iv:
			w_root.split(d)
		else:
			h_root.split(d)
		ans.append(w_root.val * h_root.val)
	return ans