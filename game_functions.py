import sys  # 导入模块，玩家退出游戏，使用 sys 模块退出游戏
import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT: # 是否是按右/左箭头键事件
        # 按下时
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # 松开时
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():    # 事件循环
        if event.type == pygame.QUIT:   # 当玩家点击关闭按钮事件
            sys.exit()  # 退出游戏

        # 当 pygame 检测到 KEYDOWN（按右/左箭头键） 事件时
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)   # 用背景颜色填充屏幕，只接受一个参数：一种颜色
    # 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    # 每次执行while循环时都绘制一个空屏幕，并抹去旧屏幕，将不断更新新屏幕，以显示元素的新位置
    pygame.display.flip()