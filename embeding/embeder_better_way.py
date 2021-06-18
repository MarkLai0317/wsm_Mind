import pandas as pd
from nltk.tokenize import word_tokenize
import gensim
import string

news_path = '/Users/yjack0827/Downloads/wsmMind/data/MINDsmall_dev/news.tsv'

news_df = pd.DataFrame(pd.read_csv(news_path, index_col=0, sep="\t", header=None, usecols = [i for i in range(5)]))\
          .rename_axis(index="newsID").rename(columns={1: 'Category', 2: 'SubCategory', 3: 'title', 4: 'Abstract' })

print(news_df.shape)

news_df.fillna("", inplace=True)

#print(news_df)

#nltk.download('stopwords')

documents = []
count = 1
for i in news_df.index:
    #print('Process ({}, {})\r'.format(count, news_df.index.size))
    print("Process (", count, ",", news_df.index.size, ")", end='\r')

    composed_str = (news_df['Category'][i] + " ")*0 + (news_df['SubCategory'][i] + " ")*0 + news_df['title'][i] + " " + news_df['Abstract'][i]
    
    words = word_tokenize(composed_str)
    #print(words)

    pre_process_words = [w for w in words if w not in string.punctuation]

    #print(pre_process_words)

    documents.append(gensim.models.doc2vec.TaggedDocument(pre_process_words, [i]))

    count += 1

print('training...')
model = gensim.models.Doc2Vec(documents, dm=1, vector_size=64, window=8, min_count=0, workers=2)

model.save('model/doc2vec_small_vaid_0011_nost.model')

with open('../newsinfo/small_valid_news_0011_nost.tsv', 'w') as f:
    for news_id in news_df.index:
        f.write(news_id + '\t' + ' '.join(map(str, model.dv[news_id])) + "\n")