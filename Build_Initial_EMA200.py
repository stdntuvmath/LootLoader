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
import Calculate_Angle_of_EMA200
import Calculate_Standard_Dev
import Calculate_EMA200AngleMean


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


def Get_HistoricalData_InsertInto_DB():

    client = easy_client(
        api_key=config_TDA_Live.api_key,
        redirect_uri=config_TDA_Live.redirect_url,
        token_path=config_TDA_Live.token_path)


    allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()
    counter_ofSymbols=0
    

    previousEma200Value = 0
    newEma200Value=0

    previousEMA200AngleValue = 0
    newEMA200AngleValue = 0

    ema200AngleArray = []

    standardDev=0

    EMA200Array = []


    for symbol in allSymbols:
        if(counter_ofSymbols < 50):
            try:
                result = client.get_price_history(symbol,
                                                
                                                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,# a candle is formed every minute
                                                need_extended_hours_data=True,
                                                start_datetime=datetime.datetime.now()-timedelta(days=3),
                                                end_datetime=datetime.datetime.now())

            except HTTPError:
                print('HTTPError: Candle data could not be pulled from TDAs server.')


            except TypeError:
                print('TypeError: Candle data could not be pulled from TDAs server.')

    
            #convert to json
            pricedata = result.json()
            counter_ofDataPoints=0
            counter_ofAnglePoints=0

            #print(pricedata)



            # #parse json data
            for candle in pricedata['candles']:                
                closePrice = candle.get("close","")
                if counter_ofDataPoints >= 1000:
                    #print(symbol, newEma200Value)
                    file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                    if(file_exists == True):

                        outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                        outFile.write("{}".format(closePriceString))
                        outFile.close()            

                    else:
                        outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                        outFile.write("{}".format(closePriceString))
                        outFile.close()


            
                newEma200Value = Calculate_EMA200.Get_NewestEMA200_Method(previousEma200Value,closePrice)


      
                newEMA200AngleValue = Calculate_Angle_of_EMA200.CalculateAngle(newEma200Value, previousEma200Value)



                ema200AngleArray.append(newEMA200AngleValue)

                if(len(ema200AngleArray) > 120):
                    ema200AngleArray.remove(ema200AngleArray[0])
                    standardDev = Calculate_Standard_Dev.Return_Standard_Dev_of_Angle_of_EMA200(ema200AngleArray)

                standardDev2 = standardDev*2
                standardDev3 = standardDev*3
                standardDev4 = standardDev*4
                standardDev5 = standardDev*5
                standardDev6 = standardDev*6
                standardDev7 = standardDev*7
                standardDev8 = standardDev*8
                standardDev9 = standardDev*9
                standardDev10 = standardDev*10


                counter_ofAnglePoints+=1

                epochTime = candle.get("datetime","")

                tz = pytz.timezone('US/Central')

                stringLocalTime = str(datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%Y%m%d %H:%M:%S'))#from utc to local time

                stringLocalTimeArray = []

                stringLocalTimeArray = stringLocalTime.split(" ")

                localDate = stringLocalTimeArray[0]
                localTime = stringLocalTimeArray[1]

                #put into lootloader server

                #Insert_Into_Symbol_Tables.Insert_Symbol_Price_andDateTime_Data(symbol, closePrice, localDate, localTime)
                #Insert_Into_Symbol_Tables.Insert_Symbol_EMA200_andDateTime_Data(symbol, newEma1000Value, localDate, localTime)

                previousEma200Value = newEma200Value
                previousEMA200AngleValue = newEMA200AngleValue

                #suggestions from David Sedivy at the math center
                #except TYPE:

                #use continue inside your except statement, after the print statement


                # #print to terminal
            
                closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(counter_ofDataPoints, symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev10, standardDev9, standardDev8, standardDev7, standardDev6, standardDev5, standardDev4, standardDev3, standardDev2, standardDev, localDate, localTime)

                #closePriceString = "{}, {}, price: {}, EMA200: {}, AngleEMA200: {}, StandardDev: {}, {}, {}\n".format(counter_ofDataPoints, symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, localDate, localTime)
                #print(closePriceString)


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



                #gets more symbols from the whole - unknown why
                # if counter == 100:
                #     sleep(0.5)
                #     counter=0
                # counter = counter+1
                # print(counter)
                # print(result)
                counter_ofDataPoints+=1



        counter_ofSymbols+=1


        previousEma200Value = 0
        previousEMA200AngleValue = 0
        EMA200Array.clear()
                #put into a file



                #sleep(0.000001)




