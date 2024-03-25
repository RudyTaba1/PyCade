from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		self.id = id #initialize block id, cell, size and rotation state
		self.cells = {} #dictionary to store cell positions
		self.cell_size = 30 #cell size
		self.row_offset = 0 #vertical movement offset
		self.column_offset = 0# horizontal movement offse
		self.rotation_state = 0 #current rotation
		self.colors = Colors.get_cell_colors() #random colors for blocks

	def move(self, rows, columns):
		#move block byt specific row and column
		self.row_offset += rows
		self.column_offset += columns

	def get_cell_positions(self):
		#calc and return current positions
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	def rotate(self):
		#rotate block to next state
		self.rotation_state += 1 #increment rotation
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0

	def undo_rotation(self):
		#undo rotation for invalid rotation
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	def draw(self, screen, offset_x, offset_y):
		#draw block on screen
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)


