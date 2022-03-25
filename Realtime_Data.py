from urllib.error import HTTPError
from tda.client import Client
from tda.auth import easy_client
import datetime
import Documentation.config_TDA_Live as config_TDA_Live
import All_Symbols
import pytz
from os.path import exists



def Get_Price_Data(numberOfSymbols):

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
                        start_datetime=datetime.datetime.now(),
                        end_datetime=datetime.datetime.now())

            except HTTPError:
                print('HTTPError: Candle data could not be pulled from TDAs server.')


            except TypeError:
                print('TypeError: Candle data could not be pulled from TDAs server.')

            #convert to json
            pricedata = result.json()


            # #parse json data
            for candle in pricedata['candles']:  

                closePrice = candle.get("close","")

                epochTime = candle.get("datetime","")

                tz = pytz.timezone('US/Central')

                stringLocalTime = str(datetime.datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%Y%m%d %H:%M:%S'))#from utc to local time

                stringLocalTimeArray = []

                stringLocalTimeArray = stringLocalTime.split(" ")

                localDate = stringLocalTimeArray[0]
                localTime = stringLocalTimeArray[1]

                #put data into a file
                closingPriceString = "{}, {}, {}, {}".format(symbol, closePrice, localDate, localTime)

                file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

                if(file_exists == True):

                    outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                    outFile.write("{}".format(closingPriceString))
                    outFile.close()            

                else:
                    outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
                    outFile.write("{}".format(closingPriceString))
                    outFile.close()


        counter_ofSymbols+=1
