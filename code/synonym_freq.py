# -*- coding: utf-8 -*-

import codecs
import sys
import os

import word_freq
import synonyms

def enum_file_names(dirs = None):
    if dirs is None:
        dirs = [('cityup', 5),
                ('9knife', 24),
                ('love0', 2)]

    return ['%s/%s.txt' % (fname, fidx)
            for fname, fidxs in dirs
            for fidx in range(1, fidxs+1)]

if __name__ == '__main__':
    (dick, invdick) = synonyms.read_wordbank('../data/wordbank.txt')
    syn_query_word = lambda word: synonyms.query_word(word, dick, invdick)

    word_freq_prefix = '../wordfreq/'
    wordfreq_files = [word_freq_prefix + fname for fname in enum_file_names()]

    words = dick.keys()

    def count(file_name, output_file = sys.stdout):
        freq_dick = word_freq.load_file(file_name)

        dick = {}
        for word in words:
            if word in freq_dick:
                dick[word] = freq_dick[word]

        print >>output_file, 'File name:', file_name
        for word, freq in sorted(dick.items(), key=lambda x: x[1], reverse=True)[:30]:
            print >>output_file, word, freq

    with codecs.open('tmp.txt', 'w', encoding='utf8') as File:
        for file_name in wordfreq_files:
            count(file_name, File)
