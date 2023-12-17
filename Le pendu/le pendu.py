import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")
pygame.display.set_mode((1080, 720))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


hangman_images = [
    pygame.image.load('img/1.png'),  
    pygame.image.load('img/2.png'),
    pygame.image.load('img/3.png'),
    pygame.image.load('img/4.png'),
    pygame.image.load('img/5.png'),
    pygame.image.load('img/6.png'),
    pygame.image.load('img/7.png')
]


def draw_hangman(attempts):
    
    hangman_status = 6 - attempts
    screen.blit(hangman_images[hangman_status], (WIDTH - 150, 100))


def load_words(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
    return [word.strip().upper() for word in words]


def add_word(filename, word):
    with open(filename, 'a') as file:
        file.write(f"{word.upper()}\n")


def draw_game(chosen_word, guessed, attempts):
    screen.fill(WHITE)

    title = TITLE_FONT.render("Jeu du Pendu", True, BLACK)
    screen.blit(title, (WIDTH/2 - title.get_width()/2, 20))

    
    display_word = " ".join([letter if letter in guessed else "_" for letter in chosen_word])
    word_text = WORD_FONT.render(display_word, True, BLACK)
    screen.blit(word_text, (400, 200))

   
    draw_hangman(attempts)

    pygame.display.update()


def play_game():
    words = load_words("mots.txt")
    chosen_word = random.choice(words)
    guessed = set()
    attempts = 6 
    running = True
    while running:
        draw_game(chosen_word, guessed, attempts)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    guessed.add(event.unicode.upper())
                    if event.unicode.upper() not in chosen_word:
                        attempts -= 1
                        if attempts == 0:
                            running = False
                           

        
        if all(letter in guessed for letter in chosen_word):
            running = False
            


def main_menu():
    menu = True
    while menu:
        screen.fill(WHITE)
        menu_text = LETTER_FONT.render("Appuyez sur P pour Jouer ou A pour Ajouter un Mot", True, BLACK)
        screen.blit(menu_text, (100, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    play_game()
                if event.key == pygame.K_a:
                    add_word("mots.txt")  

        pygame.display.update()

while True:
    main_menu()