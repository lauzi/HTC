# -*- encoding: utf-8 -*-

import codecs

import jieba as jb
jb.load_userdict('../data/dict.txt')
import jieba.posseg as ps

if __name__ == '__main__':
    tmp = u'妳問我，我今天的心情好嗎？我不覺得。好吧！我們去吃泡麵啦'
    xs = list(ps.cut(tmp.strip()))
    with codecs.open('test.txt', 'w', encoding='utf8') as File:
        for token in xs:
            print >>File, token.word, token.flag
