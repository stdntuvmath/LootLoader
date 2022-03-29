import pyodbc


def Insert_AccountValue_TEST(accountValue):#returns a float number

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    cursor = LootLoaderDBConnection.cursor()

    cursor.execute('INSERT INTO Account_Test VALUES (\'{}\')'.format(accountValue))
    
    cursor.commit()
    cursor.close()