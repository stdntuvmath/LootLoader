import datetime
import calendar
from os import read
import time
import pytz
import sys
        import time
        import pytz
        import random
        import requests
        
        from os import system
        from sys import stderr
        from time import sleep
        from datetime import datetime as dt
        from decimal import setcontext, BasicContext, Decimal
        
        from loguru import logger
        from tqdm import tqdm, trange
        
        from tda.utils import Utils
        from tda.auth import client_from_token_file
        from tda.orders.common import Session, Duration
        from .config import TOKEN_PATH, API_KEY_TDA, ACCOUNT_ID
        from tda.orders.equities import equity_buy_market, equity_sell_market



#how to be within market hours - this code works!

    # startTime = "08:29:55"
    # endTime = "14:59:00"
    # now = int(time.time())
    # today = tday.Get_Todays_Weekday_Name()

    # tz = pytz.timezone('US/Central')

    # localTime = datetime.datetime.utcfromtimestamp(now).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M:%S')#from utc to local time



    # while startTime <= now & now < endTime & today !="Saturday" & today != "Sunday":



print("hello dammit!")

api_key = 'DJWLOEI8U7VIYEGU7KD5HWRDVCKI3L6R'
client_id ='DJWLOEI8U7VIYEGU7KD5HWRDVCKI3L6R'

account_id = tda_client.get_account(int(ACCOUNT_ID)).json()


#testing and manipulating different timestamps into others
#currentEpochTime = time.time() - proven incorrect

# readable = datetime.datetime.utcfromtimestamp(currentEpochTime/1000).astimezone #/1000
# sdate = readable[:10]
# shour = int(readable[11:13]) - 5
# sminutes = int(readable[14:16])
# sseconds = float(readable[17:])


# currentLocalTime = "{} - {}:{}:{}".format(sdate,shour,sminutes,sseconds)

# print(currentLocalTime)






#   *****************this code works!*********************

#reference: https://gist.github.com/pssolanki111/ff49866b86c6d5ac418a50973e199f6f 

epoch_timestamp = 1638532800000 
tz = pytz.timezone('US/Central')

converted = datetime.datetime.utcfromtimestamp(epoch_timestamp / 1000).replace(tzinfo=pytz.utc).astimezone(tz)#from utc to local time

print(converted)

#   *****************this code works!*********************














# currentLocalMilitaryTime = datetime.now().time()
# currentLocalUTCTime = datetime.utcnow().time()
# currentLocalTime = time.localtime
currentEpochTime = time.time()
#currentLocalTimeFromCurrentEpochTime = datetime.datetime.fromtimestamp(currentEpochTime).strftime('%c')
# previous200MinutesEpochTime = currentEpochTime-12000

#currentLocalTimeFromCurrentEpochTime = time.ctime(1638579480000)

# currentCalendarDate = datetime.today().date()#YYYY-MM-DD
# currentDateAndMilitaryTime_Local_Calendar = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

currentYear = datetime.date.today().year
currentMonth = datetime.date.today().month
currentDay = datetime.date.today().day
today = datetime.datetime(currentYear, currentMonth, currentDay)

previousDay = datetime.datetime.now() - datetime.timedelta(1)
previousDayYear = previousDay.year
previousDayMonth = previousDay.month
previousDayDay = previousDay.day
yesterDay = datetime.datetime(previousDayYear, previousDayMonth, previousDayDay)

# print(f"\n\n\n{currentLocalMilitaryTime}\n{currentLocalUTCTime}\n{currentLocalTime}\n")
# print(f"{currentEpochTime}\n{previous200MinutesEpochTime}\n\n{currentDateAndMilitaryTime_Local_Calendar}")

# print("{}\n".format(today))
# print("{}\n".format(yesterDay))