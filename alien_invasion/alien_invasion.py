import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# from alien import Alien
from game_stats import GameStats
def run_game():
	pygame.init()
	# 获取配置
	game_settings = Settings()
	# 绘制屏幕
	screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
	backgound_color = (220,230,230)
	pygame.display.set_caption("Alien Invasion")
	stats = GameStats(game_settings)
	# 飞船实例化
	ship = Ship(game_settings,screen)
	# 子弹编组，管理屏幕中所有的子弹，保存继承Sprite类的Bullet实例
	# 外星人实例
	# alien = Alien(game_settings,screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(game_settings,screen,ship,aliens)
	while True:
		# 检测飞船事件：左移右移发射子弹
		gf.check_events(ship,game_settings,screen,bullets)  # 修改飞船移动标志
		if stats.game_active:
			ship.update()  # 根据飞船移动标志重新计算飞船中心位置
			# 更新所有子弹位置
			gf.update_bullets(game_settings,bullets,aliens,screen,ship)
			gf.update_aliens(game_settings,stats,screen,aliens,ship,bullets)

		# 绘制飞船子弹
		gf.update_screen(game_settings,screen,ship,bullets,aliens)  

run_game()
