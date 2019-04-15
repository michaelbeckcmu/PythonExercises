import pygame

import sys

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
		# Initialize pygame, settings, and screen object.
		pygame.init()
		ai_settings = Settings()
		screen =  pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Make a ship.
		ship = Ship(ai_settings, screen)

		#Make a group to store bullets in.
		bullets = Group()

		# Make an alien
		aliens = Group()

		# Create the fleet of aliens.
		gf.create_fleet(ai_settings, screen, aliens, ship)



		# Set the background color.
		bg_color = (230, 230, 230)


		# Start the main loop for the game.
		while True:



				# Watch for keyboard and mouse events.
				gf.check_events(ai_settings,screen,ship,bullets)

				gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

				if pygame.sprite.spritecollideany(ship,aliens):
					print("Ship hit!")
					sys.exit()

				# Redraw the screen during each pass through the loop.
				gf.update_screen(ai_settings, screen, ship, bullets, aliens)

				# Make the most recently drawn screen visible.
				pygame.display.flip()

run_game()