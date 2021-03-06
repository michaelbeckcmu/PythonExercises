import sys

import pygame

from bullet import Bullet

from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)



def check_keydown_events(event, ai_settings, screen, ship, bullets):
			"""Respond to down keypresses"""
			if event.key == pygame.K_RIGHT:
				#Move the ship to the right.
				ship.moving_right = True
			if event.key == pygame.K_LEFT:
				#Move the ship to the right.
				ship.moving_left = True

			if event.key == pygame.K_SPACE:
				fire_bullet(ai_settings, screen, ship, bullets)

			if event.key == pygame.K_q:
				sys.exit()
				

def check_keyup_events(event,ship):
			"""Respond to up keypresses"""
			if event.key == pygame.K_RIGHT:
				#Stop moving ship to the right
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				#Stop moving ship to the right
				ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
				# Create a a new bullet and add it to the bullets group.
				if len(bullets) < ai_settings.bullets_allowed:
					new_bullet = Bullet(ai_settings, screen, ship)
					bullets.add(new_bullet)

def update_bullets(ai_settings, screen, ship , aliens, bullets):


				# Get rid of bullets that have disappeared.
				for bullet in bullets.copy():
					if bullet.rect.bottom<= 0:
						bullets.remove(bullet)

				# Check for any bullets that have hit aliens
				# If so, get rid of the bullet and the alien
				collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

				if len(aliens) == 0:
					# Destroy existing bullets and create new fleet.
					bullets.empty()
					create_fleet(ai_settings, screen, aliens, ship)





# this can be divided into 3 methods for testing purposes, not going to right now
def create_alien_row(ai_settings, screen, aliens, row_number):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien width.
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	# Create the first row of aliens.
	for alien_number in range(number_aliens_x):
		# Create an alien and place it in the row.
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		aliens.add(alien)

def create_fleet(ai_settings, screen, aliens, ship):

	###
	alien = Alien(ai_settings, screen)
	alien_height = alien.rect.height

	available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship.rect.height)

	number_rows = int(available_space_y / (2 * alien_height))

	for row_number in range(number_rows):
		create_alien_row(ai_settings, screen, aliens, row_number)


def check_fleet_edges(ai_settings,aliens):
	""" Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, aliens, ship, bullets):
	aliens.empty()
	bullets.empty()
	ship.reset()

	create_fleet(ai_settings, screen, aliens, ship)


def alien_landed(screen, aliens):

	alien_landed = False

	for alien in aliens.sprites():
		if alien.rect.y >= (screen.get_height() - alien.rect.height):
			alien_landed = True

	return alien_landed

def update_screen(ai_settings, screen, ship, bullets, aliens):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	check_fleet_edges(ai_settings,aliens)
	for alien in aliens.sprites():
		alien.blitme()

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# Make the most recently drawn screen visible.
	pygame.display.flip()

