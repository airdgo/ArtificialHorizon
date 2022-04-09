import pygame
import socket

pygame.init()

pygame.display.set_caption("Attitude Indicator")
size = width, height = 500, 500
bgColor = 255, 255, 255
FPS = 60
scale_factor = 7

screen = pygame.display.set_mode(size)

frame = pygame.image.load("./images/Frame.png").convert_alpha()
inel = pygame.image.load("./images/Ring.png").convert_alpha()
interior = pygame.image.load("./images/Interior.png").convert_alpha()

UDP_IP = "127.0.0.1"
UDP_Port = 6789 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_Port))

def recievedata():
    data, addres = sock.recvfrom(1024)
    inf = data.decode('utf-8')
    return (float(inf.split("\t")[1]), float(inf.split("\t")[2]))

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def draw_window(set_pitch, set_roll, scale_factor = 1):
    screen.fill(bgColor)
    blitRotateCenter(screen, interior, (-width/2, -height/2 + set_pitch*scale_factor), set_roll)
    blitRotateCenter(screen, inel, (0, 0), set_roll)
    screen.blit(frame, (0,0))
    pygame.display.update()


def main():

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        set_pitch, set_roll = recievedata()

        draw_window(set_pitch, set_roll, scale_factor)

    pygame.quit()

if __name__ == "__main__":
    main()
       