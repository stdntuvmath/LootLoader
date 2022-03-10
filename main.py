from __future__ import print_function
from logging import exception
import os
from typing_extensions import Self
from tda import auth, client, orders
import json
import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
from ta.trend import ema_indicator
import tda
import OAuth_Authenticate
import Pull_Symbols_FromTDA
import Pull_Symbols_FromTOScsv
import ta
import asyncio
import threading
import RetrieveLiveData
import All_Symbols
import Get_Historical_PriceData
import Setup.Create_Symbol_Tables as createTables
import Setup.Delete_Symbol_Tables_FromDB as deleteTables

#allSymbols = All_Symbols.Return_ALL_Symbols_FromDB()
createTables.CreateTables()
#deleteTables.DeleteTables()
#Get_Historical_PriceData.Get_Price_Date_InsertInto_DB()
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