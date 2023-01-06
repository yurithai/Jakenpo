

"JAKENPÔ"

print("\n")
from random import randint
computerchoice = int(randint(1,3))

print("\033[35m=" * 17)
print("     \033[36mJakenpô\033[m")
print("\033[35m=\033[m" * 17)
print("\n")


def Final():

    print("\n")
    print("Você deseja continuar? \n1- SIM \n2- NÃO") 
    FinalChoice = int(input("Escolha: "))

    if FinalChoice == 1:
        
        while FinalChoice == 1:

            print("\n")
            ShowMenu()
            
    else:

        print("\033[35mFim do Jogo <3\033[m")
        

def ShowMenu():

    print('''   \033[36mMENU DE ESCOLHAS\033[m
    \033[36m1-\033[m PEDRA
    \033[36m2-\033[m PAPEL
    \033[36m3-\033[m TESOURA''')
    print("\n")

    personchoice = int(input("Qual você escolhe: "))
    print("\033[33mPROCESSANDO...\033[m")
    print("\n")
   
   
    if personchoice == 1 and computerchoice ==  2:
        print("O computador jogou {} e \033[32mGANHOU\033[m!" .format(computerchoice))

        if personchoice == 2 and computerchoice == 1:
            print("O computador jogou {} então você \033[32mGANHOU\033[m!" .format(computerchoice))


    elif personchoice == 1 and computerchoice == 3:
        print("O computador jogou {} então você \033[32mGANHOU\033[m!" .format(computerchoice))

        if personchoice == 3 and computerchoice == 1:
            print("O computador jogou {} e \033[32mGANHOU\033[m!" .format(computerchoice))

    elif personchoice == 2 and computerchoice == 3:
        print("O computador jogou {} e \033[32mGANHOU\033[m!" .format(computerchoice)) 

        if personchoice == 3 and computerchoice == 2:       
            print("O computador jogou {} então você \033[32mGANHOU\033[m!" .format(computerchoice))

    elif personchoice == 1 and computerchoice == 2:
        print("O computador jogou {} e \033[32mGANHOU\033[m!" .format(computerchoice)) 

        if personchoice == 2 and computerchoice == 1:
            print("O computador jogou {} então você \033[32mGANHOU\033[m!" .format(computerchoice))

    else:
        print("\033[34mDEU EMPATE!\033[m")
        print("O computador jogou {} então \033[32mEMPATOU\033[m!" .format(computerchoice))

    Final()

ShowMenu()     
