import random

def main_loop():
    combi =[]
    for i in range(5):
        combi.append(random.randrange(1,9))
    nbre_essais = 12
    while nbre_essais > 0:
        essai = input("Rentrez une série de 5 nombres de 1 à 8 : ")
        try:
            essai = int(essai)
            if essai >= 11111 and essai <= 88888 :
                combi_joueur = [int(x) for x in str(essai)]
                if combi_joueur == combi :
                    print("Bravo ! Vous avez trouvé la combinaison !")
                    return
                else : 
                    for i in range(5):
                        if combi_joueur[i] == combi[i]:
                            print(True)
                        else :
                            print(False)
                    nbre_essais -= 1
                    print(f"Il vous reste {nbre_essais} essais !")
            else :
                print ("Merci de rentrez une série de 5 nombres compris entre 1 et 8: ")
        except ValueError:
            print ("Merci de rentrez une série de 5 nombres compris entre 1 et 8: ")
    print(f"Dommage, la combinaison était {combi} !")

main_loop()