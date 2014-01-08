# -*- encoding: utf-8 -*-

import codecs

import rand_word
import synonym_freq

if __name__ == '__main__':
    words = u'我，覺得，太陽，裡面，沒有，太陽餅，是，一件，很，奇怪，的，事'.split(u'，')
    tokens = zip(words, 'w'*100)
    with codecs.open('tmp.txt', 'w', encoding='utf8') as File:
        for _ in range(10):
            for word in rand_word.sub(tokens, 'love0'):
                print >>File, word,
            print >>File
