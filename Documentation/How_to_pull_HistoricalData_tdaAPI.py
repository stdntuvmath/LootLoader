# IMPORTANT NOTE: YOU CANNOT ASK TDA SERVER FOR HISTORICAL DATA ON DAYS THAT THE MARKET IS NOT OPENED. IF YOU DO
# YOU GET error: Bad Request which is a 400 error even though the server is the one creating the issue.



from textwrap import indent
from tda.client import Client
from tda.auth import client_from_token_file
from datetime import datetime, timedelta
import config_TDA_Live
from os.path import exists
import json


client = client_from_token_file(config_TDA_Live.token_path, config_TDA_Live.api_key)

# client = easy_client(
#     api_key=config_TDA_Live.api_key,
#     redirect_uri=config_TDA_Live.redirect_url,
#     token_path=config_TDA_Live.token_path)



result = client.get_price_history('AMD',
                                frequency=Client.PriceHistory.Frequency.EVERY_MINUTE,
                                need_extended_hours_data=True,
                                start_datetime=datetime.today() - timedelta(days=1),
                                end_datetime=datetime.now())

print(result)

pricedata = result.json()


priceDate = json.dumps(pricedata, indent=4)

#print(pricedata)


        #put into a file

        

file_exists = exists("PriceData\\{}_priceData.json".format('AMD'))    

if(file_exists == True):

    outFile = open("PriceData\\{}_priceData.json".format('AMD'), "a")
    outFile.write("{}".format(priceDate))
    outFile.close()            

else:
    outFile = open("PriceData\\{}_priceData.json".format('AMD'), "a")
    outFile.write("{}".format(priceDate))
    outFile.close()