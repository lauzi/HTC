import jieba as jb
jb.load_userdict('../data/dict.txt')
import jieba.posseg as ps
import collections

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

def freq_dict(ngrams_list):
	d = collections.defaultdict(int)
	for x in ngrams_list:
		d[x] += 1
	return d

for file_i in range(1,2):
	print "fomatting in file ", file_i

	f = open('../format/cityup/'+ str(file_i) + '.txt', 'r')
	fw = open('../feature/cityup/' + str(file_i) + '.txt', 'w')
	count = 0
	for line in f:
		count += 1
		if count % 10 == 0:
			break
			print "working ... file", file_i, " .. line ", count
		tokens = map(lambda x:x.flag, ps.cut(unicode(line.strip(), "utf8")))
		# cut the line into tokens and use its flags
		for token in tokens:
			fw.write(token + ' ')
		fw.write('\n')
