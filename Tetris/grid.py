import pygame
from colors import Colors

class Grid:
	#constructor method for grid
	def __init__(self):
		self.num_rows = 20 #set rows in grid
		self.num_cols = 10 # set columns in grid
		self.cell_size = 30 #set cell size
		#initialize grid with 0's for each cell
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		#load ceell colors
		self.colors = Colors.get_cell_colors()

	#check if position is within grid
	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

	#check if cell is empty meaning a 0
	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

	#check if row is filled with non 0's
	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True

	#clear row by setting al cells to 0
	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

	#move row down
	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

	#clear all full rows and move rest down
	def clear_full_rows(self):
		completed = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed

	#reset grid to empty state
	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0

	#draw grid
	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
