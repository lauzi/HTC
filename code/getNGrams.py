import collections

def find_ngrams(input_list, n):
	return zip(*[input_list[i:] for i in range(n)])

dir_name = ["cityup", "9knife", "love0"]
dir_num = [5, 24, 2]

for dir_i in range(3):
	print "doing ... ", dir_name[dir_i]
	
	for file_i in range(1, dir_num[dir_i] + 1):
		f = open('../feature/' + dir_name[dir_i] + '/' + str(file_i) + '.txt', 'r')
		for n in range(3,8):# for each n-grams
			print dir_name[dir_i], file_i, n, "-grams"
			fw = open('../ngram/' + str(n) + '/' + dir_name[dir_i] + '/' + str(file_i) + '.txt', 'w')
			total_grams = dict()
			for line in f:
				token = line.strip().split(' ')
				if len(token) < n: continue#too short for ngrams
				
				grams = find_ngrams(token, n)

				for gram in grams:
					if gram not in total_grams:
						total_grams[gram] = 1
					else:
						total_grams[gram] += 1

			tmp = total_grams.items()
			tmp.sort(key=lambda x:x[1], reverse=True)
			for t in tmp:
				fw.write(str(t[0]) + ' ' + str(t[1]) + '\n')
