import pygame

pygame.init()

size = width, height = 500, 500
bgColor = 255, 255, 255

screen = pygame.display.set_mode(size)

frame = pygame.image.load("./images/Frame2.png").convert_alpha()
inel = pygame.image.load("./images/Ring2.png").convert_alpha()
interior = pygame.image.load("./images/Interior2.png").convert_alpha()

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def draw():
    blitRotateCenter(screen, interior, (-250,-250), 0)
    blitRotateCenter(screen, inel, (0,0), 0)
    screen.blit(frame, (0,0))



state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: state = False
    
    screen.fill(bgColor)
    draw()
    pygame.display.flip()   