# -*- coding:UTF-8 -*-

class Settings(object):
    '''设置类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed_factor = 5
        # 子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 15
        # 外星人属性
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction表示方向，1为向右移，-1为向左移
        self.fleet_direction = 1