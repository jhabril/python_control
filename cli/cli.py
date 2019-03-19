import sys, pygame

pygame.init()
 
if pygame.joystick.get_count() == 0:
    raise IOError("No joystick detected")
joy = pygame.joystick.Joystick(0)
joy.init()
 
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # Get joystick axes for Win 	
    #x = joy.get_axis(0)
    #if(str(x)!="-0.00784301757812"): print(x)
    #y = joy.get_axis(1)
    #if(str(y)!="-0.00784301757812"): print(y)


    # Get joystick axes for MacOS	
    x = joy.get_axis(3)
    if(str(x)!="-0.00393676757812"): print(x)
    y = joy.get_axis(4)
    if(str(y)!="-0.00393676757812"): print(y)


    # Get joystick axes for Raspberry Pi
    #x = joy.get_axis(0)
    #if(str(x)!="0.0"): print(x)
    #y = joy.get_axis(1)
    #if(str(y)!="0.0"): print(y)

    for b in range(joy.get_numbuttons()):
        if joy.get_button(b):
            print(b)            
