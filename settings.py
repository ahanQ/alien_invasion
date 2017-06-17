#coding=UTF-8
class Settings():
	"""在读《外星人入侵》的所有设置的类"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230, 230, 230)

		# 飞船的设置
		self.ship_speed_factor = 1.5

		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 5
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3