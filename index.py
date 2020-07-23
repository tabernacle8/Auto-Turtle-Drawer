# Import the pygame module, so you can use it
import pygame
from pygame import *
import sys, random, math, fractions
#import filereader

     
x_vals = []
y_vals = []

f = open("result.txt", "w")


def resolveColor(color):
    if(color =="green"):
        return((0,255,0))
    if(color =="red"):
        return((255,0,0))
    if(color =="yellow"):
        return((255,255,0))
    if(color =="blue"):
        return((0,0,255))
    if(color =="default" or color=="black"):
        return((0,0,0))
    
def changeColor(newcolor):
    pygame.display.set_caption("Color set to "+newcolor)
    x_vals.append(newcolor)
    y_vals.append(newcolor)

# Define a main function
def main():
    changeColor("default")
     
    # Initialize the pygame module
    pygame.init()
    # Load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Taber's Converter")
    
    # Create a surface on screen that has the size of 500 x 500
    screen = pygame.display.set_mode((500,500))
     
    # Define a variable to control the main loop
    running = True

    # Main loop
    timer = 0
    while running:
       

        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        screen.fill((255,255,255))
        color = (0,255,0)

        buttonDown = pygame.mouse.get_pressed()[0]

        timer = timer+1
        if buttonDown and timer%20==0:

            
            pos = pygame.mouse.get_pos()
            x_vals.append(pos[0])
            y_vals.append(pos[1])


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                   changeColor("green")
                   
                if event.key == pygame.K_r:
                    changeColor("red")
                    
                if event.key == pygame.K_y:
                    changeColor("yellow")
                   
                if event.key == pygame.K_b:
                    changeColor("blue")

                if event.key == pygame.K_d:
                    changeColor("black")
                   


            if event.type==QUIT:
                pygame.quit()

            if(event.type == pygame.MOUSEBUTTONDOWN and event.button==2):
                running = False
                print("Final code:\n\n\n")
                index = 1
                while (index<len(x_vals)):

                    if(isinstance(x_vals[index], str)):
                        f.write("turtle.color(\""+x_vals[index]+"\");")
                    else:
                        f.write("turtle.penup();")
                        f.write("turtle.goto("+str(x_vals[index]-170)+","+str((y_vals[index]-300)*-1)+");")
                        f.write("turtle.pendown();")
                        f.write("turtle.circle(1)\n")
                    index = index+1
            
        index = 0
        currentColor = (0,0,0)
        while (index<len(x_vals)):
            if(not(isinstance(x_vals[index], str))):
                pygame.draw.circle(screen, currentColor, [x_vals[index],y_vals[index]], 5, 0)
            else:
                currentColor = resolveColor(x_vals[index])
            index = index+1

        pygame.display.update()
     
     

if __name__=="__main__":
    # Run
    main()