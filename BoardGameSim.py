#Name: Aryan Patel
#Student ID: 101260400

#imports neccesary libraries
import pygame
import random
# initializes pygame
pygame.init()

#sets the total number of square for the width and height of the game window
w_square = 6
h_square = 7

# creates the necessary variables needed for the program
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (100,100,100)
PINK = (255,120,203)
BLUE = (0,100,255)
n = 0
r = 0

#creates a list that stores the possible coordinates of the player pieces
pos_p1 = [(30,10),(80,10),(130,10),(180,10),(230,10),(280,10),
          (30,60),(80,60),(130,60),(180,60),(230,60),(280,60),
          (30,110),(80,110),(130,110),(180,110),(230,110),(280,110),
          (30,160),(80,160),(130,160),(180,160),(230,160),(280,160),
          (30,210),(80,210),(130,210),(180,210),(230,210),(280,210),
          (30,260),(80,260),(130,260),(180,260),(230,260),(280,260),
          (30,310),(80,310),(130,310),(180,310),(230,310),(280,310)]
          
pos_p2 = [(15,10),(65,10),(115,10),(165,10),(215,10),(265,10),
          (15,60),(65,60),(115,60),(165,60),(215,60),(265,60),
          (15,110),(65,110),(115,110),(165,110),(215,110),(265,110),
          (15,160),(65,160),(115,160),(165,160),(215,160),(265,160),
          (15,210),(65,210),(115,210),(165,210),(215,210),(265,210),
          (15,260),(65,260),(115,260),(165,260),(215,260),(265,260),
          (15,310),(65,310),(115,310),(165,310),(215,310),(265,310)]


# loads in and stores the necessary images needed for the program in a variable
GW = pygame.image.load("GameWinner.png")
BG = pygame.image.load("checkerboard.png")

d1 = pygame.image.load("Dice1.jpg")
d2 = pygame.image.load("Dice2.jpg")
d3 = pygame.image.load("Dice3.jpg")

#creates and stores the font needed for the program in a variable

font = pygame.font.SysFont("arial", 12)

#stores the colour white in a varaiable that is used later on
c_clr = WHITE

#sets the size of each square for the background and sotres it in a variable
square_dim = 50
#Sets the number for each square 
tile_num = 1
#creates the size of the pygame window using the total number of square multiplied by the size of each square for the height and width
screen = pygame.display.set_mode((w_square*square_dim, h_square*square_dim))
#fills the window with the colour grey
screen.fill(GREY)


#Creates a checkboard pattern and numbers each square and also alternates the colour of each square 
for j in range(0, h_square):
    for i in range(0, w_square):
        pygame.draw.rect(screen, c_clr, (i * square_dim, j  * square_dim, square_dim,square_dim))
        text = font.render(str(tile_num), True, GREY)
        screen.blit(text, ( i* square_dim, j * square_dim))
        tile_num += 1
        pygame.display.update()
        pygame.time.delay(10)
           
        if c_clr == BLACK:
                c_clr = WHITE
        else:
                c_clr = BLACK

    if c_clr == BLACK:
            c_clr = WHITE
    else:
            c_clr = BLACK
        
#creates to boolean variables that are used to run the game
Turn = True
GameOn = True
#prints the two player pieces and updates the screen
p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
pygame.display.update()
pygame.time.delay(5000)


