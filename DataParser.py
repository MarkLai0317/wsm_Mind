import pandas as pd
import numpy as np


class DataParser:
    
    def __init__(self, news_path, behavior_path):
        """init all DF and prosuce news vectors dict"""
        
        self._behaviorDF = pd.DataFrame(pd.read_csv(behavior_path, index_col=0, sep = "\t",header=None))\
        .rename_axis(index='impressionID').rename(columns={1: 'userID', 2: 'time', 3: 'history', 4: 'impressions' })
        
        self._newsDF = pd.DataFrame(pd.read_csv(news_path, index_col=0, sep="\t", header=None))\
        .rename_axis(index="newsID").rename(columns={1: 'vector'})
        
        self._news_vectors = {}
        
        for row in self._newsDF.itertuples():
            self._news_vectors[row.Index] = np.array(row.vector.split(' ')).astype(float)
            
        
    def impressionNum(self):
        """get the size of dataframe, return number of impressions"""
        return len(self._newsDF.index)
    
    def getHistory(self, impressionID):
        """return array of history vectors"""
        history = self._behaviorDF.at[impressionID, 'history']
        if(history != history):
            return np.array([])
        else:    
            news = np.array(history.split(' '))
            history_vectors = []
            for i in range(0, news.size):
                history_vectors.append(self._news_vectors[news[i]])
            return np.array(history_vectors)
            
            
        
    def getImpression(self, impressionID, data_type = "test"):
        """
        tv indicate it's test data or valid data which include -1 -0.
        If its test please input 't' else 'v'.
        If it's t, return impression vectors
        else return (impression vectors, array of 1 0)
        
        """
        news = np.array(self._behaviorDF.at[impressionID, 'impressions'].split(' '))
        
        if(data_type == 'test'):
            impression_vectors = []
            for i in range(0, news.size):
                impression_vectors.append(self._news_vectors[news[i]])
            return np.array(impression_vectors)
        else:
            news = np.char.split(news, '-')
            impression_vectors = []
            impression_answer = []
            for i in range(0, news.size):
                impression_vectors.append(self._news_vectors[news[i][0]])
                impression_answer.append(news[i][1])
                
            return (np.array(impression_vectors), np.array(impression_answer))
        
    
    def _print_behaviorDF(self):
        """dubug method"""
        print(self.behaviorDF)
        
