import pygame
import sys
from bullet import Bullet

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

def update_screen(game_settings,screen,ship,bullets):
	screen.fill(game_settings.background_color)
	ship.blitme()
	"""
	API:pygame.sprite.Group.sprites
	sprites() -> sprite_list
	bullet迭代器
	"""
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()


def update_bullets(bullets):
	bullets.update()
	# 超出屏幕边界移除子弹
	# 子弹编组副本
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# 注释掉，调试用，耗时
	# print(len(bullets))
