import codecs
import re

def clean_str(str, invalid=u'，：；、…'):
#	print ">>> get" + str
	for ch in invalid:
		str = str.replace(ch, "")
#	print "<<< ret" + str
	return str

dir_name = ["cityup", "9knife", "love0"]
dir_num = [5, 24, 2]

for dir_i in range(3):
	print "doing ... ", dir_name[dir_i]
	for file_i in range(1, dir_num[dir_i] + 1):
		for gram_num in range(2,5):
			print "now in file ", dir_name[file_i]
			f = open('../data/' + dir_name[dir_i] + '/'+ str(file_i) + '.txt', 'r')
			fw = open('../wordgram/' + str(gram_num) + '/' + dir_name[dir_i] + '/'+ str(file_i) + '.txt', 'w')
			count = 0
			for line in f:
				count += 1
				if count % 100 == 0: print "working ... file", file_i, " .. line ", count
				tokens = map(lambda x:x.word, ps.cut(unicode(line.strip(), "utf8")))
				# cut the line into tokens and use its flags
				for token in tokens:
					fw.write(token + ' ')
					print token
				break
				fw.write('\n')