import pygame
import time
import random

pygame.init()  # initialize the library

white = (255, 255, 255)  # colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600  # screen dimensions
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))  # screen creation
pygame.display.set_caption('My Snake Game')  # title

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 20  # speed of snake

font_style = pygame.font.SysFont("bahnschrift", 25)  # fonts
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):  # function which counts the score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):  # function which adds rectangles to snake
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):  # gives message about losing game
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():  # base function
    game_over = False
    game_close = False

    x1 = dis_width / 2  # coordinates in the beginning
    y1 = dis_height / 2

    x1_change = 0  # coordinates' change
    y1_change = 0

    snake_List = []
    Length_of_snake = 1  # current snake length

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # random food coordinates
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:  # main loop

        while game_close == True:
            dis.fill(blue)  # display color
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)  # counting the score
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # when we press q, we quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # when ewe press c, we restart the game
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # buttons to click to move
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # loosing game when Snake hits the boundaries
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # display color
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:  # check if we ate the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # change the food coords
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # increase snake length

        clock.tick(snake_speed)  # set snake speed

    pygame.quit()
    quit()


gameLoop()