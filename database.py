import sqlite3

class Database:

    def __init__(self, db_name = "database1.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            query = "create table if not exists Books(id integer primary key autoincrement, title text not null, author text, is_borrowed boolean not null)"

            cursor.execute(query)

            conn.commit()

    def add_book(self, title, author):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "insert into Books(title, author, is_borrowed) values(?, ?, false)"

            cursor.execute(query, (title, author))

            conn.commit()

    def view_all_books(self):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "select id, title, author, is_borrowed from Books"
            cursor.execute(query)

            result = cursor.fetchall()
            
            conn.commit()

            return result

    def delete_book(self, sl_no):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query = "delete from Books where id = ?"
            cursor.execute(query, (sl_no,))

            conn.commit()

    def borrow_book(self, sl_no):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query1 = "select is_borrowed from Books where id = ?"


            cursor.execute(query1, (sl_no,))
            
            result = cursor.fetchone()



            if result == None:

                return f"Book ID not found!"
            
            elif result[0] == 1:

                return f"The book is already borrowed"
            

            else : 
                query = "update Books set is_borrowed = true where id = ?"
                cursor.execute(query, (sl_no,))
                conn.commit()

                return f"Book borrowed successfully"
            
    def return_book(self, sl_no):

        with sqlite3.connect(self.db_name) as conn:

            cursor = conn.cursor()

            query1 = "select is_borrowed from Books where id = ?"
            cursor.execute(query1, (sl_no,))

            result = cursor.fetchone()

            if result is None:
                return "No Book Found"
            
            elif result[0] == 0:

                return "The book is already in the library"
            
            else:

                query = "update Books set is_borrowed = false where id = ?"


                cursor.execute(query, (sl_no,))

                conn.commit()
                return "Book Returned Successfully"

            




