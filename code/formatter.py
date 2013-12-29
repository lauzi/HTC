#-*- coding: utf-8 -*-

import codecs
import re

def clean_str(str, invalid=u'，：；、…'):
#    print ">>> get" + str
    for ch in invalid:
        str = str.replace(ch, "")
#    print "<<< ret" + str
    return str

for file_i in range(1,2):

    fin = codecs.open('../data/love0/'+ str(file_i) + '.txt', 'r', encoding='utf8')
    fout = codecs.open('../format/love0/' + str(file_i) + '.txt', 'w', encoding='utf8')

#    fin = codecs.open('in.txt', 'r', encoding='utf8')
#    fout = codecs.open('out.txt', 'w', encoding='utf8')

    count = 0
    rest_str = ""
    for line in fin:
        count += 1
        inp = clean_str(line, u'“”﹝﹞「」”＂『』')
        inp = inp.strip()
        now_lst = re.findall(u'[^。？！]*[。？！]?', inp)
        #   print len(now_lst)
        for now_str in now_lst:
            if len(now_str) > 0:
                flag = (now_str[-1] in u'。？！')
                if flag:
                    print >> fout, (rest_str + clean_str(now_str[:-1]))
                    rest_str = ""
                elif now_str[-1] in u'，：；、…':
                    rest_str = rest_str + clean_str(now_str[:-1])
                else:
                    rest_str = ""
