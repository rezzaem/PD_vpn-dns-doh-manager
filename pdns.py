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
█▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ░ ░ ▀▀▀░ ▀░░▀ ▀▀▀ ░ ░ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀ by rezaa.em"""+txt_color.WHITE)

            print('----------------------------------------\n')
            if 'DNS request timed out.' in output:
                print(output+txt_color.YELLOW+'recommand to check network and change dns'+txt_color.WHITE)
            else:
                print(output)
            print('----------------------------------------\n')
            print("1. Electro -> (electrotm.org)\n2. Shecan -> (shecan.ir)\n3. Begzar -> (begzar.ir)\n4. Cloudflare\n5. Google\n6. Reset to default\n7. Exit")
            print('\n----------------------------------------\n')
            
            choice=input("Enter your choice [1-7] : ")
            
            if choice not in ['1','2','3','4','5','6','7']:
                continue
            else :choice = int(choice)
            print(txt_color.YELLOW+'changing dns ...'+txt_color.WHITE)
            if choice == 7:
                system('cls')
                print('This program has no affiliation and connection with DNS provider services and only uses their IP for personal use.')
                print("tnx for use\nExiting...")
                sleep(3)
                break
            elif choice == 1:
                system('python op1.py')
                provider="Electro"
            elif choice == 2:
                system('python op2.py')
                provider="Shecan"
            elif choice==3:
                system('python op3.py')
                provider='Begzar'
            elif choice == 4:
                system('python op4.py')
                provider="Cloudflare"
            elif choice == 5:
                system('python op5.py')
                provider="Google"
            elif choice == 6:
                system('python op6.py')
                provider="default"
            print(txt_color.GREEN+f"The DNS has been changed to {provider} successfully."+txt_color.WHITE)
            sleep(3)

        

    except KeyError:
        print(KeyError+'\n'+txt_color.RED+'for reslove problem contact with me : @R3288')
if __name__=='__main__':
    R3288()