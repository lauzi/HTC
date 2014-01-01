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

def query_syndb():
    cursor.execute("SELECT * FROM 同義詞")
    c = cursor.fetchall()
    for i in range(300):
        print c[i][0], ", ", c[i][1], ", ", c[i][2], ", ", c[i][3], ", ", c[i][4]

if __name__ == '__main__':
    query_syndb()

    # this is useless: we need to provide its sense
    for syn in cwn.Synset().senses:
        print syn
