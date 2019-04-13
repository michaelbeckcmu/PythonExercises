class Settings():

	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Ship settings
		self.ship_speed_factor = 0.3
		self.ship_speedup_factor = 0.02