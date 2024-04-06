import pygame


class Square:
    def __init__(self, win, x, y, color, name, font, font2):
        self.win=win
        self.x=x
        self.y=y
        self.color=color
        self.name=name
        self.font=font
        self.font2=font2
        self.SqrDi=100

        self.isUsed=0
        self.toggle=False

        self.order1 = ""
        self.order2 = ""

        self.rect = pygame.Rect(self.x, self.y, self.SqrDi, self.SqrDi)
    
    def Draw(self):
        if self.toggle>=1:
            pygame.draw.rect(self.win, self.color, self.rect)
            self.toRender1 = self.font2.render(self.order1, True, "Black")
            self.toRender2 = self.font2.render(self.order2, True, "Black")

            pygame.draw.line(self.win, "black", (self.x, self.y), (self.x+100, self.y+100))

            self.win.blit(self.toRender1, (self.x+20, self.y+50))
            self.win.blit(self.toRender2, (self.x+50, self.y+10))
            
        else:
            pygame.draw.rect(self.win, self.color, self.rect)
            self.toRender = self.font.render(self.order1, True, "Black")
            self.win.blit(self.toRender, (self.x+30, self.y+20))