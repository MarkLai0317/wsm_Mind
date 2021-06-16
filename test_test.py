import DataParser
import IR_functions
import os

data_path = './'

news_info_file = 'newsinfo/news_embed.tsv'
test_behaviors_file = os.path.join(data_path, 'test', r'behaviors.tsv')

dp = DataParser.DataParser(news_info_file, test_behaviors_file)

number_of_impressions = dp.impressionNum()
score_list = []
answer_list = []

for user_impression_ID in range(1, number_of_impressions):
  user_history = dp.getHistory(user_impression_ID)
  normalized_history = IR_functions.normalizeHistory(user_history , normalize_way = 'average')
  
  user_impression = dp.getImpression(user_impression_ID)
  score = IR_functions.cosineSimilarity(normalized_history, user_impression[0])
  score_list.append(score)

  answer = IR_functions.sortCandidateNews(score)
  answer_list.append(answer)

import numpy as np
import os

with open(os.path.join('result', 'prediction.txt'), 'w') as f:
  impr_index = 0
  for preds in answer_list:
      impr_index += 1
      pred_rank = (np.argsort(np.argsort(preds)[::-1]) + 1).tolist()
      pred_rank = '[' + ','.join([str(i) for i in pred_rank]) + ']'
      f.write(' '.join([str(impr_index), pred_rank])+ '\n')