import pyodbc
import regex as re
from os.path import exists


def Cleans_And_Insert_Data_forFuckSakeMicrosoft():
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT Symbol FROM All_NASDAQ_Symbols')

    symbolList = [] #you have to start with a list and then convert it to a tuple

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)


    cursor.execute('SELECT Symbol FROM All_NYSE_Symbols')

    #reset variables to use them again
    i=0
    makeString=""
    onlySymbol=""

    for i in cursor:

        makeString = str(i)
        onlySymbol = re.sub('[^a-zA-Z]+', '',makeString) #regex for returning only the upper and lower case letters
        symbolList.append(onlySymbol)

    #alphabetize symbols

    symbolList.sort()



    #return symbolList

    #insert into DB

    # sqlQuery = "INSERT INTO Symbols (Symbol) VALUES (%s)"


    #remove single quotes

    for symbol in symbolList:


        file_exists = exists("PriceData\\priceData2.csv")    

        if(file_exists == True):

            outFile = open("PriceData\\priceData2.csv", "a")
            outFile.write("{},".format(symbol))
            outFile.close()

            

        else:
            outFile = open("PriceData\\priceData2.csv", "a")
            outFile.write("{},".format(symbol))
            outFile.close() 






    #cursor.executemany(sqlQuery, symbolList)


    # for value in symbolList:
        
    #     cursor.executemany(sqlQuery, value)

