import pygame
import random
import time


class Dice:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.value = None
        self.images = [
            pygame.image.load("1_dots.png"),
            pygame.image.load("2_dots.png"),
            pygame.image.load("3_dots.png"),
            pygame.image.load("4_dots.png"),
            pygame.image.load("5_dots.png"),
            pygame.image.load("6_dots.png")
        ]

    def roll(self):
        self.value = random.randint(1, 6)

    def display(self, screen):
        image = self.images[self.value - 1]
        image = pygame.transform.scale(image, (self.size, self.size))
        screen.blit(image, (self.x, self.y))

if __name__ == '__main__':
    # 初始化Pygame
    pygame.init()

    # 定义窗口尺寸和标题
    window_width = 500
    window_height = 500
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Rolling Dice")

    # 创建骰子对象
    dice_size = 100
    dice1_x = window_width // 3 - dice_size // 3
    dice1_y = window_height // 2 - dice_size // 2
    dice1 = Dice(dice1_x, dice1_y, dice_size)

    dice2_x = window_width * 2 // 3 - dice_size * 2 // 3
    dice2_y = window_height // 2 - dice_size // 2
    dice2 = Dice(dice2_x, dice2_y, dice_size)

    # 間隔時間と動画時間
    FPS = 5
    duration = 5
    EndRollTime = 3

    # タイマー
    timer = pygame.time.Clock()
    start_time = time.time()

    # 游戏循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ボタンを押して、サイコロは停止する
        while (time.time() - start_time) < duration:
            window.fill((255, 255, 255))
            # 填充窗口背景
            while (time.time() - start_time) < EndRollTime:
                dice1.roll()
                dice1.display(window)

                dice2.roll()
                dice2.display(window)
                pygame.display.update()
                timer.tick(5)
            #print(dice1.value, dice2.value)
            dice_pl1 = dice1.value
            dice_pl2 = dice2.value
        running = False

    # 退出Pygame
    pygame.quit()
print(dice_pl1, dice_pl2)

