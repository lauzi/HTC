import jieba as jb
import jieba.posseg as ps
import collections

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

def freq_dict(ngrams_list):
	d = collections.defaultdict(int)
	for x in ngrams_list:
		d[x] += 1
	return d

for file_i in range(1,21):
	print "."
	f = open('../format/9knife/'+ str(file_i) + '.txt', 'r')
	fw = open('../feature/9knife/' + str(file_i) + '.txt', 'w')

	for line in f:
		tokens = map(lambda x:x.flag, ps.cut(unicode(line.strip(), "utf8")))
		# cut the line into tokens and use its flags
		if tokens:
			print >> fw, tokens
