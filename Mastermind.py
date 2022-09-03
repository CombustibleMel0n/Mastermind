import random

def main_loop():
    combi =[]
    for i in range(5):
        combi.append(random.randrange(1,9)) #Random Number
    nbre_essais = 12
    while nbre_essais > 0:
        essai = input("Enter a series of 5 numbers from 1 to 8 : ")
        number_spot = 0
        just_number = 0
        try:
            essai = int(essai)
            if essai >= 11111 and essai <= 88888 :
                combi_joueur = [int(x) for x in str(essai)]
                if combi_joueur == combi :
                    print("Well done ! You found the solution !")
                    if input('If you want to play again, type \'YES\', otherwise type anything else') == 'YES' :
                        main_loop()
                    else :
                        return

                else :
                    done = combi[:]
                    for i in range(5):
                        for j in range(5):
                            if i==j and combi_joueur[i] == done[j]:
                                number_spot +=1
                                done[j] = 0
                                break
                    for i in range(5):
                        for j in range(5):
                            if i != j and combi_joueur[i] == done[j]:
                                just_number += 1
                                done[j] = 0
                                break
                    nbre_essais -= 1
                    print(f"You have {number_spot} numbers in the right spot")
                    print(f"You have {just_number} numbers in the wrong spot")
                    print(f"You have {nbre_essais} tries remaining !")
            else :
                print ("Please enter a series of exactly 5 numbers between 1 and 8 :")
        except ValueError:
            print ("Please enter a series of 5 numbers between 1 and 8 : ")
    print(f"Nice try, the combination was {combi} !")
    if input('If you want to play again, type \'YES\', otherwise type anything else') == 'YES' :
        main_loop()
    else :
        return
main_loop()


