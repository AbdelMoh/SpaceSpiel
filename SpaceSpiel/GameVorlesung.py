import pygame
import random
import math
class Game :
    def __init__(self, width , height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Space Invedars")
        self.background_Img = pygame.image.load("spr_space_himmel.png")
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship(self,370 ,515)
        self.running = True
        self.enemies = []
        for i in range(12) :
            self.enemies.append(Enemy(self,random.randint(0,736),random.randint(30,130)))


        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_Img ,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT :
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT :
                        self.spaceship.move(10)
                    if event.key == pygame.K_SPACE :
                        self.spaceship.fired_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(-10)

            self.spaceship.update()
            if len(self.spaceship.bullets) > 0 :
                for bullet in self.spaceship.bullets :
                    if bullet.ist_fired == True :
                        bullet.update()
                    else :
                        self.spaceship.bullets.remove(bullet)
            for enemy in self.enemies :
                enemy.update()
                enemy.checkcollision()
                if enemy.y > 500 :
                    for k in self.enemies :
                        k.y = 1000
                    self.print_game_over()
                    break

            pygame.display.update()

    def print_game_over(self):
        get_font = pygame.font.Font("freesansbold.ttf",64)
        get_text = get_font.render("GAME OVER",True,(255,255,255))
        self.screen.blit(get_text,(200,250))
class Spaceship :
       def __init__(self,game,x ,y ):
           pygame.init()
           self.x = x
           self.y = y
           self.change = 0
           self.game = game
           self.spaceship_Img = pygame.image.load("spr_spaceship.png")
           self.bullets = []
       def fired_bullet(self):
           self.bullets.append(Bullet(self.game,self.x,self.y))
           self.bullets[len(self.bullets)-1].fire()

       def move(self, speed):
           self.change += speed
       def update (self):
           self.x += self.change
           if self.x < 0 :
               self.x = 730
           if self.x > 730 :
               self.x = 0
           self.game.screen.blit(self.spaceship_Img,(self.x,self.y))

class Bullet :
      def __init__(self,game,x ,y) :
          self.x = x
          self.y = y
          self.game = game
          self.ist_fired = False
          self.bullet_speed = 10
          self.bullet_img = pygame.image.load("spr_patrone.png")
      def fire (self) :
          self.ist_fired = True

      def update(self):
          self.y -= self.bullet_speed
          if self.y < 0 :
              self.ist_fired = False
          self.game.screen.blit(self.bullet_img,(self.x,self.y))

class Enemy :
     def __init__(self,game,x,y):
         self.x = x
         self.y = y
         self.change_x = 5
         self.change_y = 60
         self.game = game
         self.enemy_img = pygame.image.load("spr_space_enemy.png")
     def checkcollision(self):
         for bullet in self.game.spaceship.bullets :
             distance = math.sqrt(math.pow(self.x - bullet.x,2)+math.pow(self.y - bullet.y,2))
             if distance < 35 :
                bullet.ist_fired = False
                self.x = random.randint(0,736)
                self.y = random.randint(50,150)


     def update(self):
         self.x += self.change_x
         if self.x > 736 :
            self.y += self.change_y
            self.change_x = -5
         if self.x < 0:
             self.y += self.change_y
             self.change_x = 5
         self.game.screen.blit(self.enemy_img,(self.x,self.y))


if __name__ == "__main__" :
    game = Game(800,600)
