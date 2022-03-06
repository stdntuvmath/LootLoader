from time import sleep
from tda.client import Client
from tda.auth import easy_client
from datetime import datetime, timedelta
import Documentation.config_TDA_Live as config_TDA_Live
import pytz
import All_Symbols
from os.path import exists
from time import sleep




client = easy_client(
    api_key=config_TDA_Live.api_key,
    redirect_uri=config_TDA_Live.redirect_url,
    token_path=config_TDA_Live.token_path)


allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()

first100 = []
second100 = []
counter = 0

# for symbol in allSymbols:
    
#     if counter < 101:
#         first100.append(symbol)

#     if counter > 99 & counter < 201:
#         second100.append(symbol)

for symbol in allSymbols:


    result = client.get_price_history(symbol,
                                    frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                                    need_extended_hours_data=True,
                                    start_datetime=datetime.now() - timedelta(days=1),
                                    end_datetime=datetime.now())


    pricedata = result.json()



    for candle in pricedata['candles']:
        
        closePrice = candle.pop("close")

        epochTime = candle.pop("datetime")

        tz = pytz.timezone('US/Central')

        localTime = datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')#from utc to local time

        # priceArray.append(closePrice)
        # timeArray.append(localTime)
        # symbolArray.append(stockSymbol)

        closePriceString = "{}, {}, {}\n".format(symbol, closePrice, localTime)
        #print(closePriceString)


        file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

        if(file_exists == True):

            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
            outFile.write("{}".format(closePriceString))
            outFile.close()            

        else:
            outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
            outFile.write("{}".format(closePriceString))
            outFile.close()

        #sleep(0.00001)









# for symbol in second100:


#     result = client.get_price_history(symbol,
#                                     frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
#                                     need_extended_hours_data=True,
#                                     start_datetime=datetime.now() - timedelta(minutes=200),
#                                     end_datetime=datetime.now())


#     pricedata = result.json()



#     for candle in pricedata["candles"]:
        
#         closePrice = candle.pop("close")

#         epochTime = candle.pop("datetime")

#         tz = pytz.timezone('US/Central')

#         localTime = datetime.utcfromtimestamp(epochTime / 1000).replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')#from utc to local time

#         # priceArray.append(closePrice)
#         # timeArray.append(localTime)
#         # symbolArray.append(stockSymbol)

#         closePriceString = "{}, {}, {}\n".format(symbol, closePrice, localTime)
#         #print(closePriceString)


#         file_exists = exists("PriceData\\{}_priceData.csv".format(symbol))    

#         if(file_exists == True):

#             outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
#             outFile.write("{}".format(closePriceString))
#             outFile.close()            

#         else:
#             outFile = open("PriceData\\{}_priceData.csv".format(symbol), "a")
#             outFile.write("{}".format(closePriceString))
#             outFile.close()

