import requests
import json



def Pull_Symbols(symbol):#authentication is not needed for this method

      response = json.dumps(requests.get('https://api.nasdaq.com/api/screener/stocks', params={'tableonly' : 'true', 'limit' : 500,'exchange' : 'all'}, headers={"User-Agent": "Mozilla/5.0 (x11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0"}).json(), indent=4)


      with open("Stock Symbols\\SymbolList.json", "w") as outfile:#write to json file
            outfile.write(response)

      #print(response)



      # #read a json file
      with open("Stock Symbols\\SymbolList.json", "r") as outfile:#write json data to json file
            # load data into dictionary
            dictionary = json.loads(outfile.read())

      symbols = []

      for key, values in dictionary.items():
            for i in range(len(dictionary["data"]["table"]["rows"])):

                  symbolJson = "{}".format(dictionary["data"]["table"]["rows"][i]["symbol"])
                  print(symbol)

                  
                  symbols.append(symbol)


      with open("Stock Symbols\\Symbols.csv", "w") as outfile:#write to json file
            outfile.write(str(symbols))

      with open("Stock Symbols\\Symbols.csv", 'wb') as outfile:
            json.dump(outfile)

      print(symbols)

      #print(len(dictionary["data"]["table"]["rows"]))

      