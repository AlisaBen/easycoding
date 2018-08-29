import pygame
class Ship(object):
	"""docstring for Ship"""
	def __init__(self, game_settings,screen):
		super(Ship, self).__init__()
		self.game_settings = game_settings
		self.screen = screen  # screen游戏界面
		self.image = pygame.image.load('images/外星飞船.png').convert_alpha()  # 加载飞船图像
		# 修改图像大小
		self.width,self.height = self.image.get_size()
		self.image = pygame.transform.smoothscale(self.image,(self.width//2,self.height//2))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# 获取游戏界面的中心x坐标和底部位置便可确定飞船位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom - game_settings.screen_height / 5
		self.center = float(self.rect.centerx)  # centerx中只能表示整数
		# 移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""
		根据移动标志调整飞船位置
		更改为根据self.center更新位置
		"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			# self.rect.centerx += 1
			self.center += self.game_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			# self.rect.centerx -= 1
			self.center -= self.game_settings.ship_speed_factor
		# 更新centerx，因为绘制图形是根据self.rect()
		# self.rect()定位需要根据centerx，bottom
		self.rect.centerx = self.center  

	def blitme(self):
		"""在self.rect位置绘制图像"""
		self.screen.blit(self.image,self.rect)

