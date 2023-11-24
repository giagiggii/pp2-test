import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

ball_radius = 25
ball_color = (255, 0, 0)  #i guess red
ball_pos = [width // 2, height // 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_pos[1] - 20 >= 0:
        ball_pos[1] -= 20
    if keys[pygame.K_DOWN] and ball_pos[1] + 20 <= height:
        ball_pos[1] += 20
    if keys[pygame.K_LEFT] and ball_pos[0] - 20 >= 0:
        ball_pos[0] -= 20
    if keys[pygame.K_RIGHT] and ball_pos[0] + 20 <= width:
        ball_pos[0] += 20

    screen.fill((255, 255, 255))

    
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
