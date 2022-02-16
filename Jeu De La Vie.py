import sys, pygame, copy
from time import sleep

pygame.display.init()

WidthGrille = 80
HeigthGrille= 80

grille = {}

for i in range(HeigthGrille):
    grille[i] = [0] * WidthGrille
    
nbcellule = 0

grille2 = {}
grille2 = copy.deepcopy(grille)

size = (680, 800)
Width = len(grille[0])
Height= len(grille)
taillepixelX = size[0]//Width
taillepixelY = size[1]//Height

ecran = pygame.display.set_mode((size[0]-3*taillepixelX, size[1]-taillepixelY))

keystate = pygame.key.get_pressed()
Work = False

PixelX = {}
PixelY = {}
PixelXFin = {}
PixelYFin = {}

for ligne in range(1, Height-1):
    for colonne in range(1, Width-1):
        PixelX[colonne] = colonne*taillepixelX 
        PixelY[ligne] = ligne*taillepixelY
        PixelXFin[colonne] = (colonne+1)*taillepixelX 
        PixelYFin[ligne] = (ligne+1)*taillepixelY

print(PixelX, PixelY, PixelXFin, PixelYFin)

for ligne in range(1, Height-1):
    for colonne in range(1, Width-1):
        
        if grille[ligne][colonne] == 0:
            pygame.draw.rect(ecran, "black", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne])))
        else:
            pygame.draw.rect(ecran, "white", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne])))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Work = True
            if event.key == pygame.K_s:
                Work = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if grille[pos[1]//taillepixelY][pos[0]//taillepixelX] == 1:
                grille[pos[1]//taillepixelY][pos[0]//taillepixelX] = 0
            else:
                grille[pos[1]//taillepixelY][pos[0]//taillepixelX] = 1
            grille2 = copy.deepcopy(grille)

            for ligne in range(1, Height-1):
                for colonne in range(1, Width-1):
                    
                    if grille[ligne][colonne] == 0:
                        pygame.draw.rect(ecran, "black", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne])))
                    else:
                        pygame.draw.rect(ecran, "white", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne])))

    if Work == True:
        for ligne in range(1, Height-1):
            for colonne in range(1, Width-1):
                
                if grille[ligne][colonne] == 0:
                    pygame.draw.rect(ecran, "black", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne])))
                else:
                    pygame.draw.rect(ecran, "white", ((PixelX[colonne], PixelY[ligne]), (PixelXFin[colonne], PixelYFin[ligne]))) 
                    
                nbcellule = grille[ligne-1][colonne-1] + grille[ligne][colonne-1] + grille[ligne+1][colonne-1] + grille[ligne-1][colonne] + grille[ligne+1][colonne] + grille[ligne-1][colonne+1] + grille[ligne][colonne+1] + grille[ligne+1][colonne+1]   

                if nbcellule == 3:
                    grille2[ligne][colonne] = 1
                elif nbcellule != 2:
                    grille2[ligne][colonne] = 0    
        grille = copy.deepcopy(grille2)                

    pygame.display.flip()
