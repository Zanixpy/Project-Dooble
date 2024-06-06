import random

class cartes:
    def __init__(self, nomJoueur):
        self.nomJoueur = nomJoueur
        self.paquetDeCartes = []
        symboles = ["coeur", "sandale", "ramen", "carré", "flamme", "champignon", "étoile", "katana", "couronne", "ordinateur", "carapace", "fusée", "dragon ball", "lune", "dauphin", "clé", "panthère", "ours", "singe", "gumball", "maracas", "statue", "fraise", "kart", "tuyau", "fleur", "yoshi", "darwin", "colisée", "excalibur", "trompette", "chapeau", "éclair", "bloc", "glider", "sac", "soleil", "lit", "TV", "PI" ]
        choix = random.randint(0, 39)
        carte_temp = []
        for i in range(15):
            for i in range(5):
                while symboles[choix] in carte_temp:
                    choix = random.randint(0, 39)
                carte_temp.append(symboles[choix])
            self.paquetDeCartes.append(carte_temp)
            carte_temp = []

class dobble:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.carteDepart = []
        self.symboles = ["coeur", "sandale", "ramen", "carré", "flamme", "champignon", "étoile", "katana", "couronne", "ordinateur", "carapace", "fusée", "dragon ball", "lune", "dauphin", "clé", "panthère", "ours", "singe", "gumball", "maracas", "statue", "fraise", "kart", "tuyau", "fleur", "yoshi", "darwin", "colisée", "excalibur", "trompette", "chapeau", "éclair", "bloc", "glider", "sac", "soleil", "lit", "TV", "PI" ]

    def carteDeDepart(self):
        choixSymbole = random.randint(0, 39)
        for i in range(5):
            while self.symboles[choixSymbole] in self.carteDepart:
                choixSymbole = random.randint(0, 39)
            self.carteDepart.append(self.symboles[choixSymbole])
        return self.carteDepart

    def tour(self, joueur):
        print(joueur.nomJoueur, "joue, voilà les cartes que vous possedez:")
        for i in range(len(joueur.paquetDeCartes)):
            print("Carte n°" + str(i + 1) + ":", joueur.paquetDeCartes[i])
        choixCarte_tempo = int(input("Quel carte voulez vous utiliser ? "))
        while choixCarte_tempo > len(joueur.paquetDeCartes) or choixCarte_tempo <= 0:
            choixCarte_tempo = int(input("Le choix est invalide. Quel carte voulez vous utiliser ? "))
        choixEnCours = joueur.paquetDeCartes[choixCarte_tempo - 1]
        detecteur = False
        for i in range(len(choixEnCours)):
            if choixEnCours[i] in self.carteDepart:
                detecteur = True
        if detecteur == True:
            if choixCarte_tempo == 1:
                print("Vous avez posez votre", str(choixCarte_tempo) + "ère carte.")
            else:
                print("Vous avez posez votre", str(choixCarte_tempo) + "ème carte.")
            self.carteDepart = choixEnCours
            joueur.paquetDeCartes.pop(choixCarte_tempo - 1)
            print("La nouvelle carte est", self.carteDepart)
        else:
            print("Votre carte ne possède aucun symbole commun avec la carte déjà posé. Vous allez repiocher une carte.")
            choix = random.randint(0, 39)
            carte_temp = []
            for i in range(5):
                while self.symboles[choix] in carte_temp:
                    choix = random.randint(0, 39)
                carte_temp.append(self.symboles[choix])
            joueur.paquetDeCartes.append(carte_temp)
            print("La carte est toujours", self.carteDepart)
        return self.carteDepart

    def partie(self, p1, p2, p3, p4):
        print("Bienvenue sur le dobble ! Conseil avant de jouer: ouvrez la console à son maximum pour plus de confort.")
        print("La partie va débuter, voici la carte de départ:", game.carteDeDepart())

        self.vainqueurs = []
        while len(self.vainqueurs) != 4:
            if len(self.vainqueurs) == 3 and p1.nomJoueur not in self.vainqueurs:
                self.vainqueurs.append(p1.nomJoueur)
            elif p1.paquetDeCartes != []:
                game.tour(p1)
                if p1.nomJoueur not in self.vainqueurs and p1.paquetDeCartes == []:
                    self.vainqueurs.append(p1.nomJoueur)

            if len(self.vainqueurs) == 3 and p2.nomJoueur not in self.vainqueurs:
                self.vainqueurs.append(p2.nomJoueur)
            elif p2.paquetDeCartes != []:
                game.tour(p2)
                if p2.nomJoueur not in self.vainqueurs and p2.paquetDeCartes == []:
                    self.vainqueurs.append(p2.nomJoueur)

            if len(self.vainqueurs) == 3 and p3.nomJoueur not in self.vainqueurs:
                self.vainqueurs.append(p3.nomJoueur)
            elif p3.paquetDeCartes != []:
                game.tour(p3)
                if p3.nomJoueur not in self.vainqueurs and p3.paquetDeCartes == []:
                    self.vainqueurs.append(p3.nomJoueur)

            if len(self.vainqueurs) == 3 and p4.nomJoueur not in self.vainqueurs:
                self.vainqueurs.append(p4.nomJoueur)
            elif p4.paquetDeCartes != []:
                game.tour(p4)
                if p4.nomJoueur not in self.vainqueurs and p4.paquetDeCartes == []:
                    self.vainqueurs.append(p4.nomJoueur)
        return self.vainqueurs


joueur1 = cartes("Schadrac")
joueur2 = cartes("Rayan")
joueur3 = cartes("Mario")
joueur4 = cartes("Funky Kong")

game = dobble(joueur1, joueur2, joueur3, joueur4)
game.partie(joueur1, joueur2, joueur3, joueur4)

print("La partie est terminée ! Le vainqueur est", '\033[94m' + game.vainqueurs[0] + '\033[0m,', "le 2ème est", '\033[92m' + game.vainqueurs[1] + '\033[0m,', "le 3ème est", '\033[93m' + game.vainqueurs[2] + '\033[0m', "et le dernier est", '\033[91m' + game.vainqueurs[3] + '\033[0m.')