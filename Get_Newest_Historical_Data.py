from numpy import record
import pyodbc
import datetime



def Pull_LastLine_of_HistoricalData_FromDB(symbol):

    yesterdaysDate = datetime.datetime.today().date()-datetime.timedelta(days=1)
    #print(yesterdaysDate)
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

 

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('SELECT TOP 1 * FROM {}_Historical  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, yesterdaysDate))
    array=[]
    record = []

    for i in cursor:
        array.append(i)



    cursor.close()
    #print(record)

    recordString = str(array)
    crap1 = recordString.replace('[','')
    crap2 = crap1.replace(']','')
    crap3 = crap2.replace('(','')
    crap4 = crap3.replace(')','')
    crap5 = crap4.replace('   \'','')
    crap6 = crap5.replace('\'','')
    crap7 = crap6.replace(' ', '')
    #print(crap7)

    record=crap7.split(',')
    #print("return record")


    return record

    # if(len(record) == 16):
    #     return record
    # elif(len(record) < 16):
    #     record = [symbol,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #     return record
        

    # with LootLoaderDBConnection.cursor() as cursor:

    #     cursor.execute('SELECT TOP 1 * FROM {}_Historical  WHERE nDate = \'{}\' ORDER BY nTime DESC'.format(symbol, yesterdaysDate))
    #     print(cursor.fetchval)
    #     return cursor.fetchone



