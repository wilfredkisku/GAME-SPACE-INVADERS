'''
Wilfred kisku
Icons attributed to flaticon(www.flaticon.com)
'''
import pygame
import random

pygame.init()

#create the screen, the screen is executed and exits
screen = pygame.display.set_mode((800,600))

#font = pygame.font.Font(pygame.font.get_default_font(), 36)
#text_surface = font.render('Hello world', antialias=True, color=(0, 0, 0))
#screen.blit(text_surface, dest=(0,0))

background = pygame.image.load('./res/background.jpg')

#title and icon 
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('./res/enemy32.png')
pygame.display.set_icon(icon)

#Player X
playerImg = pygame.image.load('./res/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('./res/enemy32.png')
enemyX = random.randint(0,764)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 4
def player(x, y):
	screen.blit(playerImg, (x, y))

def enemy(x, y):
	screen.blit(enemyImg, (x,y))
	
running = True
#check the status of running 
#create a for loop that gets all the events 
#check if the event type is pygame.QUIT that is listened by the listener
#if it is then make the running status to be False
while running:

	screen.fill((0,0,0))	
	#playerX += 0.1
	#listen to a keyboard event
	screen.blit(background, (0,0))	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.3
			if event.key == pygame.K_LEFT:
				playerX_change = -0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	if playerX >= 736:
		playerX = 736	

	enemyX += enemyX_change

	if enemyX <= 0:
		enemyX_change = 0.3
		enemyY += enemyY_change
	if enemyX >= 764:
		enemyX_change = -0.3
		enemyY += enemyY_change

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()	
