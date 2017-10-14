import pygame
import serial
import time

pygame.init()
gameWindow = pygame.display.set_mode((100,100))
pygame.display.set_caption("DIRECTIONS")
clock = pygame.time.Clock()

ser = serial.Serial('COM4', baudrate = 9600, timeout = 1)
time.sleep(2)

char = 'g'

while (char[0] != 'q'):

    char = 'g'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            char = 'q'
            
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_q]):
       break

    if(keys[pygame.K_UP]):
       #print("up")  
       char+=('2')
    elif(keys[pygame.K_DOWN]):
       #print("down")
       char+=('0')
    else:
       char+=('1')
        

    if(keys[pygame.K_RIGHT]):
       #print("right")
       char+=('2')
    elif(keys[pygame.K_LEFT]):
       #print("left")
       char+=('0')
    else:
       char+=('1')
        

    ser.write(str.encode(char))
    clock.tick(4)


ser.close()
pygame.quit()
quit()
