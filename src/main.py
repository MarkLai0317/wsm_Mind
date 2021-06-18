#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import DataParser
import IR_functions
import os
import sys

if len(sys.argv) > 4 :
	print("too many arguments")
	sys.exit()

embedding_parameter = sys.argv[1]
feedback_list = []

for i in range(2,len(sys.argv)):
	feedback_list.append(sys.argv[i])

str_feedback = [int(10*float(i)) for i in feedback_list]
feedback = [float(i) for i in feedback_list]
str1 = ''.join(str(e) for e in str_feedback)

prediction_file_name = "prediction_" + sys.argv[1] + "_" + str1 + ".txt"
#print(prediction_file_name)
#print(feedback)

news_info_file = '../newsinfo/small_valid_news_0011.tsv'
test_behaviors_file = '../data/MINDsmall_dev/behaviors.tsv'

dp = DataParser.DataParser(news_info_file, test_behaviors_file)

# In[ ]:


number_of_impressions = dp.impressionNum()
score_list = []
answer_list = []
truth = []

print("Number of Impression: ", number_of_impressions)


# In[ ]:

count = 1
for user_impression_ID in range(1, number_of_impressions+1):
  print("Process ", count, " of ", number_of_impressions, end='\r')
  count += 1

  user_history = dp.getHistory(user_impression_ID)
  normalized_history = IR_functions.normalizeHistory(user_history)
  
  user_impression = dp.getImpression(user_impression_ID, data_type = 'valid')
<<<<<<< HEAD
  score = IR_functions.cosSimilarity(normalized_history, user_impression[0])
=======
  score = IR_functions.cosSimilarity(normalized_history, user_impression, feedback)
>>>>>>> 58f1e49ea17fb0785cd017e730f35601df4c8acf

  #truth.append(user_impression[1])
  answer = IR_functions.sortCandidateNews(score)
  answer_list.append(answer)

# In[ ]:

import numpy as np
import os

<<<<<<< HEAD
with open(os.path.join('../result', 'prediction_0011.txt'), 'w') as f:
=======

with open(os.path.join('../result', prediction_file_name, 'w')) as f:
>>>>>>> 58f1e49ea17fb0785cd017e730f35601df4c8acf
  impr_index = 0
  for preds in answer_list:
      impr_index += 1
      pred_rank = '[' + ','.join([str(i) for i in preds]) + ']'
      f.write(' '.join([str(impr_index), pred_rank])+ '\n')

