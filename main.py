import os
import platform
from colorama import Fore

pm = platform.system()
if pm == "Windows":
    os.system("cls")
elif pm == "Linux" or pm == "Darwin":
    os.system("clear")

banner = Fore.RED + """
                         _____ _         ______ _           _           
                        |_   _| |        |  ___(_)         | |          
                          | | | |__   ___| |_   _ _ __   __| | ___ _ __ 
                          | | | '_ \ / _ \  _| | | '_ \ / _` |/ _ \ '__|
                          | | | | | |  __/ |   | | | | | (_| |  __/ |   
                          \_/ |_| |_|\___\_|   |_|_| |_|\__,_|\___|_|   

                               Github : https://github.com/TanevAZ
"""

print(banner)

def main():
    # Ask the user for the directory to search
    directory = input(f'\n{Fore.RESET}Enter the directory to search : ')
    # Ask the user for the folder name to search for
    folder = input(f'Enter the folder name : {Fore.LIGHTGREEN_EX}')
    # Search for the folder in the directory and all subdirectories
    pathFound = []
    for root, dirs, files in os.walk(directory):
        for name in dirs:
            if name == folder:
                print(f'{Fore.RESET}Folder {Fore.LIGHTGREEN_EX}found{Fore.RESET} in : {root}\\{name}')
                pathFound.append(os.path.join(root, name))
                

    if pathFound:
        with open("results.txt", "w") as file:
            for path in pathFound:
                file.write(path + "\n")
        resultFile = os.path.join(os.getcwd(), "results.txt")
        print(f"\n{Fore.RESET}File results.txt saved in: {Fore.LIGHTYELLOW_EX}{resultFile}")
    else:
        print(f'{Fore.RESET}Folder not {Fore.LIGHTRED_EX}found{Fore.RESET}')

    input(f"\n{Fore.LIGHTGREEN_EX}Scan terminated. \n{Fore.WHITE}Press Enter to exit...")
    exit()

main()
