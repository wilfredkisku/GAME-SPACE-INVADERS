import pygame

pygame.init()

#create the screen, the screen is executed and exits
screen = pygame.display.set_mode((800,600))

#title and icon 
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('./res/ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('./res/space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
	screen.blit(playerImg, (x, y))

running = True
#check the status of running 
#create a for loop that gets all the events 
#check if the event type is pygame.QUIT that is listened by the listener
#if it is then make the running status to be False
while running:

	screen.fill((0,0,0))	
	#playerX += 0.1
	#listen to a keyboard event
	
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

	player(playerX, playerY)
	pygame.display.update()	