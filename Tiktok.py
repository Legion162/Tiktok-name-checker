# imports
import requests

from itertools import chain, combinations

import colorama

colorama.init(autoreset=True)

from colorama import Fore, Back, Style

colorama.init()

import pyfiglet

# Ressources and variables

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

chaine = str()

# Code itself

out = pyfiglet.figlet_format("Tiktok Checker", font="slant")
print(out)
caracters = input("Enter 'start' to start the machine ")

caracter = int()

start = "start"

if caracters == start:
    def all_subsets(ss):
        return chain(*map(lambda x: combinations(ss, x), range(4, 8)))


    for subset in all_subsets(list):

        g = (''.join(subset))

        url = "https://www.tiktok.com/@" + g + "?lang=en"

        req = (requests.get(url).text)

        if str('content="Couldn&#x27;t find this account') in req:
            print(Back.GREEN + str(url))
        else:
            print(Back.RED + str(url))
else:
    print("Machine did not get the order to start ")



























