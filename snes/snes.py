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
    if(boton==0): return 298
    elif(boton==1): return 335
    elif(boton==2): return 298
    elif(boton==3): return 260
    elif(boton==4): return 75
    elif(boton==5): return 295
    elif(boton==8): return 154
    elif(boton==9): return 195
    
def buttonY(boton):
    if(boton==0): return 70
    elif(boton==1): return 98
    elif(boton==2): return 127
    elif(boton==3): return 98
    elif(boton==4 or boton==5): return 11
    elif(boton==8): return 108
    elif(boton==9): return 110
 
# Create display
size = width, height = 389, 187
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load('cnes1.png').convert()
frameRect = pygame.Rect((0, 0), (width, height))
 
# Generate crosshair
crosshair = pygame.surface.Surface((10, 10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair, pygame.Color("black"), (5,5), 5, 0)
crosshair.set_colorkey(pygame.Color("magenta"))

crosshairb = pygame.surface.Surface((10, 10))
crosshairb.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshairb,pygame.Color("red"), (5,5), 5, 0)
crosshairb.set_colorkey(pygame.Color("magenta"))
 
# Generate button surfaces
buttons = {}
for b in range(joy.get_numbuttons()):
    buttons[b] = [        
        crosshair ,
        (buttonX(b), buttonY(b))
    ]
    
while True:
    # Pump and check the events queue
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()
 
    screen.blit(background_image, (0, 0))
 
    # Get joystick axes for MacOS
    x = joy.get_axis(3)
    y = joy.get_axis(4)
    
    # Get joystick axes for Win and Raspberry
    #x = joy.get_axis(0)
    #y = joy.get_axis(1)

    screen.blit(crosshairb,((x*20)+80-5,(y*20)+105-5))
    
    # Get and display the joystick buttons
    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            screen.blit(buttons[b][0], buttons[b][1])
 
    pygame.display.flip()
    clk.tick(40)
