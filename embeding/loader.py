import gensim
import pandas as pd

news_path = '/Users/yjack0827/Downloads/wsmMind/data/MINDsmall_dev/news.tsv'

news_df = pd.DataFrame(pd.read_csv(news_path, index_col=0, sep="\t", header=None, usecols = [i for i in range(5)]))\
          .rename_axis(index="newsID").rename(columns={1: 'Category', 2: 'SubCategory', 3: 'title', 4: 'Abstract' })

model_path = "/Users/yjack0827/Downloads/wsmMind/embeding/model/doc2vec_small_valid_0011.model"

model = gensim.models.Doc2Vec.load(model_path)

#print(model.docvecs)

with open('../newsinfo/small_valid_news_0011.tsv', 'w') as f:
    for news_id in news_df.index:
        print(news_id)
        f.write(news_id + "\t" + ' '.join(map(str, model.dv[news_id])) + "\n")

"""
with open('../newsinfo/large_train_news.tsv', 'w') as f:
    for news_id, i in zip(news_df.index, range(0, news_df.index.size)):
        f.write(news_id + '\t' + ' '.join(map(str, model.dv[i])) + '\n')
"""