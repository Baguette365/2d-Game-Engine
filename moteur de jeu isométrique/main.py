#importer tout les composants du programme et importer pygame
import sys
import pygame
import pygame as pg
import src.settings

#la classe principal ou la boucle principale est crée
class Game:
    def __init__(self):
        #initialiser pygame et le préparer a l'executer
        pg.init()

        #créer la fenetre de jeu(en définissant sa résolution)
        #le src.settings.res revient a dire de chercher la variable res dans le fichier settings(paramettre en anglais) contenue dans le dossier src(pour code sources)
        self.w = pg.display.set_mode(src.settings.res) #on l'appelle w pour window(fenetre en anglais) car c'est plus rapide
    #crée la ou le moteur sera mis a jour
    def mettre_a_jour(self):
        pass
    #afficher toutes les images(celles du joueurs, des enemies, de la map...)
    def afficher_tout(self):
        pass
    #permet de mettre tout les évènements dans une méthode(fonction) séparée
    def évènements(self):
        #récupère tout les évenement et les stockes une a une dans la variable event
        #exemple:
        # si la touche H et la touche B
        # d'abord event=pygame.K_H puis event=pygame.K_B
        for event in pg.event.get():
            #vue que la variable va changée pour chaque touches qui est pressée, on verrifie avec des conditions si c'est cette touche qui est pressée et pas une autre
            #meme si cela peut parraitre bizzare
            #la on voit si la feunetre tente d'etre fermée(grace a la croix sur windows/mac/linux)
            if event.type == pygame.QUIT:
                #ferme la fenetre
                pygame.quit()
                #ferme le programme
                sys.exit()
    #boucle principale du jeu
    def boucle(self):
        while True:
            self.mettre_a_jour()
            self.évènements()
            self.afficher_tout()


#on crée la class
game = Game()
#on lance le jeu
game.boucle()


























