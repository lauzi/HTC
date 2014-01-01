path = '../ngram/'
min_gram = 1
max_gram = 10
authors = {'9knife' : 24, 'cityup' : 5, 'love0' : 2}
extensions = '.txt'

for gram in range(min_gram, max_gram+1):
    print "Normalize %d gram(s)..." % (gram)
    for (author, num) in authors.items():
        print "> Proceeding author = %s, # of books = %s" % (author, num)
        normalize_dict = {}
        for book_num in range(1, num+1):
            # open file
            print ">> Now book no. = %d" % (book_num)
            file = open(path+str(gram)+'/'+author+'/'+str(book_num)+'.txt', 'r')
            origin_dict = {}
            appear_count = 0
            # parse from input
            for line in file:
                list_line = line.strip().split();
                now_grams = tuple(list_line[:-1])
                now_appear = int(list_line[-1])
                appear_count += now_appear
                origin_dict[now_grams] = now_appear
            file.close()
            # normailze & insert into dict
            for (k, v) in origin_dict.items():
                normalize_dict[k] = normalize_dict.get(k, 0) + (v * 1.0 / appear_count / num)
        # convert into list
        normalize_list = normalize_dict.items()
        normalize_list.sort(key = lambda x : x[-1], reverse = True)
        # write into output file
        fout = open(path+'/normalized_truncate/'+author+'_'+str(gram)+'.txt', 'w')
        print >> fout, normalize_list[:100]
        fout.close()
