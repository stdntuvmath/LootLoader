from ctypes.wintypes import BOOLEAN
from time import sleep
from urllib.error import HTTPError
from xmlrpc.client import Boolean
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
import Peak
import Trough
import Trade_Management


def Run_TurnerBands():

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


    okToBuy = True
    okToSell = False

    closePriceArray =[]

    buyPrice = 0
    sellPrice = 0

    peak = BOOLEAN
    trough = BOOLEAN


    accountValue = 30000

    while(accountValue >= 30000):
        for symbol in allSymbols:





            if(counter_ofSymbols < 100):
                try:
                    result = client.get_price_history(symbol,
                                                    
                                                    frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,# a candle is formed every minute
                                                    need_extended_hours_data=True,
                                                    start_datetime=datetime.datetime.now()-timedelta(weeks=2),
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

                    closePriceArray.append(closePrice)

                    if(len(closePriceArray) > 9):
                        closePriceArray.remove(closePriceArray[0])
                        #peak = Peak.Check_For_Peak(closePriceArray)
                        #trough = Trough.Check_For_Trough(closePriceArray)
                    #     print("Peak in: "+str(peak))
                    #     print("Trough in: "+str(trough))

                    # print("Peak out: "+str(peak))
                    # print("Trough out: "+str(trough))


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




                    #Buy
                    if((okToBuy == True 
                    and closePrice > newEma200Value 
                    and previousEMA200AngleValue < standardDev 
                    and newEMA200AngleValue > standardDev#and closePrice*shares < accountValue
                    ) or
                    (okToBuy == True 
                    and closePrice > newEma200Value 
                    and previousEMA200AngleValue < standardDev2 
                    and newEMA200AngleValue > standardDev2
                    )):


                        buyPrice = closePrice

                    #if((closePrice > newEma200Value and previousEMA200AngleValue < standardDev and newEMA200AngleValue > standardDev and closePriceArray[2] > closePrice and closePriceArray[5] > closePrice and closePriceArray[8] > closePrice and okToBuy == True) or (closePrice > newEma200Value and previousEMA200AngleValue < standardDev2 and newEMA200AngleValue > standardDev2  and closePriceArray[2] > closePrice and closePriceArray[5] > closePrice and closePriceArray[8] > closePrice and okToBuy == True) ):
                        #fake buy
                        closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format("BUY", symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)

                        file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                        if(file_exists == True):

                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}".format(closePriceString))
                            outFile.close()            

                        else:
                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}".format(closePriceString))
                            outFile.close()

                        #after the buy we need to subtract closePrice*shares from the current account balance
                        #accountValue = accountValue - closePrice*numberOfShares

                        okToBuy = False
                        okToSell = True





                    #Sell
                    if(previousEMA200AngleValue > standardDev10 and newEMA200AngleValue < standardDev10 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev9 and newEMA200AngleValue < standardDev9 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev8 and newEMA200AngleValue < standardDev8 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev7 and newEMA200AngleValue < standardDev7 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev6 and newEMA200AngleValue < standardDev6 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev5 and newEMA200AngleValue < standardDev5 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev4 and newEMA200AngleValue < standardDev4 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev3 and newEMA200AngleValue < standardDev3 and closePrice > buyPrice and okToSell == True or
                        previousEMA200AngleValue > standardDev2 and newEMA200AngleValue < standardDev2 and closePrice > buyPrice and okToSell == True ):
                        #fake sell
                        closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format("SELL", symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)

                        file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                        if(file_exists == True):

                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}".format(closePriceString))
                            outFile.close()            

                        else:
                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}".format(closePriceString))
                            outFile.close()


                        sellPrice = closePrice

                        newAccountValue = Trade_Management.Get_Profit(buyPrice, sellPrice, accountValue)

                        
                        print(accountValue)
                        
                        accountValue = newAccountValue


                        # file_exists = exists("PriceData\\Account.csv")    

                        # if(file_exists == True):

                        #     outFile = open("PriceData\\Account.csv", "a")
                        #     outFile.write("{}".format(newAccountValue))
                        #     outFile.close()            

                        # else:
                        #     outFile = open("PriceData\\Account.csv", "a")
                        #     outFile.write("{}\n".format(newAccountValue))
                        #     outFile.close()


                        okToSell = False
                        okToBuy = True



                    #typically you have two series, A and B. A crosses over B at point i if A[i-1] < B[i-1] and A[i] > B[i] 

                    #put into lootloader server

                    #Insert_Into_Symbol_Tables.Insert_Symbol_Price_andDateTime_Data(symbol, closePrice, localDate, localTime)
                    #Insert_Into_Symbol_Tables.Insert_Symbol_EMA200_andDateTime_Data(symbol, newEma1000Value, localDate, localTime)

                    previousEma200Value = newEma200Value
                    previousEMA200AngleValue = newEMA200AngleValue

                    #suggestions from David Sedivy at the math center
                    #except TYPE:

                    #use continue inside your except statement, after the print statement


                    # #print to terminal
                
                    #closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(counter_ofDataPoints, symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)




                    #if counter_ofDataPoints >= 1000:
                        



                    #print(symbol, newEma200Value)
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
       




