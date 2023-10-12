from bdutils import result_as_dict
import uuid

def add_author(cursor,isbn,title,price):
    cursor.execute('INSERT INTO BOOKS (ISBN,TITLE,PRICE,AID) VALUES (?, ?, ?, ?)', (isbn,title,price, uuid.uuid4()))

def add_book_review(cursor,isbn,rating,comment):
    cursor.execute('INSERT INTO REVIEWS (ISBN,COMMENT,RATINGS,USERID) VALUES (?,?,?,?)',isbn,comment,rating,uuid.uuid4())

def add_book(cursor,ISBN,TITLE,PRICE):
    cursor.execute('INSERT INTO BOOKS (ISBN,TITLE,PRICE,AID) VALUES (?,?,?,?)',ISBN,TITLE,PRICE,uuid.uuid4())

def del_book(cursor,isbn):
    cursor.execute('DELETE FROM REVIEWS WHERE ISBN=?',isbn)
    cursor.execute('DELETE FROM BOOKS WHERE ISBN=?',isbn)

def get_all_books(cursor):
    cursor.execute('SELECT * FROM BOOKS')
    authors = result_as_dict(cursor)
    for author in authors:
        print(author)
    
def get_books_isbn(cursor,isbn):
    cursor.execute('SELECT * FROM BOOKS WHERE ISBN=?',isbn)
    x = result_as_dict(cursor)
    for y in x:
        print(y)

def get_books_aid(cursor,aid):
    cursor.execute('SELECT * FROM BOOKS WHERE AID=?',aid)
    x = result_as_dict(cursor)
    for y in x:
        print(y)

def get_book_reviews(cursor,title):
    cursor.execute('SELECT * FORM REVIEWS R,BOOKS B WHERE B.TITLE=? AND B.ISBN=R.ISBN',title)
    x = result_as_dict(cursor)
    for y in x:
        print(y)