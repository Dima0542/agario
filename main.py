import pygame
import math
import random

class Ball():
    def __init__(self, color=(255, 255, 255), x=0, y=0, radius=1, speed=1):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if keys[pygame.K_s]:
            self.y += self.speed
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if keys[pygame.K_d]:
            self.x += self.speed
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, window):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)
        if self.x <= 0 + 20: self.x = 0 + 20
        if self.y <= 0 + 20: self.y = 0 + 20
        if self.x >= 800 - 20: self.x = 800 - 20
        if self.y >= 600 - 20: self.y = 600 - 20

    def collidecircle(self, ball2):
        distance = math.hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("CS2")
clock = pygame.time.Clock()

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))

ball = Ball((0, 0, 255), 400, 300, 20, 5)

running = True
while running:
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))

    ball.move()
    ball.draw(window)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()
