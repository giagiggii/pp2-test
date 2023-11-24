import pygame
import datetime
pygame.init()
w = 830
h = 830
angle1 = 0
angle2 = 0

f_sys = pygame.font.SysFont('twcen', 30)
sc = pygame.display.set_mode((w, h), pygame.RESIZABLE)

pygame.display.set_caption("simple clock")

white = (255, 255, 255)

mickey_surf = pygame.image.load("IMG_9937.JPG")
left_hand_surf = pygame.image.load("left-hand.png").convert_alpha()
right_hand_surf = pygame.image.load("right-hand.png").convert_alpha()

mickey_surf = pygame.transform.scale(mickey_surf, (mickey_surf.get_width() // 2.7, mickey_surf.get_height() // 2.7))
clock = pygame.time.Clock()
x = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()
    angle1 = -t.second * 6
    angle2 = -t.minute * 6
    sc.fill(white)
    sc_f_sys = f_sys.render(f'{t:%H-%M-%S}', 1, (0, 0, 0), (255, 255, 255))

    right_hand_surf1 = pygame.transform.scale(right_hand_surf, (right_hand_surf.get_width() // 1.2, right_hand_surf.get_height() // 1.5))
    left_hand_surf1 = pygame.transform.scale(left_hand_surf, (left_hand_surf.get_width() // 1.2, left_hand_surf.get_height() // 1.5))
    
    left_hand_surf2 = pygame.transform.rotate(left_hand_surf1, angle1)
    right_hand_surf2 = pygame.transform.rotate(right_hand_surf1, angle2)

    mickeyrect = mickey_surf.get_rect(center=(w // 2, h // 2))
    left_hand_rect = left_hand_surf2.get_rect(center=(w // 2, h // 2))
    right_hand_rect = right_hand_surf2.get_rect(center=(w // 2, h // 2))

    sc.blit(mickey_surf, mickeyrect)
    sc.blit(left_hand_surf2, left_hand_rect)
    sc.blit(right_hand_surf2, right_hand_rect)
    sc.blit(sc_f_sys, (10, 10))
    x -= 1
    pygame.display.update()

    clock.tick(1)