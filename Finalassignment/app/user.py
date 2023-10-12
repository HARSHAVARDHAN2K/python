from bdutils import result_as_dict
import uuid

def add_USER(cursor,NAME):
    cursor.execute('INSERT INTO users (userid, user_name) VALUES (?,?)',uuid.uuid4(),NAME)

def add_review(cursor,ISBN,COMMENT,RATINGS,USERID):
    cursor.execute('INSERT INTO REVIEWS (ISBN,COMMENT,RATINGS,USERID) VALUES (?,?,?,?)',ISBN,COMMENT,RATINGS,USERID)