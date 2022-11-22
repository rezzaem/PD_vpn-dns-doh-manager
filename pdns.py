# from os import system
from os import system
from time import sleep
from command_runner import command_runner

def R3288():

    try:
        while True:

            print ('getting dns info...')
            exit_code, output = command_runner('nslookup/', shell=True)
            char='\n'
            output=output[output.index(char)+2:]
            system('cls')
            print("""█▀▀█ █▀▀ █▀▀█ █▀▀ ░▀░ █▀▀█ █▀▀▄ ░ ░ █▀▀▄ █▀▀▄ █▀▀ ░ ░ █▀▀ █░░█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█
█░░█ █▀▀ █▄▄▀ ▀▀█ ▀█▀ █▄▄█ █░░█ ▀ ▀ █░░█ █░░█ ▀▀█ ▀ ▀ █░░ █▀▀█ █▄▄█ █░░█ █░▀█ █▀▀ █▄▄▀
█▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ░ ░ ▀▀▀░ ▀░░▀ ▀▀▀ ░ ░ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀""")
            
            print('----------------------------------------\n')
            print(output)
            print('----------------------------------------\n')
            print("1. electro -> (electrotm.org)\n2. shecan -> (shecan.ir)\n3. google\n4. cloudflare\n5. Reset to default\n6. Exit")
            print('\n----------------------------------------\n')
            
            choice=input("Enter your choice [1-6] : ")
            
            if choice not in ['1','2','3','4','5','6']:
                continue
            else :choice = int(choice)
            
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
            print(f"The DNS has been changed to {provider} successfully.")
            sleep(3)

        

    except KeyError:
        print(KeyError)

R3288()