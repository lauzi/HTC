import collections

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

f = open('../feature/9knife/1.txt', 'r')
fw = open('../ngram/9knife/1.txt', 'w')

total_grams = dict()

for line in f:
	token = eval(line)
	grams = find_ngrams(token, 3)

	for gram in grams:
		if gram not in total_grams:
			total_grams[gram] = 0
		else:
			total_grams[gram] += 1

tmp = total_grams.items()
tmp.sort(key=lambda x:x[1], reverse=True)
for t in tmp:
	fw.write(str(t[0]) + '\t' + str(t[1]) + '\n')
