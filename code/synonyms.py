# -*- coding: utf-8 -*-

file_name = '../data/wordbank.txt'

import codecs

#import cwn

def create_cursor():
    import MySQLdb

    conn = MySQLdb.connect(host = 'localhost',
                           port = 5566,
                           user = 'root',
                           charset = 'utf8',
                           passwd = 'root',
                           use_unicode = True,
                           db = 'cwn') # connect to my_laptop SQL
    return conn.cursor()

def query_syndb(File):
    cursor = create_cursor()
    cursor.execute(u"SELECT * FROM 同義詞")
    c = cursor.fetchall()
    for i in range(300):
        print >> File, c[i][0], ", ", c[i][1], ", ", c[i][2], ", ", c[i][3], ", ", c[i][4]

def make_wordbank(file_name):
    cursor = create_cursor()
    cursor.execute(u"SELECT DISTINCT common_schema.replace_all(word, '(012345679', '') FROM 同義詞;")
    words = map(lambda x: x[0], cursor.fetchall())

    dick = {}
    invdick = {}

    cnt = 0
    for word in words:
        query = u"SELECT lemma_id, sense_id FROM 同義詞 where word REGEXP '^%s[(0-9]*$';" % word
        cnt += 1
        if cnt % 100 == 0: print cnt
        cursor.execute(query)
        dick[word] = map(lambda (a, b): a+b, cursor.fetchall())
        for coset in dick[word]:
            if coset not in invdick:
                invdick[coset] = [word]
            else:
                invdick[coset].append(word)
        if cnt % 100 == 0: print word, dick[word]

    with codecs.open(file_name, 'w', encoding='utf8') as File:
        print >>File, "dick = "
        print >>File, dick
        print >>File, "invdick = "
        print >>File, invdick

def read_wordbank(file_name):
    with codecs.open(file_name, 'r', encoding='utf8') as File:
        File.readline()
        dick = eval(File.readline())
        File.readline()
        invdick = eval(File.readline())
    return (dick, invdick)

def query_word(word, dick, invdick):
    if word not in dick:
        return {word: 1}

    mydick = {}
    for coset in dick[word]:
        for coword in invdick[coset]:
            if coword in mydick:
                mydick[coword] += 1
            else:
                mydick[coword] = 1
    return mydick

def pretty_print_query(dick):
    for (a, b) in sorted(dick.items(), key=lambda (a, b): -b):
        print a, " -> ", b

if __name__ == '__main__':
    # this is useless: we need to provide its sense
    #for syn in cwn.Synset().senses:
    #    print syn

    #make_wordbank(file_name)

    (dick, invdick) = read_wordbank(file_name)

    pretty_print_query(query_word(u'按照', dick, invdick))
