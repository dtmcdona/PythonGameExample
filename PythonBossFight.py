# name: David McDonald
# start date: 12/30/1016
# last update: 12/31/2016
# description: Rogue Boss Fight

import pygame
import random
import time
import sys
import os

# Load/Store pictures into the game
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
wall = pygame.image.load('wall.png')
archer = pygame.image.load('archer.png')#player
arrow = pygame.image.load('arrow.png')#player arrow
boss1 = pygame.image.load('gargoyle.png')
fireball = pygame.image.load('fireball.png')
firebreath = pygame.image.load('firebreath.png')
firebite = pygame.image.load('firebite.png')
background = pygame.image.load('background.png')
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
GRAY = (150,150,150)
YELLOW = (255,255,0)
 
# --- Classes
# Blocks that are on playing field
class Background(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = background
 
        self.rect = self.image.get_rect()
# Blocks that are on playing field
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = wall
 
        self.rect = self.image.get_rect()
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    HP = 100
    msg = "" # Tells player if they won or lost
    def __init__(self):
        """ Set up the player on creation. """
        pygame.sprite.Sprite.__init__(self)
 
        self.image = archer
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]

# Sample boss but can be modified
class Boss1(pygame.sprite.Sprite):
    """ This class represents the Player. """
    bossDir = True
    HP = 100
    def __init__(self):
        """ Set up the player on creation. """
        pygame.sprite.Sprite.__init__(self)
 
        self.image = boss1
 
        self.rect = self.image.get_rect()

    def update(self):
        """ Update the boss's position. """
        # Set the boss x position to the mouse x position
        self.rect.x, self.bossDir = BossAI(self.rect.x,self.bossDir)

# Player attack bullet
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = arrow
 
        self.rect = self.image.get_rect()

    def Colliding(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def update(self):
        """ Move the bullet. """
        self.rect.y -= 5
        
# Boss attack bullet
class Bullet2(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if boss.HP > 75:
            self.image = fireball
        elif boss.HP > 50:
            self.image = firebreath
        else:
            self.image = firebite
 
        self.rect = self.image.get_rect()

    def Colliding(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def update(self):
        """ Move the bullet. """
        self.rect.y += 5

# --- Functions
      
# Simple boss movement and attack system
def BossAI(bossX, bossDir):
    #Boss movement
    rand = random.randint(1, 100)
    if rand > 99:
        bossDir = not bossDir
    if bossX <=1:
        bossDir = True
    if bossX >=700:
        bossDir = False
    if bossDir == True:#travel right
        bossX += 5
    elif bossDir == False:#travel left
        bossX -= 5
    #Boss attack
    rand = random.randint(1, 100)
    if rand > 90:
        bullet = Bullet2()
        # Set the bullet so it is where the boss is
        bullet.rect.x = boss.rect.x+48
        bullet.rect.y = boss.rect.y+100
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
    
    return bossX, bossDir

# HealthBars to add to player and boss
def HealthBars(player_health, boss_health):
    if player_health > 75:
        player_health_color = GREEN
    elif player_health > 50:
        player_health_color = YELLOW
    else:
        player_health_color = RED
        
    if boss_health > 75:
        boss_health_color = GREEN
    elif boss_health > 50:
        boss_health_color = YELLOW
    else:
        boss_health_color = RED
    #Draw player HP
    pygame.draw.rect(screen, player_health_color, (player.rect.x-34,player.rect.y+52, player_health, player.rect.y+52))
    #Draw boss HP
    pygame.draw.rect(screen, boss_health_color, (boss.rect.x, boss.rect.y+120, boss_health, boss.rect.y))             

def MainMenu():
    screen_text = font.render('Rogue Boss Fights!', True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width/10])
    screen_text = font.render(player.msg, True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width*2/10])
    screen_text = font.render('To play NOOB mode press 1', True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width*3/10])
    screen_text = font.render('To play MEDIUM mode press 2', True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width*4/10])
    screen_text = font.render('To play HARD mode press 3', True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width*5/10])
    screen_text = font.render('To play HARDCORE mode press 4', True, RED)
    screen.blit(screen_text, [screen_width/2,screen_width*6/10])

# --- Create the window
 
# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
# Name the window
pygame.display.set_caption('Rogue Boss Fights')

font = pygame.font.SysFont(None, 25)
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()

# Background layer
background_image = Background()
background_list = pygame.sprite.Group()
background_list.add(background_image)
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)+125
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create a player and boss
player = Player()
all_sprites_list.add(player)
player_damage = 5
boss = Boss1()
all_sprites_list.add(boss)
boss_damage = 20
player.rect.y = 525
boss.rect.y = 25
def main():
    # Loop until the user clicks the close button.
    bossFight = True
    inFight = False
    # -------- Main Menu ----------
    while not inFight:
        player.HP = 100
        boss.HP = 100
        background_list.draw(screen)
        MainMenu()
        pygame.display.update()
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_damge = 10
                    boss_damage = 20
                    inFight = True
                if event.key == pygame.K_2:
                    player_damge = 7
                    boss_damage = 25
                    inFight = True
                if event.key == pygame.K_3:
                    player_damge = 5
                    boss_damage = 50
                    inFight = True
                if event.key == pygame.K_4:
                    player_damge = 5
                    boss_damage = 100
                    inFight = True
             
            
    # -------- Main Game Loop -----------
    while bossFight:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x+16
                bullet.rect.y = player.rect.y-25
                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
     
        # --- Game logic
        
        # Call the update() method on all the sprites
        all_sprites_list.update()
     
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
     
            # See if it hit a block
            block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
            # For each block hit, remove the bullet and add to the score
            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            # For every time player is hit
            if bullet.Colliding(player):
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                player.HP -= boss_damage
            # For every time boss is hit
            if bullet.Colliding(boss):
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                boss.HP -= player_damage
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            if bullet.rect.y > 600:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
     
        # --- Draw a frame
     
        # Clear the screen
        background_list.draw(screen)
     
        # Draw all the spites
        all_sprites_list.draw(screen)

        # Draw health bars
        HealthBars(player.HP, boss.HP)
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

        # --- Restart the game when player or boss dies
        if player.HP <= 0 or boss.HP <= 0:
            # Tell player if they won or lost
            if player.HP <= 0:
                player.msg = "You died a horrible death."
            if boss.HP <= 0:
                player.msg = "The boss got rekt by your skills!"
            # Clear all remaining blocks and bullets
            for bullet in bullet_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
            for block in block_list:
                block_list.remove(block)
                all_sprites_list.remove(block)
            # Remake block field
            for i in range(50):
                # This represents a block
                block = Block(BLUE)
             
                # Set a random location for the block
                block.rect.x = random.randrange(screen_width)
                block.rect.y = random.randrange(350)+125
             
                # Add the block to the list of objects
                block_list.add(block)
                all_sprites_list.add(block)
            main()
main()
pygame.quit()
