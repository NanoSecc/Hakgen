import os
import sys
import time
import colorama

os.system('clear')
def banner():
   print('\033[31m')
   print "                   UwU Thanks For Using Hakgen Made By NanoSecc team"
   time.sleep(2)
banner()

def alr():
   print('\033[32m')
   print "  ~~>  Genin Your Hack The Box Invite !"
   os.system('curl -XPOST https://www.hackthebox.eu/api/invite/generate -o hash.txt -s')
   print "  ~~>  Base 64 Hash Gen From HackTheBox"
alr()
print "  ~~>  uncoding base64 hash"
time.sleep(3)
os.system('bash dyc.sh')
print "  ~~>  Invite Code ^"
print('\033[31m')
print "    ------@@@----@@@----@@@----Say-Thanks-to-N..--@@@----@@@----@@@"
