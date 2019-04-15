import pygame

class Ship():

	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen

		self.settings = ai_settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		self.moving_right = False
		self.moving_left = False

		self.speedup_counter = 0
		self.speedup_flag = False


	def reset(self):
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)



	def update(self):


		if self.moving_right and self.rect.right < self.screen_rect.right and self.multi_button_check():
			self.center += (1+self.settings.ship_speedup_factor*self.speedup_counter)*\
			(self.settings.ship_speed_factor)
		elif self.moving_left and self.rect.left > 0 and self.multi_button_check():
			self.center -= (1+self.settings.ship_speedup_factor*self.speedup_counter)*\
			(self.settings.ship_speed_factor)

		self.rect.centerx = self.center

		if self.speedup_flag:
			self.speedup_counter += 1
		
		if (self.moving_right or self.moving_left) and self.multi_button_check():
			self.speedup_flag = True
		else:
			self.speedup_flag = False
			self.speedup_counter = 0


	def multi_button_check(self):
		if self.moving_left and self.moving_right:
			return False
		else:
			return True


	def blitme(self):
		"""Check ship position and draw the ship at its current location."""
		
		self.update()

		self.screen.blit(self.image, self.rect)