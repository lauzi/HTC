import collections

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

d = collections.defaultdict(int)

f = open('../feature/9knife/1.txt', 'r')
fw = open('../ngram/9knife/1.txt', 'w')

for line in f:
	token = eval(line)
	grams = find_ngrams(token, 3)

	for gram in grams:
		d[gram] += 1

# total_grams.sort()

print len(d)
for gram in d:
	print >> fw, gram