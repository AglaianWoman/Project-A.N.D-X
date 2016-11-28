import os
import sys
import imp 
import tqdm
import pytz
import time
import astral
import random
import filedir
import datetime
import platform
import optparse
import errorhandler
from optparse import OptionParser
from tqdm import *
from time import sleep
from sys import platform as osid
from datetime import datetime, time
from astral import Astral
from errorhandler import errorhandler
from filedir import filecheck

## ChatBot - [ Als: Nemesis 2 ]  -  Version: 1.0.0  -  Xver: 1.0 ##\

## A helping bot for the tool/project A.N.D-X ##

if osid == 'win32':
    print "I'm sorry, I don't run on windows, just like the tool..."
    print("")
    os.system("pause")
    sys.exit(1)

## Check to see if the user is in root ##
if os.geteuid() == 1:
    print "\033[31m[-]\033[0m This program must be run as root. Try [sudo] bot.py or type 'sudo su' then re-run the application."
    sys.exit(1)

os.system("clear")
print "Loading, please wait...\n"
for x in tqdm(range(100)):
    sleep(0.05)
print "\nDone"
sleep(2)
os.system("clear")

__version__ = '1.0.0'

xver = 1.0

if __version__ < 1.0 and xver != __version__:
    print "[*] Running older build: ", xver, " build: ", __version__, "\n"
    pass

## Random classes, just because... ##
class textstyle:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class error:
    cmd_not_found = "I couldn't find the command or phrase..."
    e_not_found = "I couldn't understand the statement or phrase."

class cities:
    city_a = 'Chicago'
    city_b = 'Middletown'
    city_c = 'Cincinatti'
    city_d = 'Talwanda'
    # Add your city here
    # Just do:
    #  <city_[a-z or 1-Whatever] = <'' + City>
    #  Then look for the variable city = a[cities.city_b] and replace the .city_b with your city

## Variables ##
author = 'S1lent'
xgs = "\033[32m"
xge = "\033[30m"
plus = "\033[32m[+]\033[30m"
minus = "\033[31m[-]\033[30m"
regular = "[*]"

def cmd_help():
    os.system("clear")
    print "=" * 4 + xgs + "[+]" + xge + " Bot Commands and common phrases and other options." + "=" * 21 + "\n"
    print regular + " Type 'show commands' or 'show all' to display content.\n"
    input_help = raw_input("bot[cmd - ($)]> ")
    # Print all avilable commands
    #
    # bot[cmd - ($)]> show commands
    #
    # [I] All commands for the bot...
    #
    # <[$cmd (sub_cmd [{$cmd_sub)alt}])]>
    # ...
    # Basically print all the commands for the bot (chatbot) 
    #
    if input_help == 'show commands' or input_help == 'show all':
        print("")
        print textstyle.UNDERLINE + xgs + textstyle.BOLD + "Command / Phrase" + textstyle.END + textstyle.END + xge + "\t\t\t" + textstyle.UNDERLINE + xgs + textstyle.BOLD + "Description" + textstyle.END + xge + textstyle.END + "\n"
        pass
    else:
        print error.cmd_not_found + "\n"
        pass  
    # The bots commands
    # Why use a class I thought, when I could simply define a function within a function and still get the same result 


## Options. DISCLAIMER: these options are still in testing phase, I would not recommend anyone to use these yet
def opts():
    parser = OptionParser(usage="[sudo] bot.py [OPTIONS] [ARGS]", conflict_handler="resolve")
    # Options

print xgs + "Bot Status: " + xge + " On"
print xgs + "Version: " + xge, xver
print xgs + "OS: " + xge + osid
print("")
print xgs + "-" * 4 + "[ " + xge + "What can I do for you?" + xgs + " ]" + "-" * 48 + xge + "\n"
print "[ Bot ]: Oh, and before I forget, if you get confused, which you may already be, type 'help' or 'help me' or 'please help me', etc at the prompt...\n"
## While loop start ##
while True:
    user_input = raw_input("bot $> ")
    if user_input == 'help' or user_input == 'help me' or user_input == 'please, help me' or user_input == 'please help me' or user_input == 'please help' or user_input == 'show help':
        cmd_help()
        pass
    elif user_input == 'exit' or user_input == 'see ya' or user_input == 'bye' or user_input == 'bye, thank you':
        # print "\nBye, have a nice day :) \n"
        #
        # Tell if it's day or night
        a = Astral()
        city = a[cities.city_a]
        now = datetime.now(pytz.utc)
        sun = city.sun(date=now, local=True)
        if now >= sun['dusk'] or now <= sun['dawn']:
            print "\nBye, have a good morning...or night :) \n"
        elif now >= sun['dawn'] or now <= sun['morning']:
            print "\nBye, have a good morning :) \n"
        elif now >= sun['dusk']:
            print "\nBye, have a good night :) \n"
        else:
            print "\nBye, unable to tell if dusk or dawn, maybe the set city is wrong...\n" 
        sleep(2)
        sys.exit()
    else:
        print("")
        print error.e_not_found + "\n"
        pass
