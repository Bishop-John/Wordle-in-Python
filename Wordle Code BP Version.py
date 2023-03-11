import random, pygame, sys
from pygame.locals import *
pygame.init()

WHITE  = [255, 255, 255]
BLACK  = [0  , 0  , 0  ]
GREEN  = [0  , 255, 0  ]
YELLOW = [255, 255, 102]
GREY   = [128, 128, 128]
LGREEN = [153, 255, 204]

font = pygame.font.SysFont("Arial", 40)
bigFont = pygame.font.SysFont("Arial", 80)

youWin     = bigFont.render("You Win!", True, LGREEN)
youLose    = bigFont.render("You Lose!", True, LGREEN)
playAgain  = bigFont.render("Play Again?", True, LGREEN)

clock = pygame.time.Clock()
gameDisplayHeight, gameDisplayWidth = 600, 500
gameDisplay = pygame.display.set_mode((gameDisplayWidth, gameDisplayHeight))

def checkGuess(turns, word, userGuess, gameDisplay):
    renderList = ["","","","",""]
    spacing = 0
    guessColourCode = [GREY,GREY,GREY,GREY,GREY]

    for x in range(0,5):
        if userGuess[x] in word:
            guessColourCode[x] = YELLOW
        if word[x] == userGuess[x]:
            guessColourCode[x] = GREEN

    list(userGuess)
    for x in range(0,5):
        renderList[x] = font.render(userGuess[x], True, BLACK)
        pygame.draw.rect(gameDisplay, guessColourCode[x], pygame.Rect(60 +spacing, 50+ (turns*80), 50, 50))
        gameDisplay.blit(renderList[x], (70 + spacing, 50 + (turns*80)))
        spacing+=80

    if guessColourCode == [GREEN, GREEN, GREEN, GREEN, GREEN]:
        return True

def gameLoop():
    file = open("5 Letter Words.txt", "r")
    wordList = file.readlines()
    word = wordList[random.randint(0, len(wordList)-1)].upper()
    guess = ""
    answer = word
    
    
    #print(word)
    
    gameDisplay.fill(BLACK)
    for i in range(0,5):
        for i2 in range(0,6):
            pygame.draw.rect(gameDisplay, GREY, pygame.Rect(60+(i*80), 50+(i2*80), 50, 50),2)

    turns = 0
    win = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                guess += event.unicode.upper()

                if event.key == pygame.K_RETURN and win == True:
                    gameLoop()          
                if event.key == pygame.K_RETURN and turns == 6:
                    gameLoop()
                if event.key == pygame.K_BACKSPACE or len(guess) > 6:#Broken
                    guess = guess[:-2]
                if event.key == pygame.K_RETURN and len(guess) > 4:
                    win = checkGuess(turns, word, guess, gameDisplay)
                    turns += 1
                    guess = ""
                    gameDisplay.fill(BLACK, (0, 500, 500, 200))
                                       
        gameDisplay.fill(BLACK, (0, 500, 500, 200))#unneeded?
        renderGuess = font.render(guess, True, GREY)
        gameDisplay.blit(renderGuess, (180, 530))

        if win == True:
            gameDisplay.blit(youWin,(90,200))
            gameDisplay.blit(playAgain,(60,300))

        if turns == 6 and win != True:
            gameDisplay.blit(youLose, (90, 200))
            gameDisplay.blit(playAgain, (60, 300))
            showAnswer = font.render("Answer was " + str(answer[:-1]), True, LGREEN)
            gameDisplay.blit(showAnswer, (60, 520))
                   
        pygame.display.update()
        clock.tick(30)

gameLoop()
