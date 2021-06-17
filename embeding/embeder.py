import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import warnings
warnings.filterwarnings('ignore')  # 警告扰人，手动封存
import gensim

news_path = '/Users/yjack0827/Downloads/wsmMind/data/MINDlarge_test/news.tsv'

news_df = pd.DataFrame(pd.read_csv(news_path, index_col=0, sep="\t", header=None, usecols = [i for i in range(5)]))\
          .rename_axis(index="newsID").rename(columns={1: 'Category', 2: 'SubCategory', 3: 'title', 4: 'Abstract' })

print(news_df.shape)

news_df.fillna("", inplace=True)

#print(news_df)

stemmer = PorterStemmer()
nltk.download('stopwords')

documents = []
count = 1
for i in news_df.index:
    #print('Process ({}, {})\r'.format(count, news_df.index.size))
    print("Process (", count, ",", news_df.index.size, ")", end='\r')

    composed_str = (news_df['Category'][i] + " ")*4 + (news_df['SubCategory'][i] + " ")*2 + news_df['title'][i] + " " + news_df['Abstract'][i]
    
    words = word_tokenize(composed_str)

    pre_process_words = [stemmer.stem(w) for w in words if w not in stopwords.words('english')]

    documents.append(gensim.models.doc2vec.TaggedDocument(pre_process_words, [i]))

    count += 1

print('training...')
model = gensim.models.Doc2Vec(documents, dm=1, vector_size=100, window=8, min_count=5, workers=3)

model.save('model/doc2vec_large_test.model')

with open('../newsinfo/large_test_news.tsv', 'w') as f:
    for news_id in news_df.index:
        f.write(news_id + '\t' + '[' + ' '.join(map(str, model.dv[news_id])) + "]\n")
        break