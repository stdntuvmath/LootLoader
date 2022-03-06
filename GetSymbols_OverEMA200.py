import json



#read SymbolList.json file

with open("Stock Symbols\\SymbolList.json", "r") as outfile:#write json data to json file
    # load data into dictionary
    dictionary = json.loads(outfile.read())

#gets the close prices from all the candles from the dictionary json object via python
for key, values in dictionary.items():
    for i in range(len(dictionary["data"])):

        candleEpochTime = dictionary["candles"][i]["datetime"]

        #candleEpochTime = int(dictionary["candles"][i]["datetime"])
        #candleEpochTimeFloat = float(candleEpochTime)
        #currentLocalTimeFromCurrentEpochTime = time.ctime(candleEpochTimeFloat)
        #currentLocalTimeFromCurrentEpochTime = datetime.datetime.fromtimestamp(candleEpochTime).strftime('%Y-%m-%d %H:%M:%S')
        
        print("{} - {}".format(dictionary["candles"][i]["close"], candleEpochTime))

if(dictionary["empty"]==True):
    os.remove("PriceData\\{}_priceData.json".format(symbol))
    print("\n\nSymbol: {} returned no price data for evaluation.\n\n".format(symbol))