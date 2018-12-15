from urllib.request import urlopen, Request, URLError, HTTPError
import sys
import time
print('''\033[36;1m
  ____             _      _____ _           _
 |  _ \  __ _ _ __| | __ |  ___(_)_ __   __| | ___ _ __
 | | | |/ _` | '__| |/ / | |_  | | '_ \ / _` |/ _ \ '__|
 | |_| | (_| | |  |   <  |  _| | | | | | (_| |  __/ |
 |____/ \__,_|_|  |_|\_\ |_|   |_|_| |_|\__,_|\___|_|
''')
def hp(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(10./100)
hp("\033[32;1m[!]Thanks for using Dark Finder[!]")
hp("[+]ex:https://darkerror.net or http://darkerror.net")
hp("[+]Greetz All Muslims Hacker")
hp("[+]Special Thanks to 703 bro ^_^")
hp("[>]Facebook:www.facebook.com/uiddarkhtml")
hp("[>]youtube:youtube.com/DarkError\033[0m")
header = {'user-agent': 'Moofzilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
file = open('link.txt', 'r').read().split('\n')
site = input('\033[36;1mEnter a site: ')
print('\033[38mAvailable links>>>\033[0m')
for list in file:
    url = site + '/' +list
    try:
        req = Request(url, None, header)
        res = urlopen(req)
    except(ValueError, HTTPError, URLError):
        print('\033[31;1mNot Found: ' + url + '\033[0m')
    else:
        print('\033[32;1mFound: ' + url + '\033[0m')
