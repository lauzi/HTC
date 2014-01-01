# -*- coding: utf-8 -*-

import cwn
import MySQLdb

conn = MySQLdb.connect(host = 'localhost',
                       port = 5566,
                       user = 'root',
                       charset = 'utf8',
                       passwd = 'root',
                       db = 'cwn') # connect to my_laptop SQL
cursor = conn.cursor()

if __name__ == '__main__':
    cursor.execute("SELECT * FROM 同義詞")
    c = cursor.fetchall()
    for i in range(300):
        print c[i][0], ", ", c[i][1], ", ", c[i][2], ", ", c[i][3], ", ", c[i][4]

    #print ', '.join(map(str, list(c[0])))
    cwn.synsets('食物')
