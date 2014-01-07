# -*- encoding: utf-8 -*-

import codecs
import re
import os

import word_freq
import synonym_freq

dirs = ['cityup', '9knife', 'love0']

if __name__ == '__main__':
    for author in dirs:
        files = os.listdir('../wordfreq/%s/' % (author))
        dick = {}
        for subfile in files:
            if re.match(r'\d{1,2}\.txt', subfile) is None: continue

            subdick = word_freq.load_file('../wordfreq/%s/%s' % (author, subfile))

            total = sum(subdick.values())

            for key in subdick:
                weight = float(subdick[key]) / total
                if key not in dick:
                    dick[key] = weight
                else:
                    dick[key] += weight

        with codecs.open('../wordfreq/%s/sum.txt' % (author), 'w', encoding='utf8') as File:
            print >>File, 'freq_dick = '
            print >>File, dick
