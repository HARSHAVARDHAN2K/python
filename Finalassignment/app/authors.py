from bdutils import result_as_dict
import uuid

def all_authors(cursor):
    cursor.execute('SELECT NAME FROM AUTHOR')
    authors = result_as_dict(cursor)
    for author in authors:
        print(author)

def del_author(cursor,aid):
    cursor.execute('DELETE FROM AUTHOR WHERE AID=?',aid)
    all_authors(cursor)

def add_author(cursor,name):
    cursor.execute('INSERT INTO author (name, aid) VALUES (?, ?)', (name, uuid.uuid4()))

def author_by_id(cursor,id):
    cursor.execute('select * from Author where aid=?',id)
    results= result_as_dict(cursor)
    for res in results:
            print(res)
    
def author_exist(cursor,id):
     result = cursor.execute('SELECT * FROM AUTHOR WHERE AID=?',id)
     return result

def a_update(cursor,name,id):
    if author_exist(cursor,id):
        cursor.execute('UPDATE AUTHOR SET NAME= ? where aid=?',name,id)
    else:
         print(f'Author by that name won\'t exist')

def get_author_review(cursor,isbn):
     cursor.execute('SELECT R.* FROM REVIEWS R, BOOKS B, AUTHOR A WHERE R.ISBN=? AND B.AID=A.AID',isbn)
     results= result_as_dict(cursor)
     for res in results:
            print(res)