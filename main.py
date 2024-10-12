import pygame
import random
import tkinter as tk
from tkinter import messagebox

def show_score(total_clicks, hits, score):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Результаты игры", f"Количество кликов: {total_clicks}\nКоличество попаданий: {hits}\nОбщий счет: {score:.2f}")
    root.destroy()

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/Tir.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("images/target73X75.png")
target_width = 73
target_height = 75
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-0.1, 0.1])  # Меньшая скорость по оси X
target_speed_y = random.choice([-0.1, 0.1])  # Меньшая скорость по оси Y
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

total_clicks = 0  # Количество кликов
hits = 0  # Количество попаданий

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            total_clicks += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1  # Увеличение счетчика попаданий
                score = hits / total_clicks  # Общий счет = отношение попаданий к кликам
                print(f"Очки: {hits}, Клики: {total_clicks}, Счет: {score:.2f}")

    # Движение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновений с границами экрана
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        target_speed_y = -target_speed_y

    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()

score = hits / total_clicks if total_clicks > 0 else 0
show_score(total_clicks, hits, score)
pygame.quit()
