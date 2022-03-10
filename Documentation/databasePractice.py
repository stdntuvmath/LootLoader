import pyodbc
import regex as re



#database stuff

LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                      'Database=LootLoader;'
                      'Trusted_Connection=yes;')

cursor = LootLoaderDBConnection.cursor()

cursor.execute('SELECT Symbol FROM All_NASDAQ_Symbols')

symbolList = list() #you have to start with a list and then convert it to a tuple

for i in cursor:

    makeString = str(i)
    onlySymbol = re.sub('[^a-zA-Z]+', '', makeString) #regex for returning only the upper and lower case letters
    symbolList.append(onlySymbol)

symbolTuple = tuple(symbolList)
print(symbolTuple)