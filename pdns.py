# from os import system
from os import system
from time import sleep
from command_runner import command_runner

class txt_color : 
   GREEN = "\033[92m"
   RED = "\033[91m"
   WHITE = "\033[0m"
   YELLOW="\033[33m"
   Cyan="\033[36m"

def R3288():

    try:
        while True:

            print ('getting dns info...')
            exit_code, output = command_runner('nslookup/', shell=True)
            char='\n'
            output=output[output.index(char)+2:]
            system('cls')
            print(txt_color.Cyan+"""█▀▀█ █▀▀ █▀▀█ █▀▀ ░▀░ █▀▀█ █▀▀▄ ░ ░ █▀▀▄ █▀▀▄ █▀▀ ░ ░ █▀▀ █░░█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█
█░░█ █▀▀ █▄▄▀ ▀▀█ ▀█▀ █▄▄█ █░░█ ▀ ▀ █░░█ █░░█ ▀▀█ ▀ ▀ █░░ █▀▀█ █▄▄█ █░░█ █░▀█ █▀▀ █▄▄▀
█▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ░ ░ ▀▀▀░ ▀░░▀ ▀▀▀ ░ ░ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀"""+txt_color.WHITE)
            
            print('----------------------------------------\n')
            if 'DNS request timed out.' in output:
                print(output+txt_color.YELLOW+'recommand to check network and change dns'+txt_color.WHITE)
            else:
                print(output)
            print('----------------------------------------\n')
            print("1. electro -> (electrotm.org)\n2. shecan -> (shecan.ir)\n3. google\n4. cloudflare\n5. Reset to default\n6. Exit")
            print('\n----------------------------------------\n')
            
            choice=input("Enter your choice [1-6] : ")
            
            if choice not in ['1','2','3','4','5','6']:
                continue
            else :choice = int(choice)
            print(txt_color.YELLOW+'changing dns ...'+txt_color.WHITE)
            if choice == 6:
                system('cls')
                print("tnx for use\nExiting...")
                sleep(1)
                break
            elif choice == 1:
                system('python op1.py')
                provider="electro"
            elif choice == 2:
                system('python op2.py')
                provider="shecan"
            elif choice == 3:
                system('python op3.py')
                provider="google"
            elif choice == 4:
                system('python op4.py')
                provider="cloudflare"
            elif choice == 5:
                system('python op5.py')
                provider="default"
            print(txt_color.GREEN+f"The DNS has been changed to {provider} successfully."+txt_color.WHITE)
            sleep(3)

        

    except KeyError:
        print(KeyError+'\n'+txt_color.RED+'for reslove problem contact with me : @R3288')

R3288()