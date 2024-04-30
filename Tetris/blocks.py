import pygame

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



class Colors:
	#color defintitions
	dark_grey = (25, 30, 40)
	green = (50, 230, 25)
	red = (230, 20, 20)
	orange = (225, 115, 20)
	yellow = (240, 235, 5)
	purple = (165, 0, 250)
	cyan = (20, 200, 210)
	blue = (15, 65, 215)
	white = (255, 255, 255)
	dark_blue = (45, 45, 125)
	light_blue = (60, 85, 160)
	dark_green = (0, 100, 0)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]

class Position:
	#constructor method for position
	def __init__(self, row, column):
		#assign input arg row to var row
		self.row = row
		#assign input arg column to var column
		self.column = column

#defintion of L block and possible orientations
class LBlock(Block):
	def __init__(self):
		super().__init__(id = 1)
		self.cells = {
			0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
			1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
			2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
			3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
		}
        #move spawn point to middle
		self.move(0, 3)

#defintion of J block and possible orientations
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
            3: [Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
        }
        #move spawn point to middle
        self.move(0, 3)

#defintion of I block and possible orientations
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
            1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
            2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
            3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
        }
        #move spawn point to middle
        self.move(-1, 3)

#defintion of O block an possible orientations
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
        }
        #move spawn point to middle
        self.move(0, 4)

#defintion of S block and possible orientations
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
            2: [Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
            3: [Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        #move spawn point to middle
        self.move(0, 3)

#defintion of T block and possible orientations
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
        }
        #move spawn point to middle
        self.move(0, 3)

#defintion of Z block and possible orientations
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
            0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
            1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
            2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
            3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
        }
        #move spawn point to middle
        self.move(0, 3)



