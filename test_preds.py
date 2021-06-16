import numpy as np
import os

answer_list = [[0.3, 0.5, 0.2], # 2 1 3
               [2, 1, 3], # 2 3 1
               []] 

with open(os.path.join('result', 'prediction.txt'), 'w') as f:
  impr_index = 0
  for preds in answer_list:
    impr_index += 1
    pred_rank = (np.argsort(np.argsort(preds)[::-1]) + 1).tolist()
    pred_rank = '[' + ','.join([str(i) for i in pred_rank]) + ']'
    f.write(' '.join([str(impr_index), pred_rank])+ '\n')