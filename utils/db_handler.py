import sqlite3


def get_news():
    db = sqlite3.connect('cowback.db')
    c = db.cursor()
    c.execute(" SELECT * FROM news ORDER BY ID desc LIMIT 10 ") # only get the last 10 news
    content = ""
    for row in c:
        content += '\n{0}\n{1}\n{2}\n\n'.format(row[1], row[2], row[3]) #row[0] is id
    db.close()
    return content

def insert_news(pubdate, title, content):
    db = sqlite3.connect('cowback.db')
    c = db.cursor()

    # make sure the table already exists, if not create one
    c.execute(" CREATE TABLE IF NOT EXISTS news ( id INTEGER PRIMARY KEY AUTOINCREMENT, pubdate DATE, title TEXT, content TEXT) ")
    
    c.execute(' INSERT INTO news VALUES (null, ?, ?, ?) ', (pubdate, title, content))
    db.commit()
    db.close()

def clear_table(table_name):
    db = sqlite3.connect('cowback.db')
    c = db.cursor()
    c.execute(" DELETE FROM " + table_name + " WHERE id >= 0 ")
    db.commit()
    db.close()
    print("clear_table done")
