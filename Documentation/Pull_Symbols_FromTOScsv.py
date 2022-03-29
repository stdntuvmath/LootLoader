import json
import csv


def Pull_Symbols():#authentication is not needed for this method

    #convert CSV to JSON

    #create empty dictionary

    data = []
    # lines = []

    # # read file
    # csvFile = open(r"Stock Symbols\WatchListScanner.csv", 'r')
    #     # read an store all lines into list
    # lines = csvFile.readlines()

    # csvFile.close()

    # newCSVFile = open(r"Stock Symbols\WatchListScanner.csv", 'w')
    # for line in lines:
    #     if line.strip("\n") != "Watchlist Scanner":
    #         newCSVFile.write(line)
    
    # newCSVFile.close()


    #read csv file from TD Ameritrade
    with open("Stock Symbols\\WatchListScanner.csv", "r") as csvFile:

        # load csv data into variable
        csvReader = csv.DictReader(csvFile)

        # Convert each row into a dictionary
        # and add it to data
        for row in csvReader:
             if(csvReader[row]):
            
                data.append(row)
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open("Stock Symbols\\WatchListScanner.csv", "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))