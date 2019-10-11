import pygame   # pygame 模块包含开发游戏所需功能
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import  game_functions as gf    # 导入模块，指定一个别名gf

def run_game(): # 定义一个方法
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 初始化背景设置，让 python 能够正常的工作
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 创建一个游戏窗口
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()   # 创建一个实例

    # 设置背景颜色
    bg_color = (ai_settings.bg_color)  # 设置背景颜色为浅灰色

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()   # 飞船的位置将在检测事件后更新屏幕前更新
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game() # 初始化游戏并开始主循环
