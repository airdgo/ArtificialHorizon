import pygame

pygame.init()

size = width, height = 500, 500
bgColor = 255, 255, 255
arrowColor = 0, 0, 0
topHorizon = 38, 55, 203
botHorizon = 178,34,34
pitchColor = 0, 0, 0

screen = pygame.display.set_mode(size)

a_surface = pygame.Surface((width+200,height), pygame.SRCALPHA)
a_surface.fill(botHorizon)

b_surface = pygame.Surface((width+200,height), pygame.SRCALPHA)
b_surface.fill(botHorizon)

def bg_surface():
    screen.blit(b_surface, (-100,0))
    pygame.draw.rect(b_surface, topHorizon, ((0, 0),(width+200, height/2)))



# Draw indicator
def draw_indicator():
    pygame.draw.line(screen, arrowColor,(100,250), (220,250), 6)
    pygame.draw.rect(screen, arrowColor, ((245,245), (10,10)))
    pygame.draw.line(screen, arrowColor,(280,250), (400,250), 6)

def draw_horizon():
    pygame.draw.rect(a_surface, topHorizon, ((0, 0),(width+200, height/2)))

    xCoords = [[250, 340, 300, 340],[450, 360, 400, 360]]

    for i in range(17):

        yCoords = (1+i/4)*width/6
    
        xCoords[0].append(xCoords[0][i])
        xCoords[1].append(xCoords[1][i])
    
        pygame.draw.line(a_surface, pitchColor, (xCoords[0][i], yCoords),(xCoords[1][i], yCoords), 2)

textColor = 0,0,0
fontSize = 20
font = pygame.font.SysFont("verdana", fontSize)

def draw_values():
    num0 = font.render("0", True, textColor)
    a_surface.blit(num0, (width/2-fontSize, height/2-fontSize/2))
    a_surface.blit(num0, (width - fontSize*2 , height/2 - fontSize/2))


def blitRotateCenter(screen, surface, topleft, angle):
    rotated_surface = pygame.transform.rotate(surface, angle)
    new_rect = rotated_surface.get_rect(center = surface.get_rect(topleft = topleft).center)
    screen.blit(rotated_surface, new_rect)


state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: state = False
    
    screen.fill(bgColor)

    bg_surface()

    draw_horizon()
    draw_values()
    blitRotateCenter(screen,a_surface,(-100,0), 0)
    
    draw_indicator()


    pygame.display.flip()