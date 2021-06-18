import sys
input = sys.stdin.readline
import math
import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (155,155,102)
green = (0,255,0)

width = 800
height = 600
dis = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()

block_len = 10
snake_speed = 20

font_style = pygame.font.SysFont(None,40)
score_font = pygame.font.SysFont(None,50)

def your_score(score):
	val = score_font.render('Your Score: '+ str(score), True, yellow)
	dis.blit(val, [0,0])

def our_snake(block_len,snake_list):
	for x in snake_list:
		pygame.draw.rect(dis,black,[x[0], x[1], block_len, block_len])

def message(msg,color):
	m = font_style.render(msg, True, color)
	dis.blit(m, [width / 6, height / 3])

def game_loop():
	game_over = False
	game_close = False

	x1 = width/2
	y1 = height/2

	x1_change = 0
	y1_change = 0

	snake_list = []
	Length_snake = 1

	foodx = round(random.randrange(0, width)/10.0)*10.0
	foody = round(random.randrange(0, height)/10.0)*10.0



	while not game_over:

		while game_close == True:
			dis.fill(white)
			message('You Lost! Press Q-Quit or C-Play Again', red)
			your_score(Length_snake - 1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						game_loop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x1_change = -block_len
					y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = block_len
					y1_change = 0
				elif event.key == pygame.K_UP:
					x1_change = 0
					y1_change = -block_len
				elif event.key == pygame.K_DOWN:
					x1_change = 0
					y1_change = block_len
		if x1 >= width or x1 < 0 or y1 >= height or y1< 0:
			game_close = True

		x1 += x1_change
		y1 += y1_change
		dis.fill(white)
		pygame.draw.rect(dis,green,[foodx,foody,block_len,block_len])
		
		# pygame.draw.rect(dis,black,[x1,y1,block_len,block_len])
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)
		if len(snake_list) > Length_snake:
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				game_close = True

		our_snake(block_len,snake_list)
		your_score(Length_snake - 1)
		pygame.display.update()

		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0,width)/10.0)*10.0
			foody = round(random.randrange(0,height)/10.0)*10.0
			Length_snake += 1
			# print('Got Food!')
		clock.tick(snake_speed+10)

# message("You lost", red)
# pygame.display.update()
# pygame.time.wait(1000)
# time.sleep(20)
	pygame.quit()
	quit()

game_loop()