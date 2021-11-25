import pygame
import os

from pygame import event
pygame.font.init()
pygame.mixer.init()


class Goku():
    def __init__(self, screen, char_width, char_height, vel, screen_border, screen_height):
        self.screen = screen
        self.char_width = char_width
        self.char_height = char_height
        self.velocity = vel
        self.screen_border = screen_border
        self.screen_height = screen_height

        self.goku_img_load = pygame.image.load(
            os.path.join('Assets', 'def_goku.png'))

        self.goku_img = pygame.transform.rotate(pygame.transform.scale(
            self.goku_img_load, (self.char_width, self.char_height)), 0)

    def goku_movement(self, key_pressed, goku_char):
        # key_pressed = key_pressed

        # if key pressed "a" move to left
        if key_pressed[pygame.K_a] and goku_char.x - self.velocity > 0:  # left
            goku_char.x -= self.velocity
            # print(goku_char.x)

        # if key pressed "d" move to right
        if key_pressed[pygame.K_d] and goku_char.x + self.velocity + goku_char.width < self.screen_border.x:  # Right
            goku_char.x += self.velocity

        # if key pressed "w" move up
        if key_pressed[pygame.K_w] and goku_char.y - self.velocity > 0:  # UP
            goku_char.y -= self.velocity

        # if key pressed "s" move down
        if key_pressed[pygame.K_s] and goku_char.y + self.velocity + goku_char.height < self.screen_height - 15:  # DOWN
            goku_char.y += self.velocity

    def ki_blast_handle(self, event, max_ki, ki_vel, goku_ki_blast, goku_char):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(goku_ki_blast) < max_ki:
                ki_blast = pygame.Rect(
                    goku_char.x + goku_char.width, goku_char.y +
                    goku_char.height // 2 - 2, 20, 20
                )
                goku_ki_blast.append(ki_blast)
                ki_sound = pygame.mixer.Sound('Assets/goku_ki_blast.mp3')
                ki_sound.play()

    def blast_func(self, goku_ki_blast, ki_vel, vegeta_char, Vegeta_HIT, screen_width):
        for ki in goku_ki_blast:
            ki.x += ki_vel
            if vegeta_char.colliderect(ki):
                pygame.event.post(pygame.event.Event(Vegeta_HIT))
                # print("True") // it does collide.
                goku_ki_blast.remove(ki)
            elif ki.x > screen_width:
                goku_ki_blast.remove(ki)


class Vegeta():
    def __init__(self, screen, char_width, char_height, vel, screen_border, screen_width, screen_height):
        self.screen = screen
        self.char_width = char_width
        self.char_height = char_height
        self.velocity = vel
        self.screen_border = screen_border
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.vegeta_img_load = pygame.image.load(
            os.path.join('Assets', 'vegeta_.png'))

        self.vegeta_img = pygame.transform.rotate(pygame.transform.scale(
            self.vegeta_img_load, (self.char_width, self.char_height)), 0)

    def vegeta_movement(self, key_pressed, vegeta_char):
        # key_pressed = key_pressed

        # if key pressed "a" move to left
        if key_pressed[pygame.K_LEFT] and vegeta_char.x - self.velocity > self.screen_border.x + self.screen_border.width:  # left
            vegeta_char.x -= self.velocity
            # print(goku_char.x)

        # if key pressed "d" move to right
        if key_pressed[pygame.K_RIGHT] and vegeta_char.x + self.velocity + vegeta_char.width < self.screen_width:  # Right
            vegeta_char.x += self.velocity

        # if key pressed "w" move up
        if key_pressed[pygame.K_UP] and vegeta_char.y - self.velocity > 0:  # UP
            vegeta_char.y -= self.velocity

        # if key pressed "s" move down
        if key_pressed[pygame.K_DOWN] and vegeta_char.y + self.velocity + vegeta_char.height < self.screen_height - 15:  # DOWN
            vegeta_char.y += self.velocity

    def ki_blast_handle(self, event, max_ki, ki_vel, vegeta_ki_blast, vegeta_char):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL and len(vegeta_ki_blast) < max_ki:
                ki_blast = pygame.Rect(
                    vegeta_char.x, vegeta_char.y + vegeta_char.height // 2 - 2, 20, 20
                )
                vegeta_ki_blast.append(ki_blast)
                ki_sound = pygame.mixer.Sound('Assets/vegeta_ki_blast.mp3')
                ki_sound.play()

    def blast_func(self, vegeta_ki_blast, ki_vel, goku_char, Goku_HIT):
        for ki in vegeta_ki_blast:
            ki.x -= ki_vel
            if goku_char.colliderect(ki):
                pygame.event.post(pygame.event.Event(Goku_HIT))
                # print("True") // it does collide.
                vegeta_ki_blast.remove(ki)
            elif ki.x < 0:
                vegeta_ki_blast.remove(ki)


class Winner():
    def __init__(self, vegeta_health, goku_health, winner_font, screen, screen_width, screen_height):

        self.vegeta_health = vegeta_health
        self.goku_health = goku_health
        self.winner_font = winner_font
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.winner_text = ""

        if vegeta_health <= 0:
            self.winner_text = "Kakarot Wins"

        if goku_health <= 0:
            self.winner_text = "The Almighty Prince Wins"

        if self.winner_text != "":
            # Winner.draw_winner(self,self.winner_text)

            # def draw_winner(self, text):
            draw_text = self.winner_font.render(
                self.winner_text, 1, (255, 255, 255))
            self.screen.blit(draw_text, (self.screen_width/2 - draw_text.get_width() /
                                         2, self.screen_height/2 - draw_text.get_height()/2))
    # pygame.display.update()
    pygame.time.delay(5000)


