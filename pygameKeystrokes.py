import pygame

pygame.init()
gameWindow = pygame.display.set_mode((100,100))

pygame.display.set_caption("DIRECTIONS")

clock = pygame.time.Clock()

char = []

while (char != 'q'):

    char = 'g'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            char = 'q'
            
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_UP] !=0):
       print("up")  
       char.append('2')
    elif(keys[pygame.K_DOWN] !=0):
       print("down")
       char.append('2')

    if(keys[pygame.K_LEFT] !=0):
       print("left")
       char.append('2')
    elif(keys[pygame.K_RIGHT] !=0):
       print("Right")
       char.append('2')
       
  

    #print(event)

    pygame.display.update()

    clock.tick(120)
    print(char)

pygame.quit()
quit()
