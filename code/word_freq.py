# -*- coding: utf-8 -*-

import codecs
import os

import jieba as jb
jb.load_userdict('../data/dict.txt')
import jieba.posseg as ps

dirs = [('cityup', 5),
        ('9knife', 24),
        ('love0', 2)]

def check_dir(path):
    dirs = path.split('/')
    for i in range(len(dirs)):
        subpath = '/'.join(dirs[:i+1])
        if not os.path.isdir(subpath):
            os.mkdir(subpath)

def count_freqs_from_files(thres):
    for dir_i in range(len(dirs)):
        (dir_name, dir_num) = dirs[dir_i]
        print 'doing ... ', dir_name
        for file_i in range(1, dir_num + 1):
            file_name = '%s/%s.txt' % (dir_name, file_i)
            res_dir_name = '../wordfreq/' + dir_name
            print 'now in file', file_name

            word_dick = {}

            with codecs.open('../format/' + file_name, 'r', encoding='utf8') as File:
                count = 0
                for line in File:
                    count += 1
                    if count % 100 == 0:
                        print 'working ... file', file_name, '.. line', count
                    for token in ps.cut(line.strip()):
                        word = token.word
                        if word in word_dick:
                            word_dick[word] += 1
                        else:
                            word_dick[word] = 1

            check_dir(res_dir_name)
            with codecs.open('../wordfreq/' + file_name, 'w', encoding='utf8') as File:
                print >>File, 'freq_dick = '
                print >>File, {k: v for k, v in word_dick.iteritems() if v > thres}

def raise_threshold(new_thres):
    for dir_i in range(len(dirs)):
        (dir_name, dir_num) = dirs[dir_i]
        print 'doing ... ', dir_name
        for file_i in range(1, dir_num + 1):
            file_name = '%s/%s.txt' % (dir_name, file_i)
            print 'now in file', file_name

            with codecs.open('../wordfreq/' + file_name, 'r', encoding='utf8') as File:
                File.readline()
                word_dick = eval(File.readline())

            with codecs.open('../wordfreq/' + file_name, 'w', encoding='utf8') as File:
                print >>File, 'freq_dick = '
                print >>File, {k: v for k, v in word_dick.iteritems() if v > new_thres}

if __name__ == '__main__':
    count_freqs_from_files(5)
    raise_threshold(8)
