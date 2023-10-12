import pyodbc as db
from bdutils import result_as_dict
import authors

 

#import utils

 

def main():
    driver='{ODBC Driver 18 for SQL Server}'
    server=r'localhost\SQLEXPRESS'
    database='LIBRARY'
    encrypt='no'
    trusted_connection='yes'

 

    connection_string=f'''
            DRIVER={driver};
            SERVER={server};
            DATABASE={database};
            trusted_connection={trusted_connection};
            ENCRYPT={encrypt};'''
    print(connection_string)

    with db.connect(connection_string) as connection:
        cursor=connection.cursor()
        result = cursor.execute('select * from books')
        print(result)
        for i in result:
            print(i.TITLE)
        # name = input("enter the Author to add:")
        
        # authors.all_authors(cursor)
        # authors.del_author(cursor,'8f7877ae-94f9-46e6-98b4-37adb862477f')
        # authors.add_author(cursor,'Robert kiyoski')
        # authors.all_authors(cursor)
        authors.author_by_id(cursor,'252ff8a6-f0ba-4f9a-8ffe-4c28fae33172')
        # authors.a_update(cursor,'Shakessphere','4060e260-a4b3-4d46-8e48-8114e55db281')
        authors.get_author_review(cursor,'9788129115356')
        connection.commit()

        

 

main()

