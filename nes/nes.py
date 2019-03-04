import sys, pygame
pygame.init()
 
# Create a clock (for framerating)
clk = pygame.time.Clock()
 
# Grab joystick 0
if pygame.joystick.get_count() == 0:
    raise IOError("No joystick detected")
joy = pygame.joystick.Joystick(0)
joy.init()

def buttonX(boton):
    if(boton==1): return 295
    elif(boton==2): return 250
    elif(boton==8): return 148
    elif(boton==9): return 193
    
def buttonY(boton):
    if(boton==1 or boton==2): return 112    
    elif(boton==8 or boton==9): return 112
 
# Create display
size = width, height = 350, 175
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load('image.png').convert_alpha()
 
# Generate crosshair
crosshair = pygame.surface.Surface((10, 10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair, pygame.Color("blue"), (5,5), 5, 0)
crosshair.set_colorkey(pygame.Color("magenta"))


crosshairb = pygame.surface.Surface((10, 10))
crosshairb.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshairb,pygame.Color("red"), (5,5), 5, 0)
crosshairb.set_colorkey(pygame.Color("magenta"))

# Generate button surfaces
buttons = {}
for b in range(joy.get_numbuttons()):
    buttons[b] = [ crosshair , (buttonX(b), buttonY(b))]
    
while True:
    
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
             
    screen.fill([255, 255, 255])
    screen.blit(background_image, (0, 0))
 
    # Get joystick axes for MacOS
    x = joy.get_axis(3)
    y = joy.get_axis(4)
    # Get joystick axes for Win and Raspberry
    #x = joy.get_axis(0)
    #y = joy.get_axis(1)

    screen.blit(crosshairb,((x*20)+64,(y*20)+96))
    
    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            screen.blit(buttons[b][0], buttons[b][1])
 
    pygame.display.flip()
    clk.tick(40)
