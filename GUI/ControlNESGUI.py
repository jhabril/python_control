import sys,pygame
size = width, height = 350, 175
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load('image.png').convert_alpha()
 
while True:        
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill([255, 255, 255])
    screen.blit(background_image, (0, 0))
 
    pygame.display.flip()
    
