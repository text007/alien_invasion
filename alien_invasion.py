import pygame   # pygame 模块包含开发游戏所需功能
from pygame.sprite import Group

from settings import Settings
from game_stats import GameeStats
from ship import Ship
from alien import Alien
import  game_functions as gf    # 导入模块，指定一个别名gf

def run_game(): # 定义一个方法
    # 初始化游戏并创建一个屏幕对象
    pygame.init()   # 初始化背景设置，让 python 能够正常的工作
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 创建一个游戏窗口
    pygame.display.set_caption('Alien Invasion')

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen) # 创建一个实例
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置背景颜色
    bg_color = (ai_settings.bg_color)  # 设置背景颜色为浅灰色

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameeStats(ai_settings)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) # 创建玩家的输入

        if stats.game_active:
            ship.update()   # 飞船的位置将在检测事件后更新屏幕前更新
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)  # 更新使用未消失的子弹的位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)    # 更新后的位置绘制新屏幕

run_game() # 初始化游戏并开始主循环
