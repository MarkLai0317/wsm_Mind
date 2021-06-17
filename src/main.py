#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import DataParser
import IR_functions
import os

news_info_file = '../newsinfo/news_embed.tsv'
test_behaviors_file = '../test/behaviors.tsv'

dp = DataParser.DataParser(news_info_file, test_behaviors_file)


# In[ ]:


number_of_impressions = dp.impressionNum()
score_list = []
answer_list = []
truth = []

print("Number of Impression: ", number_of_impressions)


# In[ ]:


for user_impression_ID in range(1, number_of_impressions):
  user_history = dp.getHistory(user_impression_ID)
  normalized_history = IR_functions.normalizeHistory(user_history)
  
  user_impression = dp.getImpression(user_impression_ID, data_type = 'test')
  score = IR_functions.cosSimilarity(normalized_history, user_impression[0])

  #truth.append(user_impression[1])

  answer = IR_functions.sortCandidateNews(score)
  answer_list.append(answer)


# In[ ]:


import numpy as np
import os

with open(os.path.join('../result', 'prediction.txt'), 'w') as f:
  impr_index = 0
  for preds in answer_list:
      impr_index += 1
      pred_rank = '[' + ','.join([str(i) for i in preds]) + ']'
      f.write(' '.join([str(impr_index), pred_rank])+ '\n')

