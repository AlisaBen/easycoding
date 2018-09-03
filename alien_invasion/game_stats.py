class GameStats(object):
	"""跟踪游戏统计信息"""
	def __init__(self, game_settings):
		super(GameStats, self).__init__()
		self.game_settings = game_settings
		self.reset_stats()
		self.game_active = True

	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.ships_left = self.game_settings.ship_limit

		