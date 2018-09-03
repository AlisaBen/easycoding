import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_events(event,ship,game_settings,screen,bullets):
	"""
	按下键盘事件：右移，左移，发射子弹
	"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings,screen,ship,bullets)
	# 按Q时游戏结束
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(game_settings,screen,ship,bullets):
	"""
	如果没有超过当前屏幕显示的最多子弹数，实例化子弹，添加到子弹编组中
	"""
	if(len(bullets) < game_settings.bullet_allowed):
		bullet = Bullet(game_settings,screen,ship)
		bullets.add(bullet)

def check_keyup_events(event,ship):
	"""
	抬起键，抬起空格不发生任何事
	"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship,game_settings,screen,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ship,game_settings,screen,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def update_screen(game_settings,screen,ship,bullets,aliens):
	screen.fill(game_settings.background_color)
	ship.blitme()
	# alien.blitme()
	aliens.draw(screen)
	"""
	API:pygame.sprite.Group.sprites
	sprites() -> sprite_list
	bullet迭代器
	"""
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()


def update_bullets(game_settings,bullets,aliens,screen,ship):
	bullets.update()
	# 超出屏幕边界移除子弹
	# 子弹编组副本
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# 注释掉，调试用，耗时
	# print(len(bullets))
	check_bullet_alien_collisions(game_settings,screen,ship,aliens,bullets)


def check_bullet_alien_collisions(game_settings,screen,ship,aliens,bullets):
	"""检查是否有子弹击中外星人"""
	"""如果是，删除相应的子弹和外星人"""
	# 遍历aliens编组和bullets编组，如果有rect重叠，返回的字典种添加一个键值对
	# 第一个True表示碰撞后删除子弹，第二个True表示碰撞后删除外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	# 生成新的外星人组
	if len(aliens) == 0:
		bullets.empty()
		create_fleet(game_settings,screen,ship,aliens)



def check_fleet_edges(game_settings,aliens):
	for alien in aliens.sprites():
		# 撞击边缘
		if alien.check_edges():
			# 改变移动方向
			change_fleet_direction(game_settings,aliens)
			break


def change_fleet_direction(game_settings,aliens):
	for alien in aliens.sprites():
		# 所有的y加上fleet_drop_speed
		alien.rect.y += game_settings.fleet_drop_speed
	# 更改fleet_direction
	game_settings.fleet_direction *= -1


def ship_hit(game_settings,stats,screen,ship,aliens,bullets):
	"""相应被外星人撞到的飞船"""
	"""游戏重置，复活机会减一"""
	if stats.ships_left > 0:
		stats.ships_left -= 1
		aliens.empty()
		bullets.empty()
		create_fleet(game_settings,screen,ship,aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False




def check_aliens_bottom(game_settings,stats,screen,ship,aliens,bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.botton >= screen_rect.bottom:
			ship_hit(game_settings,stats,screen,ship,aliens,bullets)
			break


def update_aliens(game_settings,stats,screen,aliens,ship,bullets):
	"""更新外星人群种所有外星人的位置，自动对每个外星人调用update方法"""
	check_fleet_edges(game_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(game_settings,stats,screen,ship,aliens,bullets)
		# print("Ship hit!!!")
	check_aliens_bottom(game_settings,stats,screen,ship,aliens,bullets)


def get_number_aliens_x(game_settings,alien_width):
	"""计算每行可容纳多少个外星人"""
	available_space_x = game_settings.screen_width - 2 * alien_width
	# print(available_space_x)
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(game_settings,ship_height,alien_height):
	available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(game_settings,screen,aliens,alien_number,row_number):
	alien = Alien(game_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 *alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = 0.5 * alien.rect.height + alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(game_settings,screen,ship,aliens):
	alien = Alien(game_settings,screen)
	# print(alien.rect.width)
	# print(alien.rect.height)
	# print(ship.rect.height)
	number_aliens_x = get_number_aliens_x(game_settings,alien.rect.width)
	number_rows = get_number_rows(game_settings,ship.rect.height,alien.rect.height)
	# print(number_rows)
	# print(number_aliens_x)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(game_settings,screen,aliens,alien_number,row_number)


