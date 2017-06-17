#coding:utf-8
import sys

import pygame
from bullet import Bullet

def check_keyup_events(event, ship):
	"""响应按键松开"""
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = False

def check_keydown_events(event, ai_settins, screen, ship, bullets):
	"""响应按键按下"""
	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settins, screen, ship, bullets)

def fire_bullet(ai_settins, screen, ship, bullets):
	"""如果还没有到达限制，就发射一颗子弹"""
	# 创建新子弹并将其加入到编组bullets中
	if len(bullets) < ai_settins.bullets_allowed:
		new_bullet = Bullet(ai_settins, screen, ship)
		bullets.add(new_bullet)

def check_events(ai_settins, screen, ship, bullets):
	"""响应按键和鼠标事件"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settins, screen, ship, bullets)

def update_screen(ai_settins, screen, ship, bullets):
	"""更新屏幕上的图像，并切换到新屏幕"""
	# 每次循环时都重绘屏幕
	screen.fill(ai_settins.bg_color)

	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# 让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	"""更新子弹的位置，并删除已消失的子弹"""
	# 更新子弹的位置
	bullets.update()

	# 删除已消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)