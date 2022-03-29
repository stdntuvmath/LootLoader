from urllib.error import HTTPError
from tda.client import Client
from tda.auth import easy_client
import datetime
import Documentation.config_TDA_Live as config_TDA_Live
import All_Symbols
import pytz
from os.path import exists
import Calculate_EMA200
import Calculate_Angle_of_EMA200
import Calculate_Standard_Dev
import Insert_Into_Symbol_Tables
import pyodbc
import regex as re



def Get_Historical_Data_Insert_IntoDB(numberOfSymbols):

    counter_ofSymbols=0
    previousEma200Value = 0
    newEma200Value=0
    previousEMA200AngleValue = 0
    newEMA200AngleValue = 0
    standardDev=0

    ema200AngleArray = []
    EMA200Array = []
    closePriceArray =[]

    #____________________________________________________________________________________________________


    allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()
    counter_ofSymbols = 0

    client = easy_client(
        api_key=config_TDA_Live.api_key,
        redirect_uri=config_TDA_Live.redirect_url,
        token_path=config_TDA_Live.token_path)


    for symbol in allSymbols:
        if(counter_ofSymbols < numberOfSymbols):

            try:
                result = client.get_price_history(symbol,
                                                
                        frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,# a candle is formed every minute
                        need_extended_hours_data=True,
                        start_datetime=datetime.datetime.now() - datetime.timedelta(weeks=4),
                        end_datetime=datetime.datetime.now() - datetime.timedelta(days=1))

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

                #put data into DB
                #closingPriceString = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(symbol, localDate, localTime, closePrice, previousEma200Value, previousEMA200AngleValue, standardDev10, standardDev9, standardDev8, standardDev7, standardDev6, standardDev5, standardDev4, standardDev3, standardDev2, standardDev)


                Insert_Into_Symbol_Tables.Insert_Into_Historical_Data(symbol, localDate, localTime, closePrice, newEma200Value, newEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10)
                previousEma200Value = newEma200Value
                previousEMA200AngleValue = newEMA200AngleValue
        
        counter_ofSymbols+=1
        previousEma200Value = 0
        previousEMA200AngleValue = 0
        EMA200Array.clear()




















def Pull_LastLine_of_HistoricalData_FromDB(symbol):


    todaysDate = datetime.datetime.today().date()
    
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    with LootLoaderDBConnection.cursor() as cursor:

        cursor.execute('SELECT TOP 1 * FROM {}_Historical  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, todaysDate))   

    
        return cursor.fetchone()