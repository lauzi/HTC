def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

f = open('../feature/9knife/2.txt', 'r')
fw = open('../ngram/9knife/2.txt', 'w')
total_grams = list()

for line in f:
	token = eval(line)
	grams = find_ngrams(token, 3)
	for gram in grams:
		if gram not in total_grams:
			total_grams.append(gram)

total_grams.sort()

print len(total_grams)
for gram in total_grams:
	print >> fw, gram