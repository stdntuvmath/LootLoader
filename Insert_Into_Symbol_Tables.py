import pyodbc


def Insert_Symbol_Price_andDateTime_Data(symbol, price, date, time):
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()


    #insert data int table
    cursor.execute('INSERT INTO {} (Symbol, Price, nDate, nTime) VALUES (\'{}\', {}, \'{}\', \'{}\')'.format(symbol, symbol, price, date, time))
    cursor.commit()
    cursor.close()




def Insert_Into_Historical_Data(symbol, localDate, localTime, closePrice, newEma200Value, newEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10):
    #database stuff

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                        'Database=LootLoader;'
                        'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    #
    #insert data int table
    cursor.execute('INSERT INTO {}_Historical (Symbol, nDate, nTime, Price, EMA200, EMA200Angle, stdrdDev1, stdrdDev2, stdrdDev3, stdrdDev4, stdrdDev5, stdrdDev6, stdrdDev7, stdrdDev8, stdrdDev9, stdrdDev10) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(symbol, symbol, localDate, localTime, closePrice, newEma200Value, newEMA200AngleValue, standardDev, standardDev2, standardDev3, standardDev4, standardDev5, standardDev6, standardDev7, standardDev8, standardDev9, standardDev10))
    cursor.commit()
    cursor.close()


