import sys, pygame 
 
size = width, height = 389, 187
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load('cnes1.png').convert()

while True:
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    screen.blit(background_image, (0, 0))
 
    pygame.display.flip()
