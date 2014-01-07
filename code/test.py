# -*- encoding: utf-8 -*-

import codecs

import jieba as jb
jb.load_userdict('../data/dict.txt')
import jieba.posseg as ps

if __name__ == '__main__':
    tmp = u'我餓了'
    xs = list(ps.cut(tmp.strip()))
    with codecs.open('test.txt', 'w', encoding='utf8') as File:
        for token in xs:
            print >>File, token.word, token.flag
