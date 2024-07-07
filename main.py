import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка иконки и изображения цели
icon = pygame.image.load("img/5555.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80


# Класс для системы подсчета очков
class ScoreSystem:
    def __init__(self):
        self.score = 0  # Общий счет
        self.hits = 0  # Количество попаданий

    def add_score(self, points):
        self.score += points
        self.hits += 1

    def get_score(self):
        return self.score

    def get_hits(self):
        return self.hits

    def reset(self):
        self.score = 0
        self.hits = 0


# Создание экземпляра системы подсчета очков
score_system = ScoreSystem()

# Инициализация шрифта для отображения счета
font = pygame.font.Font(None, 36)

# Генерация случайного цвета фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Начальное положение цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Основной игровой цикл
running = True
while running:
    # Заполнение экрана цветом
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получение позиции мыши при клике
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Проверка попадания по цели
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score_system.add_score(10)  # Добавление 10 очков за попадание
                # Перемещение цели на новую позицию
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отображение счета и количества попаданий
    score_text = font.render(f"Счет: {score_system.get_score()}", True, (255, 255, 255))
    hits_text = font.render(f"Попаданий: {score_system.get_hits()}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(hits_text, (10, 50))

    # Обновление экрана
    pygame.display.update()

# Завершение работы Pygame
pygame.quit()