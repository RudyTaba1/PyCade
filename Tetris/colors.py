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