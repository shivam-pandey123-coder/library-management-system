import mysql.connector as mysql

def issue():
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS issue(id INTEGER NOT NULL, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute('INSERT INTO book (title, author, year, isbn) VALUES (%s, %s, %s, %s)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def request_insert(title, author, year, isbn):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="request", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute('INSERT INTO request (title, author, year, isbn) VALUES (%s, %s, %s, %s)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def request_view(title="",author="",year="",isbn=""):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="request", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("SELECT * FROM request")
    rows = cur.fetchall()
    conn.close()
    return rows

def request_delete(title):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="request", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("DELETE FROM request WHERE title=%s", (title,))
    conn.commit()
    conn.close()

def issue_delete(id):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("DELETE FROM issue WHERE id=%s", (id,))
    conn.commit()
    conn.close()

def issue_insert(id):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute('INSERT INTO issue SELECT * FROM book WHERE id=%s', (id,))
    conn.commit()
    conn.close()

def issue_view(title="",author="",year="",isbn=""):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("SELECT * FROM issue")
    rows = cur.fetchall()
    conn.close()
    return rows

def view():
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = mysql.connect(host="localhost", user="root", password="pandey@123", database="books", auth_plugin="mysql_native_password")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
