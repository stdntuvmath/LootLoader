import pyodbc
import regex as re


def Get_Account_TEST():#returns a float number

    LootLoaderDBConnection = pyodbc.connect('Driver={SQL Server};'
                                            'Server=DESKTOP-8KIMCEV\SQLEXPRESS;'
                                            'Database=LootLoader;'
                                            'Trusted_Connection=yes;')

    with LootLoaderDBConnection.cursor() as cursor:

        cursor.execute('SELECT * FROM Account_Test')


        return cursor.fetchone()