#while the  GameOn variable is set to true the code inside will run
while GameOn == True:
    #if the Turn variable is true the code inside will run
    if Turn == True:
        #sets a variable for each dice and puts a randint function in each to act as the dice values
        dice1 = random.randint(1,3)
        dice2 = random.randint(1,3)
        #Adds up both dice values to indicate the total spaces the player will move
        player_move = dice1 + dice2
        #creates texts in the case a player moves or misses a turn which is used later on and is specific to the player
        move_text = font.render(("Blue player moves " + str(player_move) + " spaces"), True, BLACK)
        missed1_text = font.render("Blue player misses a turn", True, BLACK)
        #prints the dice values
        print(dice1)
        print(dice2)
        #updates display
        pygame.display.update()


        #sets the condition of when each dice value is rolled, all showing the text that indicates how many spaces the player moves, shows the dice faces on the screen and updates the screen,
        #only exception is when a both dices roll one in which the text that indicates that the player misses the turn is shown and the positions of both players are shown
        if dice1 == 1:
            if dice2 == 1:
                player_move = 0
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(missed1_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)               
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                
        elif dice1 == 2:
            if dice2 == 1:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                
        elif dice1 == 3:
            if dice2 == 1:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)

                
        # runs the loop as many times as the value of play_move                               
        for i in range (player_move):
            #prints the position of both players, prints the background and updates the screen
            screen.blit(BG,(0,0))
            p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
            p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
            pygame.display.update()
            pygame.time.delay(700)

            #increases the value of n which changes the coordinates of the player as they move spaces    
            n = n + 1

            #if n == 41 they have won the game which prints the position of both players then displays a win message and ends the game 
            if n == 41:
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)
                print("p1 wins")
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(GW, (35,0))
                win_text = font.render("Blue wins", True, BLACK)
                screen.blit(win_text, (125,200))
                pygame.display.update()
                pygame.time.delay(5000)
                player_move = 0
                GameOn = False
                pygame.quit()
                exit()
                
            #prints the position of both players, prints the background and updates the screen
            else:
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)
                
        #changes the value of Turn to switch to the other player so they can take their turn    
        Turn = False


    else:
        #sets a variable for each dice and puts a randint function in each to act as the dice values
        dice1 = random.randint(1,3)
        dice2 = random.randint(1,3)
        #Adds up both dice values to indicate the total spaces the player will move
        player_move = dice1 + dice2
        #creates texts in the case a player moves or misses a turn which is used later on and is specific to the player
        move_text = font.render(("Pink player moves " + str(player_move) + " spaces"), True, BLACK)
        missed2_text = font.render(" Pink player misses a turn", True, BLACK)
        #prints the dice values
        print(dice1)
        print(dice2)
        #updates display
        pygame.display.update()


        #sets the condition of when each dice value is rolled, all showing the text that indicates how many spaces the player moves, shows the dice faces on the screen and updates the screen,
        #only exception is when a both dices roll one in which the text that indicates that the player misses the turn is shown and the positions of both players are shown
        if dice1 == 1:
            if dice2 == 1:
                player_move = 0
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(missed1_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)               
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d1, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                
        elif dice1 == 2:
            if dice2 == 1:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d2, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
                
        elif dice1 == 3:
            if dice2 == 1:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d1, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 2:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d2, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)
            elif dice2 == 3:
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(d3, (70,100))
                screen.blit(d3, (145,100))
                screen.blit(move_text, (75,200))
                pygame.display.update()
                pygame.time.delay(5000)

   
        # runs the loop as many times as the value of play_move      
        for i in range (player_move):
            #prints the position of both players, prints the background and updates the screen
            screen.blit(BG,(0,0))
            p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
            p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
            pygame.display.update()
            pygame.time.delay(700)
            
            #increases the value of r which changes the coordinates of the player as they move spaces     
            r = r + 1

            #if r == 41 they have won the game which prints the position of both players then displays a win message and ends the game 
            if r == 41:
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)
                print("p2 wins")
                pygame.draw.rect(screen, WHITE, (0,0,300,350))
                screen.blit(GW, (35,0))
                win_text = font.render("Pink wins", True, BLACK)
                screen.blit(win_text, (125,200))
                pygame.display.update()
                pygame.time.delay(5000)
                player_move = 0
                GameOn = False
                pygame.quit()
                exit()

            #prints the position of both players, prints the background and updates the screen
            else:
                screen.blit(BG,(0,0))
                p1 = pygame.draw.circle(screen, BLUE , (pos_p1[n]), 5)
                p2 = pygame.draw.circle(screen, PINK, (pos_p2[r]), 5)
                pygame.display.update()
                pygame.time.delay(700)

        #changes the value of Turn to switch to the other player so they can take their turn        
        Turn = True


#Allows the user to quit the game when they want
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()