class Window():
    def __init__(self, screen, screen_border, screen_width, screen_height, vegeta_char, goku_char, goku_img, vegeta_img, goku_ki_blast, vegeta_ki_blast, vegeta_health, goku_health, health_font):
        # super().__init__(Goku.screen, Goku.char_width, Goku.char_height)
        self.screen = screen

        self.screen_border = screen_border

        background = pygame.transform.scale(pygame.image.load(
            os.path.join('Assets', 'background.jpg')), (screen_width, screen_height))

        # Background show image
        self.screen.fill((0, 0, 0))
        self.screen.blit(background, (0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.screen_border)

        vegeta_health_text = health_font.render(
            "Health: " + str(vegeta_health), 1, (255, 255, 255)
        )
        vegeta_text_width = vegeta_health_text.get_width()

        goku_health_text = health_font.render(
            "Health: " + str(goku_health), 1, (255, 255, 255)
        )
        self.screen.blit(vegeta_health_text,
                         (screen_width - vegeta_text_width - 10, 10))
        self.screen.blit(goku_health_text, (10, 10))

        self.screen.blit(goku_img, (goku_char.x, goku_char.y))
        self.screen.blit(vegeta_img, (vegeta_char.x, vegeta_char.y))

        for ki in goku_ki_blast:
            pygame.draw.ellipse(screen, (255, 0, 0), ki)

        for ki in vegeta_ki_blast:
            pygame.draw.ellipse(screen, (255, 169, 0), ki)

        # pygame.time.delay(5000)
        pygame.display.update()


def main():
    screen_width, screen_height = 1280, 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dragon Ball Shooter")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    screen_border = pygame.Rect(screen_width//2-5, 0, 10, screen_height)

    health_font = pygame.font.SysFont('comicsans', 40)
    Winner_font = pygame.font.SysFont('comicsans', 100)
    FPS = 60
    vel = 20
    ki_vel = 50
    max_ki = 3
    char_width, char_height = 100, 150

    Goku_HIT = pygame.USEREVENT + 1
    Vegeta_HIT = pygame.USEREVENT + 2

    # Yellow = goku        Red = Vegeta
    vegeta_char = pygame.Rect(700, 300, char_width, char_height)
    goku_char = pygame.Rect(100, 300, char_width, char_height)

    vegeta_ki_blast = []
    goku_ki_blast = []

    vegeta_health = 10
    goku_health = 10

    clock = pygame.time.Clock()
    background_music = pygame.mixer.Sound(
        "Assets/dragon_ball_super_background.mp3")
    background_music.set_volume(0.25)
    background_music.play(loops=-1)
    run = 1
    while run:
        clock.tick(FPS)
        goku = Goku(screen, char_width, char_height,
                    vel, screen_border, screen_height)
        vegeta = Vegeta(screen, char_width, char_height, vel,
                        screen_border, screen_width, screen_height)

        keys_pressed = pygame.key.get_pressed()
        goku.goku_movement(keys_pressed, goku_char)
        vegeta.vegeta_movement(keys_pressed, vegeta_char)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0

            # for shoot_event in pygame.event.get():
            goku.ki_blast_handle(event, max_ki, ki_vel,
                                 goku_ki_blast, goku_char)
            vegeta.ki_blast_handle(event, max_ki, ki_vel,
                                   vegeta_ki_blast, vegeta_char)

            if event.type == Vegeta_HIT:
                vegeta_health -= 1
                # vegeta_hit_sound = pygame.mixer.Sound(
                #     'Assets/vegeta_sound.mp3')
                # vegeta_hit_sound.play()

            if event.type == Goku_HIT:
                goku_health -= 1
                # goku_hit_sound = pygame.mixer.Sound(
                #     'Assets/goku_scream.mp3')
                # goku_hit_sound.play()

        winner_text = ""

        if vegeta_health < 0:
            winner_text = "Kakarot Wins"

        if goku_health < 0:
            winner_text = "The Almighty Prince Wins"
            vegeta_win = pygame.mixer.Sound(
                'Assets/I am Prince of all sayains (1).mp3')
            vegeta_win.play()

        if winner_text != "":
            # draw_winner(winner_text)
            draw_text = Winner_font.render(winner_text, 1, (255, 0, 0))
            screen.blit(draw_text, (screen_width/2 - draw_text.get_width() /
                                    2, screen_height/2 - draw_text.get_height()/2))
            background_music.stop()
            pygame.display.update()
            pygame.time.delay(3500)
            break

        goku.blast_func(goku_ki_blast, ki_vel, vegeta_char,
                        Vegeta_HIT, screen_width)
        vegeta.blast_func(vegeta_ki_blast, ki_vel, goku_char, Goku_HIT)

        windows = Window(screen, screen_border, screen_width, screen_height, vegeta_char, goku_char, goku.goku_img,
                         vegeta.vegeta_img, goku_ki_blast, vegeta_ki_blast, vegeta_health, goku_health, health_font)

        # pygame.display.update()


if __name__ == "__main__":
    main()
