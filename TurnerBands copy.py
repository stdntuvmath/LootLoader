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
import Historical_Data
import Trade_Management
import Insert_BuyPrice_IntoDB
import Get_BuyPrice_FromDB
import Insert_AccountValue_IntoDB
import Get_Account_Value


def Run_TurnerBands(numberOfSymbols, toggleHistoricalData):

    counter_ofSymbols=0
    newEma200Value=0
    newEMA200AngleValue = 0
    buyPrice = 0
    sellPrice = 0

    ema200AngleArray = []
    EMA200Array = []
    closePriceArray =[]

    okToBuy = True
    okToSell = False

    #peak = BOOLEAN
    #trough = BOOLEAN




    client = easy_client(
        api_key=config_TDA_Live.api_key,
        redirect_uri=config_TDA_Live.redirect_url,
        token_path=config_TDA_Live.token_path)


    allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()



    
    for symbol in allSymbols:
        if(counter_ofSymbols < numberOfSymbols):

            if(toggleHistoricalData == True):
                #pull newest line of historical data in from DB
               
                oldRecord = Historical_Data.Pull_LastLine_of_HistoricalData_FromDB(symbol)


                #load historical data into Turner Bands process
                                
                localDate = oldRecord[1]
                localTime = oldRecord[2]
                closePrice = oldRecord[3]
                previousEma200Value = oldRecord[4]
                previousEMA200AngleValue = oldRecord[5]        
                standardDev = oldRecord[6]
                standardDev2 = oldRecord[7]
                standardDev3 = oldRecord[8]
                standardDev4 = oldRecord[9]
                standardDev5 = oldRecord[10]
                standardDev6 = oldRecord[11]
                standardDev7 = oldRecord[12]
                standardDev8 = oldRecord[13]
                standardDev9 = oldRecord[14]
                standardDev10 = oldRecord[15]

                ema200AngleArray.append(previousEMA200AngleValue)

                #oldRecord.clear()


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

            elif(toggleHistoricalData == False):


                #get realtime data
            
                try:
                    result = client.get_price_history(symbol,
                                                    
                                                    frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,# a candle is formed every minute
                                                    need_extended_hours_data=True,
                                                    start_datetime=datetime.datetime.now(),
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

                    # closePriceArray.append(closePrice)

                    # if(len(closePriceArray) > 9):
                    #     closePriceArray.remove(closePriceArray[0])
                    oldRecord = Historical_Data.Pull_LastLine_of_HistoricalData_FromDB(symbol)

                    localDate = oldRecord[1]
                    localTime = oldRecord[2]
                    closePrice = oldRecord[3]
                    previousEma200Value = oldRecord[4]
                    previousEMA200AngleValue = oldRecord[5]        
                    standardDev = oldRecord[6]
                    standardDev2 = oldRecord[7]
                    standardDev3 = oldRecord[8]
                    standardDev4 = oldRecord[9]
                    standardDev5 = oldRecord[10]
                    standardDev6 = oldRecord[11]
                    standardDev7 = oldRecord[12]
                    standardDev8 = oldRecord[13]
                    standardDev9 = oldRecord[14]
                    standardDev10 = oldRecord[15]

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
                    accountValueString = str(Get_Account_Value.Get_Account_TEST())
                    numberAndCommaSpace1 = accountValueString.replace("(","")
                    numberAndCommaSpace2 = numberAndCommaSpace1.replace(")","")
                    numberAndCommaSpace3 = numberAndCommaSpace2.replace(",","")
                    numberAndCommaSpace4 = numberAndCommaSpace3.replace(" ","")

                    accountValue = float(numberAndCommaSpace4)

                    
                    if((okToBuy == True 
                    and closePrice > newEma200Value 
                    and previousEMA200AngleValue < standardDev 
                    and newEMA200AngleValue > standardDev
                    ) or
                    (okToBuy == True 
                    and closePrice > newEma200Value 
                    and previousEMA200AngleValue < standardDev2 
                    and newEMA200AngleValue > standardDev2
                    ) or
                    (accountValue > 3000)):


                        buyPrice = closePrice
                        shareAmount = Trade_Management.Get_Share_Amount(buyPrice)
                        Insert_BuyPrice_IntoDB.InsertBuyPrice(symbol, buyPrice, shareAmount)

                        risk = Trade_Management.Get_Risk_Amount(buyPrice)
                        accountValue = accountValue - risk
                        Insert_AccountValue_IntoDB.Insert_AccountValue_TEST(accountValue)
                        closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format("BUY", symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)

                        file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                        if(file_exists == True):

                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}\n".format(closePriceString))
                            outFile.close()            

                        else:
                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}\n".format(closePriceString))
                            outFile.close()




                        sleep(0.25)



                        file_exists = exists("Profit\\profit.csv")    

                        if(file_exists == True):

                            outFile = open("Profit\\profit.csv", "a")
                            outFile.write("{}\n".format(accountValue))
                            outFile.close()            

                        else:
                            outFile = open("Profit\\profit.csv", "a")
                            outFile.write("{}\n".format(accountValue))
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
                        previousEMA200AngleValue > standardDev2 and newEMA200AngleValue < standardDev2 and closePrice > buyPrice and okToSell == True or
                        closePrice < newEma200Value-2*newEma200Value*standardDev10):
                        #fake sell
                        #closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format("SELL", symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)
                        
                        buyPrice = Get_BuyPrice_FromDB.GetBuyPrice(symbol)
                        sellPrice = closePrice
                        shareAmount = Get_BuyPrice_FromDB.Get_numberOfShares(symbol)
                        accountValue = Get_Account_Value.Get_Account_TEST()

                        accountValue = accountValue+((sellPrice-buyPrice)*shareAmount)
                        Insert_AccountValue_IntoDB.Insert_AccountValue_TEST(accountValue)

                        closePriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format("SELL", symbol, closePrice, previousEma200Value,previousEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10, localDate, localTime)

                        file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                        if(file_exists == True):

                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}\n".format(closePriceString))
                            outFile.close()            

                        else:
                            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                            outFile.write("{}\n".format(closePriceString))
                            outFile.close()



                        sleep(0.25)




                        file_exists = exists("Profit\\profit.csv")  



                        if(file_exists == True):

                            outFile = open("Profit\\profit.csv", "a")
                            outFile.write("{}\n".format(accountValue))
                            outFile.close()            

                        else:
                            outFile = open("Profit\\profit.csv", "a")
                            outFile.write("{}\n".format(accountValue))
                            outFile.close()



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
       




