def numCells(grid):
	result = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			val = grid[i][j]
			flag = True
			for ii in range(max(0,i-1), min(len(grid), i + 2)):
				for jj in range(max(0, j-1), min(len(grid[0]), j + 2)):
					if (ii, jj) != (i, j) and val <= grid[ii, jj]:
						flag = False
						break
				if(flag == False):
					break
			else:
				result += 1
	return result
