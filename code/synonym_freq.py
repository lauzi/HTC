# A library for word swapping.
#
# A word's preference = syn_weight * (synonym_freq.freq_offset + actual word freq)
#
# Example:
# import synonym_freq
# import word_freq
# import synonyms
# (dick, invdick) = synonyms.read_wordbank('../data/wordbank.txt')
# freq_dick = word_freq.load_file(file_name)
# candidates = synonym_freq.query('duck', dick, invdick, freq_dick)
# print candicates

# -*- coding: utf-8 -*-

import codecs
import sys

import word_freq
import synonyms

freq_offset = 3

def enum_file_names(dirs = None):
    if dirs is None:
        dirs = [('cityup', 5),
                ('9knife', 24),
                ('love0', 2)]

    return ['%s/%s.txt' % (fname, fidx)
            for fname, fidxs in dirs
            for fidx in range(1, fidxs+1)]

def reweight(dick):
    """Reweights a DICKTIONARY so that its values' sum will be 1"""

    total = sum(dick.items())
    return {key: float(val)/total for key, val in dick}

def query(word, dick, invdick, freqdick):
    """Returns [(syn, prob.)] where `syn` is a synonym of `word` and
    `prob.` is its weight, i.e. how much we prefer it."""
    global freq_offset

    # sim for similarities
    syn_sims = reweight(synonyms.query_word(word, dick, invdick))

    # we should give any word a chance
    res_freqs = reweight({key: val * (freqdick.get(key, 0) + freq_offset)
                          for key, val in syn_sims})

    return sorted(res_freqs.iteritems(), lambda x: x[1], reversed=True)
    return res_freq.items() # comment prev. line if we don't need to sort the result

if __name__ == '__main__':
    (dick, invdick) = synonyms.read_wordbank('../data/wordbank.txt')
    syn_query_word = lambda word: synonyms.query_word(word, dick, invdick)

    word_freq_prefix = '../wordfreq/'
    wordfreq_files = [word_freq_prefix + fname for fname in enum_file_names()]

    words = dick.keys()

    def count(file_name, output_file = sys.stdout):
        freq_dick = word_freq.load_file(file_name)

        syn_freq_dick = {}
        for word in words:
            if word in freq_dick:
                syn_freq_dick[word] = freq_dick[word]

        print >>output_file, 'File name:', file_name
        total = sum(syn_freq_dick.values())
        for word, freq in sorted(syn_freq_dick.iteritems(), key=lambda x: x[1], reverse=True)[:30]:
            print >>output_file, word, '%d/%d =' % (freq, total), float(freq) / total

    with codecs.open('../wordfreq/synonym_freqs.txt', 'w', encoding='utf8') as File:
        for file_name in wordfreq_files:
            count(file_name, File)
