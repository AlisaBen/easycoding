import pygame
from pygame.sprite import Sprite

# 继承Sprite类，完善自己的代码
class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, game_settings,screen,ship):
		super(Bullet, self).__init__()
		self.screen = screen
		# # 在0，0位置创建bullet，并设置宽高
		# self.rect = pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)

		# # 调整子弹位置到飞船所在位置，调整top相同，中心x坐标相同
		# self.rect.centerx = ship.rect.centerx
		# self.rect.top = ship.rect.top
		# # 将y坐标存储为小数值，以便能够微调子弹的速度
		# self.y = float(self.rect.y)
		# self.color = game_settings.bullet_color
		# self.speed_factor = game_settings.bullet_speed_factor
		# 把子弹换成一个好玩的图片,把图片转换成位图
		self.image = pygame.image.load('images/生气.png').convert_alpha()
		# 修改图像大小
		self.width,self.height = self.image.get_size()
		self.image = pygame.transform.smoothscale(self.image,(self.width//10,self.height//10))
		self.rect = self.image.get_rect()
		# 调整子弹位置到飞船所在位置，调整top相同，中心x坐标相同
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		# 将y坐标存储为小数值，以便能够微调子弹的速度
		self.y = float(self.rect.y)
		self.speed_factor = game_settings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 更新一次坐标y向上移动speed_factor个像素
		self.y -= self.speed_factor
		# 更新子弹的rect位置
		self.rect.y = self.y

	def draw_bullet(self):
		# """
		# API:rect(Surface,color,Rect,width=0)->Rect
		# draw a rectangular shape on the Surgace
		# The width argument is the thickness to draw the outer edge. 
		# If width is zero then the rectangle will be filled.
		# """
		# pygame.draw.rect(self.screen,self.color,self.rect)
		"""在self.rect位置绘制图像"""
		self.screen.blit(self.image,self.rect)

		