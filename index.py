# Import the pygame module, so you can use it
import pygame
from pygame import *
import sys, random, math, fractions
#import filereader

windowSize = (500,500)

     
x_vals = []
y_vals = []

f = open("result.txt", "w")

def deleteCord(x, y, buffer):
    index = 0
    for xint in x_vals:

        if(not(isinstance(x_vals[index], str)) and not(isinstance(y_vals[index], str)) and not(isinstance(x_vals[index], list))):

            if( abs(xint-x) <= buffer and abs(y_vals[index]-y) <= buffer):

                del x_vals[index]
                del y_vals[index]

        index = index+1


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
    hdMode = False
    delete = False
    skip_draw = False
    fillEverything = False
    squareMode = 0

    cache = []
    changeColor("default")
     
    # Initialize the pygame module
    pygame.init()
    # Load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Taber's PyDraw")
    
    # Create a surface on screen that has the size of 500 x 500
    screen = pygame.display.set_mode(windowSize)
     
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

            if delete:
                pos = pygame.mouse.get_pos()
                deleteCord(pos[0],pos[1],10)

            elif squareMode==1:
                pos = pygame.mouse.get_pos()
                cache = [ [pos[0],pos[1]] ]
                pygame.display.set_caption("Press 2 for second corner")
                skip_draw = True
                squareMode = -1
            
            elif squareMode==2:
                pos = pygame.mouse.get_pos()
                cache.append([pos[0],pos[1]])
                squareMode = 0
                skip_draw = False

                if fillEverything:
                    cache[0] = [cache[0][0],cache[0][1],"filled"]
                    x_vals.append(cache[0])
                    y_vals.append(cache[1])

                else:
                    cache[0] = [cache[0][0],cache[0][1],"none"]
                    x_vals.append(cache[0])
                    y_vals.append(cache[1])

                deleteCord(cache[0][0], cache[0][1], 1)
                deleteCord(cache[1][0], cache[1][1], 1)
                cache = []
                pygame.display.set_caption("Taber's PyDraw")

            else:
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
                
                if event.key == pygame.K_e:
                    if(delete):
                        pygame.display.set_caption("Erase mode disabled")
                        delete = False
                    else:
                        delete = True
                        pygame.display.set_caption("Erase mode enabled")
                   

                if event.key == pygame.K_h:
                    if(hdMode):
                        pygame.display.set_caption("HD Mode disabled")
                        hdMode = False
                    else:
                        hdMode = True
                        pygame.display.set_caption("HD Mode enabled")

                if event.key == pygame.K_1:
                    if(squareMode == 0):
                        pygame.display.set_caption("Square Mode: 1st corner")
                        squareMode = 1

                if event.key == pygame.K_2:
                    if(squareMode == 0):
                        pygame.display.set_caption("Error: First coordinate not set")
                    else:
                        squareMode = 2
                        pygame.display.set_caption("Square Mode: 2nd corner")

                if event.key == pygame.K_3:
                    if(fillEverything):
                        pygame.display.set_caption("No longer filling automatically")
                        fillEverything = False
                    else:
                        fillEverything = True
                        pygame.display.set_caption("AutoFill enabled")
                   


            if event.type==QUIT:
                pygame.quit()

            if(event.type == pygame.MOUSEBUTTONDOWN and event.button==2):
                running = False
                print("Final code:\n\n\n")
                index = 1
                while (index<len(x_vals)):

                    if(isinstance(x_vals[index], list)):

                        if(x_vals[index][2]=="filled"):
                            f.write("turtle.begin_fill();")

                        f.write("turtle.penup();")
                        f.write("turtle.goto("+str(x_vals[index][0]-170)+","+str((x_vals[index][1]-300)*-1)+");")
                        f.write("turtle.setheading(0);")
                        f.write("turtle.pendown();")
                        f.write("turtle.forward("+str(y_vals[index][0] - x_vals[index][0])+");")
                        f.write("turtle.right(90);")
                        f.write("turtle.forward("+str(y_vals[index][1] - x_vals[index][1])+");")
                        f.write("turtle.right(90);")
                        f.write("turtle.forward("+str(y_vals[index][0] - x_vals[index][0])+");")
                        f.write("turtle.right(90);")
                        f.write("turtle.forward("+str(y_vals[index][1] - x_vals[index][1])+");\n")
                        #y_vals[index][0] - x_vals[index][0],y_vals[index][1] - x_vals[index][1]

                        if(x_vals[index][2]=="filled"):
                            f.write("turtle.end_fill();")


                    elif(isinstance(x_vals[index], str)):
                        f.write("turtle.color(\""+x_vals[index]+"\");")
                    else:


                        if(hdMode):
                            f.write("turtle.begin_fill();")
                            f.write("turtle.penup();")
                            f.write("turtle.goto("+str(x_vals[index]-170)+","+str((y_vals[index]-300)*-1)+");")
                            f.write("turtle.pendown();")
                            f.write("turtle.circle(3)\n")
                            f.write("turtle.end_fill();")
                        else:
                            f.write("turtle.penup();")
                            f.write("turtle.goto("+str(x_vals[index]-170)+","+str((y_vals[index]-300)*-1)+");")
                            f.write("turtle.pendown();")
                            f.write("turtle.circle(1)\n")
                    index = index+1
            
        index = 0
        currentColor = (0,0,0)
        while (index<len(x_vals)):

            if skip_draw:
                break

            if(isinstance(x_vals[index], list)):
                if(x_vals[index][2]=="filled"):
                    pygame.draw.rect(screen, currentColor, (x_vals[index][0],x_vals[index][1],y_vals[index][0] - x_vals[index][0],y_vals[index][1] - x_vals[index][1]))
                else:
                    pygame.draw.rect(screen, currentColor, (x_vals[index][0],x_vals[index][1],y_vals[index][0] - x_vals[index][0],y_vals[index][1] - x_vals[index][1]),1)

            elif(not(isinstance(x_vals[index], str))):
                pygame.draw.circle(screen, currentColor, [x_vals[index],y_vals[index]], 5, 0)

                if delete:
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(screen, (255,0,0), [pos[0],pos[1]], 10, 1)
                
                if(squareMode>0):
                    pos = pygame.mouse.get_pos()
                    pygame.draw.circle(screen, (0,0,255), [pos[0],pos[1]], 10, 1)

            else:
                currentColor = resolveColor(x_vals[index])
            index = index+1

        pygame.display.update()
     
     

if __name__=="__main__":
    # Run
    main()