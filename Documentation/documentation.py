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

    startTime = "08:29:55"
    endTime = "14:59:00"
    now = int(time.time())
    today = tday.Get_Todays_Weekday_Name()

    tz = pytz.timezone('US/Central')

    localTime = datetime.datetime.utcfromtimestamp(now).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M:%S')#from utc to local time



    while startTime <= now & now < endTime & today !="Saturday" & today != "Sunday":



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








#NOTES for Client.get_price_history

# Client.get_price_history(symbol, *, period_type=None, period=None, frequency_type=None, frequency=None, start_datetime=None, end_datetime=None, need_extended_hours_data=None)
# Get price history for a symbol. Official documentation.

# Parameters
# period_type – The type of period to show.

# period – The number of periods to show. Should not be provided if start_datetime and end_datetime.

# frequency_type – The type of frequency with which a new candle is formed.

# frequency – The number of the frequencyType to be included in each candle.

# start_datetime – Start date.

# end_datetime – End date. Default is previous trading day.

# need_extended_hours_data – If true, return extended hours data. Default is true.

# classtda.client.Client.PriceHistory
# classFrequency(value)
# An enumeration.

# EVERY_MINUTE= 1
# EVERY_FIVE_MINUTES= 5
# EVERY_TEN_MINUTES= 10
# EVERY_FIFTEEN_MINUTES= 15
# EVERY_THIRTY_MINUTES= 30
# DAILY= 1
# WEEKLY= 1
# MONTHLY= 1
# classFrequencyType(value)
# An enumeration.

# MINUTE= 'minute'
# DAILY= 'daily'
# WEEKLY= 'weekly'
# MONTHLY= 'monthly'
# classPeriod(value)
# An enumeration.

# ONE_DAY= 1
# TWO_DAYS= 2
# THREE_DAYS= 3
# FOUR_DAYS= 4
# FIVE_DAYS= 5
# TEN_DAYS= 10
# ONE_MONTH= 1
# TWO_MONTHS= 2
# THREE_MONTHS= 3
# SIX_MONTHS= 6
# ONE_YEAR= 1
# TWO_YEARS= 2
# THREE_YEARS= 3
# FIVE_YEARS= 5
# TEN_YEARS= 10
# FIFTEEN_YEARS= 15
# TWENTY_YEARS= 20
# YEAR_TO_DATE= 1
# classPeriodType(value)
# An enumeration.

# DAY= 'day'
# MONTH= 'month'
# YEAR= 'year'
# YEAR_TO_DATE= 'ytd'





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



#createTables.CreateTables()
#createTablesEMA200.CreateTables()
#Delete_Table_Data.ClearTables()
#deleteTables.DeleteTables()

#Get_Historical_PriceData.Get_Price_Date_InsertInto_DB()

Build_Initial_EMA200.Get_HistoricalData_InsertInto_DB()

#asyncio.run(RetrieveLiveData.MarketDataService.retrieveLiveData(Self))


#array = {"AMD","BASE"}

#RetrievePolygonMarketHistory.retrievePolygonMarketHistory(array)



#pull all symbols above the EMA200

#stream price data for each symbol

#check current price position relative to price[3], price[6], price[9] for each symbol

#get ema200 value for each symbol

#calculate ema200 angle for each symbol

#check ema200 angle relative to turner bands for each symbol



#c = OAuth_Authenticate.Authenticate()#Call Authenticate method

#----------------------------------------------------------------------------------------------------------asyncio.run(Stream_Price_.read_stream())

#asyncio.get_running_loop(Stream_Price_.read_stream()).stop(Stream_Price_.read_stream())

#Pull_Symbols_FromTOScsv.Pull_Symbols()#returns a dict object

#symbolList = "AMD,BASE"

#asyncio.run(Stream_Price_FromSymbol.read_stream())


# try asyncio.gather()

# MalachiConstant — Today at 4:41 PM
# @stdntuvmath I think your methodology is flawed, your streams will run forever until you stop them (or tda closes them).  You need one stream reader and have it handle everything.  If you need to have multiple tasks running look into asyncio.gather()

#Get_Symbol_ClosePrice_Timestamp.Get_ClosePrice_Timestamp("AMD")




#parse the nested json data into a pandas dataFrame
# pandasDF = pd.json_normalize(dictionary, record_path=['candles'])
# pandasDF.info()

#print(dictionary["candles"][5]["close"])

#gets the close prices from all the candles from the dictionary json object via python
# for key, values in dictionary.items():
#     for i in range(len(dictionary["data"]["table"]["rows"])):

#         #candleEpochTime = dictionary["candles"][i]["datetime"]

#         #candleEpochTime = int(dictionary["candles"][i]["datetime"])
#         #candleEpochTimeFloat = float(candleEpochTime)
#         #currentLocalTimeFromCurrentEpochTime = time.ctime(candleEpochTimeFloat)
#         #currentLocalTimeFromCurrentEpochTime = datetime.datetime.fromtimestamp(candleEpochTime).strftime('%Y-%m-%d %H:%M:%S')
        
#         print("{}".format(dictionary["data"]["table"]["rows"][i]["symbol"]))
# print(len(dictionary["data"]["table"]["rows"]))
# if(dictionary["empty"]==True):
#     os.remove("PriceData\\{}_priceData.json".format(symbol))
#     print("\n\nSymbol: {} returned no price data for evaluation.\n\n".format(symbol))




# with open("priceData.json", "r") as file:
#     data=file.read()



# dictionary = json.loads(data)

# print(type(str))