import pygame,background,main
from pygame import*
from background import*
from main import*
pygame.init() #lancement de pygame
pygame.display.set_caption("Made in Heaven")
screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
screen_width , screen_height = screen.get_size() 

jeu_en_cours=False
playingGame=False
bricks = []

clock = pygame.time.Clock()

class Brick():
    #attribut de classe un dictionnaire de couleurs
    COLORS = {1: "#64ff96", 2: "#ff6496", 3: "#9664ff"}

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attreibut largeur
        self.pos = pygame.Vector2(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur

    # méthode pour afficher la brique
    def display(self):
        noir=(0,0,0)
        #Rectangle plein coloré
        pygame.draw.rect(screen,self.col,(self.pos.x, self.pos.y, self.w, self.h))
        #Rectangle vide dont lde contour est d'épaisseur 1
        pygame.draw.rect(screen,noir,(self.pos.x, self.pos.y, self.w, self.h),1)



class Ball():

    def __init__(self):# le constructeur
        self.r = 10 #attribut rayon
        self.vel = pygame.Vector2(1, 1)*1 # attribut vitesse
        self.dir = pygame.Vector2(1, 1) # attribut direction
        self.pos = pygame.Vector2(screen_width/2, screen_height/2) # attribut position initiale

    # méthode pour l'actualisation de la position
    def update(self):
        if playingGame == True:
            self.pos.x += self.vel.x*self.dir.x
            self.pos.y += self.vel.y*self.dir.y

    # méthode pour afficher la balle
    def display(self):
        couleurBall=pygame.Color(45, 111, 200)

        pygame.draw.circle(screen,couleurBall,(self.pos.x, self.pos.y),self.r)


    #méthode pour les collision avec les bords
    def checkEdges(self):
        # bord droit
        if (self.pos.x > screen_width - self.r and self.dir.x > 0):
            self.dir.x *= -1 # on change le signe de la direction
        # bord gauche
        if (self.pos.x < self.r and self.dir.x < 0):
            self.dir.x *= -1
        # bord haut
        if (self.pos.y < self.r and self.dir.y < 0):
            self.dir.y *= -1
        # bord bas
        if (self.pos.y > screen_height - self.r and self.dir.y > 0):
            self.dir.y *= -1

    # méthode pour détecter la collision avec le paddle
    def meets(self, paddle):
        if (self.pos.y < paddle.pos.y and
            self.pos.y > paddle.pos.y - self.r and
            self.pos.x > paddle.pos.x - self.r and
            self.pos.x < paddle.pos.x + paddle.w + self.r):
            return True
        else:
            return False

    def meetBricks(self,brick):
        # méthode pour détecter la collision avec la ball

        if (self.pos.y < brick.pos.y +brick.h and
            self.pos.y > brick.pos.y - self.r and
            self.pos.x > brick.pos.x - self.r and
            self.pos.x < brick.pos.x + brick.w + self.r):
            return True
        else:
            return False


class Paddle():

    def __init__(self): # constructeur
        self.w = 120  # attribut longueur du paddle
        self.h = 15   # attribut largeur du paddle
        # la position du paddle avec un objet Pvector
        self.pos = pygame.Vector2(screen_width/2- self.w/2, screen_height - 40) #La position initiale en fonction de la taille de la fenêtre
        self.isMovingLeft = False  # booléen pour mouvement à gauche
        self.isMovingRight = False  # idem à droite
        self.stepSize = 1   # pas pour le déplacement
    # méthode premettant l'affichage
    def display(self):
        # affichage du rectangle rect(x,y,longueur, largeur)
        couleurPaddle=pygame.Color(255, 255, 255)
        pygame.draw.rect(screen,couleurPaddle,(self.pos.x, self.pos.y, self.w, self.h))
     # méthode qui gère le déplacement
    def move(self, step):
        self.pos.x = step + self.pos.x
    # méthode pour actualiser l'affichage des déplacements
    def update(self):
        if self.isMovingLeft:
            self.move(-self.stepSize)
        elif self.isMovingRight:
            self.move(self.stepSize)

    # méthode qui gère les collisions avec les bords
    def checkEdges(self):
        if self.pos.x <= 0:
            self.pos.x = 0
        elif self.pos.x + self.w >= screen_width:
            self.pos.x = screen_width - self.w


fondjeu = Background("B.png",[0,0])

def addBrick(x,y,hits):
    brick = Brick(x,y,hits)
    bricks.append(brick)


for x in range(5, screen_width - 80, 75):
    addBrick(x + 37.5, 50, 3)
    addBrick(x + 37.5, 70, 2)
    addBrick(x + 37.5, 90, 1)





paddle = Paddle()
ball = Ball()

world = True
running = True

while world:
    # Set frame rate limit
    clock.tick(60)  # Limits to 60 frames per second

    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world = False
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
            # Recreate dynamically scaled title and buttons
            update_button_positions(screen_width, screen_height)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if jeu_en_cours:
                    jeu_en_cours = False
                    running = True
                else:
                    world = False

    # Main Menu
    if not jeu_en_cours:
        screen.fill([255, 255, 255])
        screen.blit(background.ground, background.rect)
        # Draw main menu elements
        if screen_state == "main":
            # Draw title and buttons
            title_x, title_y = get_dynamic_title_position(screen_width, screen_height)
            screen.blit(title_img_dynamic, (title_x, title_y))
            if exit_button.draw(screen) and not clicked:
                world = False
            if play_button.draw(screen) and not clicked:
                jeu_en_cours = True
                clicked = True
            if options_button.draw(screen) and not clicked:
                screen_state = "options"
                clicked = True

        # Options screen
        elif screen_state == "options":
            # Draw options elements
            title_x, title_y = get_dynamic_title_position(screen_width, screen_height)
            screen.blit(title_img_dynamic, (title_x, title_y))
            if back_button.draw(screen) and not clicked:
                screen_state = "main"
                clicked = True

        # Draw custom cursor
        pos = pygame.mouse.get_pos()
        screen.blit(new_cursor, pos)

        pygame.display.flip()

    # Game Loop
    if jeu_en_cours:
        screen.fill((100, 40, 70))
        screen.blit(fondjeu.ground, fondjeu.rect)

        # Update and draw paddle
        paddle.display()
        paddle.checkEdges()
        paddle.update()

        # Update and draw ball
        ball.display()
        ball.checkEdges()
        ball.update()

        # Ball and paddle collision
        if ball.meets(paddle):
            if ball.dir.y > 0:
                ball.dir.y = -ball.dir.y

        # Update and draw bricks
        for brick in bricks:
            brick.display()
        for i in range(len(bricks) - 1, -1, -1):
            if ball.meetBricks(bricks[i]):
                bricks.pop(i)
                ball.dir.y *= -1

        # Handle paddle movement
        keys = pygame.key.get_pressed()
        paddle.isMovingLeft = keys[pygame.K_q]
        paddle.isMovingRight = keys[pygame.K_d]

pygame.quit()