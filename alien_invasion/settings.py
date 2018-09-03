class Settings(object):
	"""docstring for Settings"""
	def __init__(self):
		super(Settings, self).__init__()
		self.screen_width = 1200
		self.screen_height = 800
		self.background_color = (230,230,230)
		self.ship_speed_factor = 1.5  # 飞船一个while循环走1.5像素

		# 子弹配置
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (120,120,120)
		self.bullet_speed_factor = 3
		self.bullet_allowed = 5  # 最大子弹数

		# 外星人配置
		self.alien_speed_factor = 1
		# 撞击屏幕边缘时，向下移动的速度
		self.fleet_drop_speed = 10
		# 1--右移  -1--左移
		self.fleet_direction = 1

		self.ship_limit = 3
		

		