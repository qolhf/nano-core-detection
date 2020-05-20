import os, sys, requests, socket, json, urllib.request
from colorama import Fore, Style
from time import sleep

print(Fore.BLUE + "Nanocore DDNS Detector!")
print(Fore.GREEN + "Made by qolhf! (https://github.com/qolhf/nanocoredetector)")

if len(sys.argv) == 1:
    ip = input("Enter The DDNS Or The IP: ")
    if '.ddns' in ip:
        print(Fore.GREEN + "[INFO] DDNS Detected!")
        print(Fore.GREEN + "[INFO] Running DNS Lookup!")
        with urllib.request.urlopen("https://json.geoiplookup.io/{}".format(ip)) as url:
            js = json.loads(url.read().decode())
            ipp = js['ip']
            country = js['country_name']
        print(Fore.GREEN + "[INFO] {} Resolves to: {} and is located in {}".format(ip, ipp, country))
        print(Fore.GREEN + "[INFO] Running final test on {}".format(ip))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultsock123 = sock.connect_ex((ip,123))
        if resultsock123 == 0:
            port123 = "OPEN"
        else:
            port123 = "CLOSED"
        resultsock1604 = sock.connect_ex((ip, 1604))
        if resultsock1604 == 0:
            port1604 = "OPEN"
        else:
            port1604 = "CLOSED"
        resultsock1605 = sock.connect_ex((ip, 1605))
        if resultsock1605 == 0:
            port1605 = "OPEN"
        else:
            port1605 = "CLOSED"

        if port1604 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 1604 Is Open.".format(ip))
        if port123 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 123 Is Open. (COULD BE HARMLESS)".format(ip))
        if port1605 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 123 Is Open. (COULD BE HARMLESS)".format(ip))
        else:
            print(Fore.RED + "[WARNING] {} got a NEGATIVE hit for Nanocore C&C/C2! Reason: Port 1604 and 123 Is Closed!.".format(ip))
        
    else:
        print(Fore.GREEN + "[INFO] IP Address Detected!")
        print(Fore.GREEN + "[INFO] Running DNS Lookup!")
        with urllib.request.urlopen("https://json.geoiplookup.io/{}".format(ip)) as url:
            js = json.loads(url.read().decode())
            ippp = js['ip']
            country = js['country_name']
        print(Fore.GREEN + "[INFO] {} Resolves to: {} and is located in {}".format(ip, ippp, country))
        print(Fore.GREEN + "[INFO] Running final test on {}".format(ip))
        print(Fore.GREEN + "[INFO] If this stage takes over 30 seconds, feel free to kill it (means the host is not a nanocore cnc)")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        resultsock123 = sock.connect_ex((ip,123))
        if resultsock123 == 0:
            port123 = "OPEN"
        else:
            port123 = "CLOSED"
        resultsock1604 = sock.connect_ex((ip, 1604))
        if resultsock1604 == 0:
            port1604 = "OPEN"
        else:
            port1604 = "CLOSED"
        resultsock1605 = sock.connect_ex((ip, 1605))
        if resultsock1605 == 0:
            port1605 = "OPEN"
        else:
            port1605 = "CLOSED"


        if port1604 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 1604 Is Open.".format(ip))
        elif port123 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 123 Is Open. (COULD BE HARMLESS)".format(ip))
        elif port1605 == "OPEN":
            print(Fore.RED + "[WARNING] {} got a POSITIVE hit for Nanocore C&C/C2! Reason: Port 1605 Is Open.".format(ip))
        elif port1605 == "CLOSED" and port1604 == "CLOSED" and port123 == "CLOSED":
            print(Fore.RED + "[WARNING] {} got a NEGATIVE hit for Nanocore C&C/C2! Reason: Ports 1604, 123 and 1605 are Closed!.".format(ip))
else:
    print("This is not a CLI application! Please run it normally and you will be prompted by input for the host!")