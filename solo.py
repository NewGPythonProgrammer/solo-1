from colorama import *
import os
from time import *
import optparse
import random
import sys
import core.pscan as pscan
import core.oscan as oscan

def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "█" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

def load():
    for i in range(101):
        progress(i)
        sleep(0.01)

def start(us,ps,os):
    if(ps == "true"):
        pscan.portscan(us)
    if(os == "true"):
        oscan.oscan(us)
        
if __name__ == "__main__":
    parser = optparse.OptionParser(Fore.BLUE+f"""
{Fore.BLUE} _______  _______  ___      _______ 
{Fore.BLUE}|       ||       ||   |    |       |
{Fore.BLUE}|  _____||   _   ||   |    |   _   |
{Fore.RED}| |_____ |  | |  ||   |    |  | |  |
{Fore.RED}|_____  ||  |_|  ||   |___ |  |_|  |
{Fore.GREEN} ____|  ||       ||       ||       |
{Fore.GREEN}|_______||_______||_______||_______|

                        {Fore.RED} Coded By @thesaderror 
                        {Fore.GREEN} Github: TheSadError

{Fore.BLUE}Usage : python3 solo.py --p true --u example.com

    """)
    parser.add_option("--p",dest = "port",type="string",help = "Port scanning parameter")
    parser.add_option("--u",dest = "url",type="string",help = "Target URL , Username Usage : --u TheSadError , --u thesaderror.com")
    parser.add_option("--o",dest = "osint",type="string",help = "Osint Option Usage : --o true")
    (options,args) = parser.parse_args()
    port = options.port
    url = options.url
    osint = options.osint
    if(url == None):
        print(parser.usage)
        exit(0)

    start(url,port,osint)
