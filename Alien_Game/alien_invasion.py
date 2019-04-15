import pygame

import sys

from pygame.sprite import Group

from settings import Settings

from ship import Ship

from game_stats import GameStats

from button import Button

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

		stats = GameStats(ai_settings)

		# Set the background color.
		bg_color = (230, 230, 230)

		ship_counter = 0

		game_active = True

		play_button = Button(ai_settings, screen, "Play")

		gf.update_screen(ai_settings, screen, ship, bullets, aliens)

		play_button.draw_button()

		pygame.display.flip()

		game_starting = True

		while game_starting:

			mouse_x, mouse_y = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if play_button.rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
					game_starting = False
					del play_button



		# Start the main loop for the game.
		while game_active:

				pygame.mouse.set_visible(False)

				# Watch for keyboard and mouse events.
				gf.check_events(ai_settings,screen,ship,bullets)

				gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

				if pygame.sprite.spritecollideany(ship,aliens) or gf.alien_landed(screen, aliens):
					print("Life lost!")
					stats.lose_life()

					if  stats.check_game_over():
						print("Game over")
						game_active = False
					else:
						gf.update_aliens(ai_settings, screen, aliens, ship, bullets)


				# Redraw the screen during each pass through the loop.
				gf.update_screen(ai_settings, screen, ship, bullets, aliens)

				# Make the most recently drawn screen visible.
				pygame.display.flip()


		pygame.mouse.set_visible(True)
		
		end_button = Button(ai_settings, screen, "Quit")

		end_button.draw_button()

		pygame.display.flip()

		while True:

			mouse_x, mouse_y = pygame.mouse.get_pos()

			for event in pygame.event.get():

				if event.type == pygame.MOUSEBUTTONDOWN and end_button.rect.collidepoint(mouse_x, mouse_y):
					sys.exit()



run_game()