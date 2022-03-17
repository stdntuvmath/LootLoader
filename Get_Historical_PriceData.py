from time import sleep
from urllib.error import HTTPError
from tda.client import Client
from tda.auth import easy_client
from datetime import datetime, timedelta
import Documentation.config_TDA_Live as config_TDA_Live
import pytz
import All_Symbols
from os.path import exists
import time
import datetime
import Insert_Into_Symbol_Tables
import Todays_Weekday as tday
import Calculate_EMA200


def Get_Price_Date_InsertInto_DB():

    client = easy_client(
        api_key=config_TDA_Live.api_key,
        redirect_uri=config_TDA_Live.redirect_url,
        token_path=config_TDA_Live.token_path)


    allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()
    counter1=0
    

    previousEma200Value = 131.9
    timeDataArray = []
    


    for symbol in allSymbols:
        if(counter1 < 50):
            try:
                result = client.get_price_history(symbol,
                                                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                                                need_extended_hours_data=False,
                                                start_datetime=datetime.datetime.now(),
                                                end_datetime=datetime.datetime.now())

            except HTTPError:
                print('HTTPError: Candle data could not be pulled from TDAs server.')


            except TypeError:
                print('TypeError: Candle data could not be pulled from TDAs server.')

    
            #convert to json
            pricedata = result.json()
            counter=0

            #print(pricedata)



            # #parse json data
            for candle in pricedata['candles']:
                
                closePrice = candle.get("close","")
                # if(counter1 == 0):
                #     previousEma200Value = closePrice
                newEma200Value = Calculate_EMA200.Get_NewestEMA200_Method(previousEma200Value,closePrice)
                #print(newEma200Value)
                epochTime = candle.get("datetime","")

                tz = pytz.timezone('US/Central')

                stringLocalTime = str(datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%Y%m%d %H:%M:%S'))#from utc to local time

                stringLocalTimeArray = []

                stringLocalTimeArray = stringLocalTime.split(" ")

                localDate = stringLocalTimeArray[0]
                localTime = stringLocalTimeArray[1]

                #put into lootloader server

                Insert_Into_Symbol_Tables.Insert_Symbol_Price_andDateTime_Data(symbol, closePrice, localDate, localTime)
                Insert_Into_Symbol_Tables.Insert_Symbol_EMA200_andDateTime_Data(symbol, newEma200Value, localDate, localTime)

                previousEma200Value = newEma200Value
                #suggestions from David Sedivy at the math center
                #except TYPE:

                #use continue inside your except statement, after the print statement


                # #print to terminal
            
                # closePriceString = "{}, {}, {}, {}\n".format(symbol, closePrice, localDate, localTime)
                # print(closePriceString)



                #gets more symbols from the whole - unknown why
                # if counter == 100:
                #     sleep(0.5)
                #     counter=0
                # counter = counter+1
                # print(counter)
                # print(result)



        counter1+=1

                #put into a file

        #print(counter1)

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