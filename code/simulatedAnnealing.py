#-*- coding: utf-8 -*-

import math
import random
import codecs
import copy
import sys
import jieba as jb
import jieba.posseg as ps

gram_path = '../ngram/normalized/9knife_%d.txt'
gram_num = 3
file_name = 'in.txt'
fout = sys.stdout
ftmp = sys.stdout

# simulated annealing
def sa(inputStr, gram_dict, k_max=1000, tem=lambda x: 1.0-x):
    s = ps.cut(inputStr)
    s_now = map(lambda x:(x.word, x.flag), ps.cut(inputStr))
    e_now = energy(s_now, gram_dict)
    k_now = 0
    while k_now < k_max:
        if k_now % (k_max/10) == 0:
            print >> ftmp, ("k_now = %d, e_now = %f %s" % (k_now,  e_now, tokens_to_str(s_now)))
        s_nxt = get_neighbor(s_now)
        e_nxt = energy(s_nxt, gram_dict)
        if (e_nxt > e_now) or random.random() < math.exp(-(e_now-e_nxt)*1.0/tem(k_now*1.0/k_max)):
            s_now = s_nxt
            e_now = e_nxt
        
        k_now = k_now +1
    return s_now

# tokens to string
def tokens_to_str(tokens):
    return "".join(map(lambda x:x[0], tokens))
    
# get neighbor
def get_neighbor(_tokens, magic=0.999, gap=1):
    tokens = list(_tokens)
    if random.random() < magic:
        # shuffle
        if len(tokens) > 1:
            pos1 = random.randint(0, len(tokens)-1)
            pos2 = random.randint(max(pos1-gap,0), min(pos1+gap,len(tokens)-1))
            tmp = tokens[pos1]
            tokens[pos1] = tokens[pos2]
            tokens[pos2] = tmp
    else:
        # duplicate
        pos = random.randint(0, len(tokens)-1)
        tokens.insert(pos, tokens[pos])
    '''
        # remove
        if len(tokens) > gram_num:
            pos = random.randint(0, len(tokens)-1)
            if tokens[pos][1] != 'n':
                tokens.pop(pos)
    '''
    
    return tokens

# fine ngrams
def find_ngrams(lst):
	return zip(*[lst[i:] for i in range(gram_num)])

# calc the energy of current tokens
def energy(tokens, gram_dict):
    lst = find_ngrams(map(lambda x:x[1], tokens))
    if lst:
        energy_count = 0.0
        for gram in lst:
            energy_count += gram_dict.get(gram, 0)
        return energy_count / len(lst) * 100000
    else:
        return 0

# get dictionary from eval the target file
def get_dict():
    fin = open(gram_path % gram_num, 'r')
    return eval(fin.readline().strip())

# sort of preprocessing ...
def solve(inputStr, gram_dict):
    after_tokens = sa(inputStr, gram_dict)
    return tokens_to_str(after_tokens)

# clean any not-word symbol
def clean_str(str, invalid=u'，：；、…，。！？“”﹝﹞「」”＂『』《》—　 （）'):
    for ch in invalid:
        str = str.replace(ch, "")
    return str

if __name__ == "__main__":
    # input interface
    ftmp = codecs.open('out.txt', 'w', encoding='utf8')
    if len(sys.argv) > 1:
        pre_arg = ""
        for arg in sys.argv[1:]:
            if arg == "-out" or arg == "-gnum" or arg == "-in":
                pre_arg = arg
            else:
                if pre_arg == "-out":
                    fout = codecs.open(arg, 'w', encoding='utf8')
                elif pre_arg == "-gnum":
                    gram_num = int(arg)
                elif pre_arg == "-in":
                    file_name = arg
                else:
                    print "syntax: -out outfile -in infile -gnum num_of_gram"
                    exit()

    # init
    gram_dict = get_dict()
    jb.load_userdict('../data/dict.txt')
    
    # process input
    fin = codecs.open(file_name, 'r', encoding='utf8')
    for line in fin:
        inp = clean_str(line)
        inp = inp.strip()
        if len(inp) > gram_num:
            print >> fout, "Origin Str:\n%s" % (inp)
            print >> fout, "After Str:\n%s" % (solve(inp, gram_dict))
    fin.close()
    ftmp.close()
