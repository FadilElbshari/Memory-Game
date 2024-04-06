import pygame
import random
import start as start
import Scripts.square as square

from pygame import time
from pygame import mixer

def imageLoad(path, w, h):
    return pygame.transform.scale(pygame.image.load(f"{path}"), (w, h))

def useFont(type, size):
    return pygame.font.SysFont(type, size)


pygame.init()
mixer.init()

WIDTH, HEIGHT = 750, 650

FPS = 60.0
clk = time.Clock()

correct = r"Sound\correct.mp3"
wrong = r"Sound\wrong.mp3"

colors = [(211, 211, 211), (229, 228, 226)]
Font = useFont("DDC HARDWARE", 100)
Font2 = useFont("DDC HARDWARE", 60)
Font3 = useFont("DDC HARDWARE", 75)


bg = imageLoad(r"Images\bg.jpg", WIDTH, HEIGHT)
fullH = imageLoad(r"Images\fullH.png", 70, 70)
twoThirdsH = imageLoad(r"Images\twoThirdsH.png", 70, 70)
oneTthirdH = imageLoad(r"Images\oneThirdH.png", 70, 70)
emptyH = imageLoad(r"Images\heart.png", 70, 70)

Hlevels = [fullH, twoThirdsH, oneTthirdH, emptyH]

vOn = imageLoad(r"Images\vOn.png", 40, 40)
vOff = imageLoad(r"Images\vOff.png", 40, 40)

Vlevels = [vOff, vOn]

fullM = imageLoad(r"Images\fullM.png", 40, 40)
twoThirdsM = imageLoad(r"Images\twoThirdsM.png", 40, 40)
oneTthirdM = imageLoad(r"Images\oneThirdM.png", 40, 40)
emptyM = imageLoad(r"Images\emptyM.png", 40, 40)

Mlevels = [fullM, twoThirdsM, oneTthirdM, emptyM]

def MainFunc():
    Win = pygame.display.set_mode((WIDTH, HEIGHT))

    def PlaySound(file, vol):
        mixer.music.load(file)
        mixer.music.set_volume(vol)
        mixer.music.play()

    def DrawBoard(squares, rows):
        x=0
        for i, row in enumerate(range(125, WIDTH-200, 100)):
            for j, col in enumerate(range(100, HEIGHT-100, 100)):
                squares.append(square.Square(Win, row, col, colors[x%2], f"{rows[i]}{5-j}", Font, Font3))
                x+=1

    def DrawNotation(rows):
        for i in range(5):
            Win.blit(Font2.render(f"{5-i}", True, "Black"), (85, 130+100*i))
            Win.blit(Font2.render(f"{rows[i]}", True, "Black"), (160+100*i, HEIGHT-50))

    mousePos = [0, 0]

    squares = []
    rows = "abcde"

    isAllowed = False
    toReset = False
    allowReset = False

    level = 1
    timer = 0
    lives = 3
    vol = 1
    sec = 0

    run = True

    DrawBoard(squares, rows)
    DrawNotation(rows)

    sequence = [f"{random.choice(rows)}{random.randint(1, 5)}" for _ in range(level)]
    print(sequence)

    while run:

        clk.tick(FPS)
        pygame.display.update()
        Win.fill((115, 147, 179))

        timer+=1/60
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos[0], mousePos[1] = pygame.mouse.get_pos()
                for sqr in squares:
                    if (mousePos[0] > sqr.x and mousePos[0] < sqr.x+100) and (mousePos[1] > sqr.y and mousePos[1] < sqr.y+100)  and isAllowed:
                        if len(sequence)>0:
                            if sqr.name == sequence[0] and sqr.isUsed<1:
                                PlaySound(correct, vol)
                                sqr.color = (80, 200, 120)
                                sqr.order1 = str(level - len(sequence) + 1)
                                sqr.isUsed +=1 
                                sequence.pop(0)
                            
                            elif sqr.name == sequence[0] and sqr.isUsed>=1:
                                PlaySound(correct, vol)
                                sqr.order2 = str(level - len(sequence) + 1) 
                                sqr.toggle = True
                                sequence.pop(0)
                            
                            else:
                                PlaySound(wrong, vol)
                                lives-=1

                    elif (mousePos[0] > WIDTH-100 and mousePos[0] < WIDTH-60) and (mousePos[1] > 20 and mousePos[1] < 60):
                        vol = (vol+1)%2
                    
                    elif (mousePos[0] > 320 and mousePos[0] < 320+115) and (mousePos[1] > 20 and mousePos[1] < 70) and allowReset:
                        toReset = True
  
        if toReset:
            level+=1
            sequence = [f"{random.choice(rows)}{random.randint(1, 5)}" for _ in range(level)]
            print(sequence)
            squares = []
            DrawBoard(squares, rows)
            toReset=False
            timer=0
            isAllowed=False
            lives=3
            sec=0

        for sqr in squares:
            sqr.Draw()

        if timer<3:
            
            for i in range(len(sequence)):
                sequenceRender = Font2.render(f"{sequence[i]}", True, "Gold")
                Win.blit(sequenceRender, ((WIDTH-((level+1)*75))/2+30+75*i, 30))
            if timer>1 and timer<2:
                sec=1
            elif timer>2 and timer<3:
                sec=2
 
        else:
            isAllowed = True
            sec=3


        if lives>=0:
            Win.blit(Hlevels[3-lives], (20, 20))
        else:
            break

        if len(sequence)<1:
            pygame.draw.rect(Win, "black", (320, 20, 115, 50))
            Win.blit(Font2.render("NEXT", True, "white"), (320, 25))
            allowReset=True

        Win.blit(Vlevels[vol], (WIDTH-100, 20))
        Win.blit(Mlevels[sec], (WIDTH-100, 100))
        DrawNotation(rows)

if __name__=="__main__":
    start.StartUp()
