import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('test.db')

#tuple of names
fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


#loop through each object in the tuple to find the names taht end in TXT
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one name out of the tuple therefor (x,)
        # will denote a one element tuple for each name ending with txt
            cur.execute("INSERT INTO fileList (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()
