# import the pygame module, so you can use it
import pygame
from pygame import *
import sys, random, math, fractions
#import filereader


f = open("result.txt", "w")
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Carters Converter")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500,500))
     
    # define a variable to control the main loop
    running = True
     


    x_vals = [0]
    y_vals = [0]
    # main loop
    timer = 0
    while running:
       

        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        screen.fill((255,255,255))
        color = (0,255,0)

        buttonDown = pygame.mouse.get_pressed()[0]
            # only do something if the event is of type QUIT

        timer = timer+1
        if buttonDown and timer%20==0:

            
            pos = pygame.mouse.get_pos()
            x_vals.append(pos[0])
            y_vals.append(pos[1])


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()

            if(event.type == pygame.MOUSEBUTTONDOWN and event.button==2):
                running = False
                print("Final code:\n\n\n")
                index = 1
                while (index<len(x_vals)):
                    f.write("turtle.penup();")
                    f.write("turtle.goto("+str(x_vals[index]-170)+","+str((y_vals[index]-300)*-1)+");")
                    f.write("turtle.pendown();")
                    f.write("turtle.circle(1)\n")
                    index = index+1
            
        index = 0
        while (index<len(x_vals)):
            pygame.draw.circle(screen, color, [x_vals[index],y_vals[index]], 1, 0)
            index = index+1

        pygame.display.update()
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()