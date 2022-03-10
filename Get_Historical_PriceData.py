from time import sleep
from tda.client import Client
from tda.auth import easy_client
from datetime import datetime, timedelta
import Documentation.config_TDA_Live as config_TDA_Live
import pytz
import All_Symbols
from os.path import exists
import time
import datetime
from Insert_Into_Symbol_Tables import Insert_Symbol_Price_andDateTime_Data
import Todays_Weekday as tday


def Get_Price_Date_InsertInto_DB():

    client = easy_client(
        api_key=config_TDA_Live.api_key,
        redirect_uri=config_TDA_Live.redirect_url,
        token_path=config_TDA_Live.token_path)


    allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()


    for symbol in allSymbols:


        result = client.get_price_history(symbol,
                                        frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                                        need_extended_hours_data=False,
                                        start_datetime=datetime.datetime.now(),
                                        end_datetime=datetime.datetime.now())


        pricedata = result.json()



        for candle in pricedata['candles']:
            
            closePrice = candle.pop("close")

            epochTime = candle.pop("datetime")

            tz = pytz.timezone('US/Central')

            stringLocalTime = str(datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%Y%m%d %H:%M:%S'))#from utc to local time

            stringLocalTimeArray = []

            stringLocalTimeArray = stringLocalTime.split(" ")

            localDate = stringLocalTimeArray[0]
            localTime = stringLocalTimeArray[1]

            #put into lootloader server

            Insert_Symbol_Price_andDateTime_Data(symbol, closePrice, localDate, localTime)

            # #print to terminal

           










            #put into a file

            # closePriceString = "{}, {}, {}\n".format(symbol, closePrice, localTime)
            # # print(closePriceString)

            # file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

            # if(file_exists == True):

            #     outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
            #     outFile.write("{}".format(closePriceString))
            #     outFile.close()            

            # else:
            #     outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
            #     outFile.write("{}".format(closePriceString))
            #     outFile.close()

            #sleep(0.000001)