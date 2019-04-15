class GameStats():
	"""Track statistics for Alien Invasion"""

	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.reset_stats()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.lives

	def lose_life(self):
		self.ships_left -= 1

	def check_game_over(self):
		if self.ships_left <= 0:
			return True