import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_string TEXT, \
        col_string2 TEXT, \
        )")
    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files (col_string, col_string2) VALUES (?, ?, ?)", \
                ('Hello.txt', 'World.txt'))
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_string, col_string2 FROM tbl_files")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First file: {}\nSecond File: {}".format(item[0],item[1])
    print(msg)

