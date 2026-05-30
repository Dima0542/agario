import pygame
import math
import random

pygame.init()

Size = 800, 600

class Ball():
    def __init__(self, color=(255, 255, 255), x=0, y=0, radius=1, speed=0):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.scale = 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, window):
        self.scale = max(0.3, min(50 / self.radius, 1.5))
        player_screen_radius = int(self.radius * self.scale)
        pygame.draw.circle(window, self.color, (Size[0] // 2, Size[1] // 2), player_screen_radius)

    def collidecircle(self, ball2):
        distance = math.hypot(self.x - ball2.x, self.y - ball2.y)
        return distance < (self.radius + ball2.radius)

window = pygame.display.set_mode(Size)
pygame.display.set_caption("Agar.io")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (800, 600))

ball = Ball((0, 0, 255), 400, 300, 20, 5)

running = True
lose = False

cells = [Ball((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(-2000, 2000), random.randint(-2000, 2000), 10) for _ in range(100)]

while running:
    window.fill((0, 0, 0))
    window.blit(bg, (0, 0))

    to_remove = []
    for cell in cells:
        if cell.collidecircle(ball):
            to_remove.append(cell)
            ball.radius += int(cell.radius * 2)
        else:
            sx = int((cell.x - ball.x) * ball.scale + Size[0] // 2)
            sy = int((cell.y - ball.y) * ball.scale + Size[1] // 2)

            cell_radius = int(cell.radius * ball.scale)
            pygame.draw.circle(window, cell.color, (sx, sy), cell_radius)

    ball.move()
    if not lose:
        ball.draw(window)

    if lose:
        t = font.render('U Lose!', 1, (244, 0, 0))
        window.blit(t, 400, 500)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    pygame.display.update()
    clock.tick(60)
pygame.quit()
