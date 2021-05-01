#coded by N17RO
#code fixed and modifed by X.pL01T3R (Sabbir Rahman)
#Youtube : https://youtube.com/channel/UCQxsdKKHhf1zYpGdqsOKonQ
#Facebook : https://www.facebook.com/sab.bir936
#Instagram : https://instagram.com/catch._me_if_you_can?igshid=w1j6mscmruwg
#Github : https://github.com/XPL01T3R/

#modules
import argparse
import requests, json
import sys
from sys import argv
import os



parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'


#banner
print (green+"""

###########################################################
                           ___                            
 .-.                      (   )                           
( __)    .-..     .--.     | | .-.     .--.    ___ .-.    
(''")   /    \   /    \    | |/   \   /    \  (   )   \   
 | |   ' .-,  ; |  .-. ;   |  .-. .  |  .-. ;  | ' .-. ;  
 | |   | |  . | |  |(___)  | |  | |  | |  | |  |  / (___) 
 | |   | |  | | |  |       | |  | |  | |  | |  | |        
 | |   | |  | | |  | ___   | |  | |  | |  | |  | |        
 | |   | |  ' | |  '(   )  | |  | |  | '  | |  | |        
 | |   | `-'  ' '  `-' |   | |  | |  '  `-' /  | |        
(___)  | \__.'   `.__,'   (___)(___)  `.__.'  (___)       
       | |                                                
      (___)                                               

###########################################################

""")
print (yellow+bold+"                 <<IP Address Tracker>> \n"+clear)
print (cyan+bold+"                        v1.0 \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = red+bold+"[∆]"
        b = green+bold+"[∆]"
        print (a, "[Victim]:", data['query'])
        print(cyan+"###############"+cyan)
        print (b, "[ISP]:", data['isp'])
        print(cyan+"###############"+cyan)
        print (a, "[Organisation]:", data['org'])
        print(cyan+"###############"+cyan)
        print (b, "[City]:", data['city'])
        print(cyan+"###############"+cyan)
        print (a, "[Region]:", data['region'])
        print(cyan+"###############"+cyan)
        print (b, "[Longitude]:", data['lon'])
        print(cyan+"###############"+cyan)
        print (a, "[Latitude]:", data['lat'])
        print(cyan+"###############"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(cyan+"###############"+cyan)
        print (a, "[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Quiting, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[×]"+" Turn on your wifi/data!"+clear)
sys.exit(1)