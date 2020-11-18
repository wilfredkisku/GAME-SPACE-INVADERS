'''
Wilfred kisku
Icons attributed to flaticon(www.flaticon.com)
'''
import pygame
import random
import math

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('./res/enemy32.png'))
    enemyX.append(random.randint(0,764))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(5)

#bullet
#ready state is when it cannot be seen in the screen
#fire state when in motion
bulletImg = pygame.image.load('./res/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 1
bulletY_change = 5
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 24,y + 2))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2)+math.pow(enemyY-bulletY, 2))
    if distance < 16:
        return True
    else:
        return False

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
                playerX_change = 1
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
	

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736	

    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 764:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,764)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i], enemyY[i], i)	
    
    #bullet movement 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    pygame.display.update()	
