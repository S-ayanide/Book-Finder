import sqlite3
Data=sqlite3.connect('fetcher.db')
cur=Data.cursor()
cur.execute('''CREATE TABLE BOOKDATA(
Serial_no INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT(20) NOT NULL,
Price FLOAT NOT NULL);''')
number=int(input("Enter the number of books you want in your library : "))
for i in range(number):
    try:
        title=input("Enter book name: ")
        cost=float(input("Enter price: "))
        cur.execute("INSERT INTO BOOKDATA (Name,Price) VALUES (?,?)",(title,cost))
        print('Data added succesfully')
        Data.commit()
    except:
        print('Error writing data')
        Data.rollback()
Data.close()
