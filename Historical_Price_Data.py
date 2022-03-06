import requests
import tda
from Documentation.config_TDA_Live import api_key
from datetime import datetime




#define endpoint

endPoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format('AMD')



#define current time and pull parameters

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")


payLoad = {'apiKey':'DJWLOEI8U7VIYEGU7KD5HWRDVCKI3L6R',
           'periodType':'day',
           'frequencyType':'minute',
           'frequency':'1',
           'period':'2',
           'endDate':'1556158524000',
           'startDate':'1554535854000',
           'needExtendedHoursData':'true'}

   

content = requests.get(url=endPoint, params=payLoad)
    



#convert it to dictionary
data = content.json()
print(data)