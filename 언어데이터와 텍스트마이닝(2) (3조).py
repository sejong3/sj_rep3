from nltk.corpus import brown
print 'Total Categories: ', len(brown.categories())
print brown.categories()
brown.sents(categories='mystery')
brown.tagged_sents(categories = 'mystery')
