import mysql.connector

def get_connect():
    return mysql.connector.connect(
       host = "localhost",
        user = "root",
        passwd = "",
        database = "library_db",

    )
# print("Connected to MySQL Server version:", get_connect().server_info)
if __name__ == "__main__":
    try:
        db = get_connect()
        print("Connected to MySQL Server version:", get_connect().server_info)
    except mysql.connector.Error as err:
        print("Connection error:", err)
    finally:
        try:
            db.close()
        except Exception:
            pass

def add_book(title,author,isbn):
    db = get_connect()
    cursor = db.cursor()
    try:
        sql = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
        cursor.execute(sql,(title,author,isbn))
        db.commit()
        print("Book added successfully")
    except mysql.connector.Error as err:
        print("Failed to add book", err)
        db.rollback()
    finally:
        cursor.close()
        db.close()

# if __name__ == "__main__":
#     add_book("The Hobbit", "J. R. R. Tolkien", "978-0547928227")
def search_book(title_query):
    db = get_connect()
    cursor = db.cursor(dictionary=True)

    try:
        sql = "SELECT id, title, author, ISBN FROM books WHERE title LIKE %s"
        params =f"%{title_query}%"
        cursor.execute(sql,(params,))
        result = cursor.fetchall()
        db.commit()
        if not result:
            print("No books found")
        else:
            for row in result:
                print(f"ID: {row['id']} | Title: {row['title']} | Author: {row['author']} | ISBN: {row['ISBN']}")
    except mysql.connector.Error as err:
        print("Failed to search book", err)
    finally:
        cursor.close()
        db.close()



if __name__ == "__main__":
    search_book('The Hobbit')   # should show The Hobbit
