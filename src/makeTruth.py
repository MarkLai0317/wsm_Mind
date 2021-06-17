import DataParser
import IR_functions
import pandas as pd
import os

small_valid_behaviors_file = '../../MINDsmall_valid/behaviors.tsv'

behavior_path = small_valid_behaviors_file

behavior_df = pd.DataFrame(pd.read_csv(behavior_path, index_col=0, sep = "\t",header=None))\
        .rename_axis(index='impressionID').rename(columns={1: 'userID', 2: 'time', 3: 'history', 4: 'impressions' })





import numpy as np

def getImpressionTruth(impressionID):
  news = np.array(behavior_df.at[impressionID, 'impressions'].split(' '))
  news = np.char.split(news, '-')

  impression_answer = []
  for i in range(0, news.size):
      impression_answer.append(news[i][1])
          
  return np.array(impression_answer)


truth_list = []

for impression_id in range(1, behavior_df.index.size):

    print("(", impression_id, ", ", behavior_df.index.size, ")", end='\r')

    truth = getImpressionTruth(impression_id)

    truth_list.append(truth)





with open(os.path.join('../truth', 'small_valid_truth.tsv'), 'w') as f:
  for i, t in zip(behavior_df.index, truth_list):
    f.write(str(i) + " [" + ",".join(map(str, t)) + "]\n")