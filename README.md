# Book-Finder
Open the Database.py file and add the names of books you want in your library
Open BookFinder.py file and enter the book you want to search 
It will fetch you the book price

--------------------------------------------------------------------------------------------------------------------
def EnterTitle(self):
        import sqlite3
        Data1=sqlite3.connect('fetcher.db')
        c=Data1.cursor()
        t=self.t1.text()
        c.execute("SELECT Price FROM BOOKDATA WHERE Name='"+t+"';")
        rec=c.fetchone()
        if rec!=None:
            self.pr=rec[0]
            self.t2.setText(str(self.pr))
        else:
            self.t2.setText('Book not found')
----------------------------------------------------------------------------------------------------------------------
Function EnterTitle takes the data writter in text format from the box
Searches and displays it in the Price box below
