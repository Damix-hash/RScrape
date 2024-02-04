import os, os.path
from os import system
import colorama
from colorama import Fore, init

init()

system("title " + "RSCRAPE - Made by Damix :3c")
seperator = "---------------------------------------------------------------"
banner = (
    Fore.MAGENTA
    + """
██████╗ ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝███████╗██║     ██████╔╝███████║██████╔╝█████╗  
██╔══██╗╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
██║  ██║███████║╚██████╗██║  ██║██║  ██║██║     ███████╗
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝ Made by Damix :3c
"""
)
print(banner)
print(seperator)

def clr():
    os.system('cls' if os.name=='nt' else 'clear')


print("Input File: ")
filename = input("> ")
clr()
print(banner)
print(seperator)
print("Want to log what account are getting scraped? Y/N")
anwser = input("> ")

folder = "Exported"

def incremenate():
    global i
    i = 0
    while os.path.exists(f"{folder}/scraped_{i}.txt"):
        i += 1

new = incremenate()

if not os.path.exists(folder):
    os.mkdir(folder)
if not os.path.exists(f"{folder}/scraped_{i}.txt"):
    open(f"{folder}/scraped_{i}.txt", "w").close()

def setup():
    clr()
    print(banner)
    print(seperator)
    print("Scraping...")
    print(seperator)
    def scrape():
        with open(f"{folder}/scraped_{i}.txt", "w", encoding="utf-8") as export:
            global count
            count = 0
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    for line in file:
                        if "roblox" in line and line.startswith("https://") or line.startswith("www."):
                            try:
                                splitted = line.split(":")
                                username = splitted[2]
                                password = splitted[3]
                                if not username == "" and not password == "":
                                    export.write("{}:{}".format(username, password))
                                count += 1
                                if anwser == "Y" or anwser == "y":
                                        if not username == "" and not password == "":
                                            print("{}:{}".format(username, password), end="")
                            except Exception as e:
                                print(str(e))
                                continue

    scrape()


if __name__ == "__main__":
    setup()
    print(seperator)
    print(f"Scraped {count} accounts to scraped_{i}.txt")
    input("Press ENTER to leave.")
    exit
