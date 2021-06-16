import math 
import numpy as np
import random

def normalizeHistory(historyVectors,normalizeWay='arithmetic'):

	#return an empty array if historyVectors is an empty array
	if(historyVectors.size == 0):
		return np.array([])


	# normalize each vector

	newVectors = np.empty((0,len(historyVectors[0])),float)
	for vector in historyVectors:
		total = 0
		for i in vector:
			total += i**2
		length = math.sqrt(total)
		newVect = np.array([])
		for i in range(len(vector)):
			newVect = np.append(newVect, vector[i]/length)
		newVectors = np.append(newVectors,np.array([newVect]),axis=0)


	# different ways to average

	# arithmetic mean

	if(normalizeWay == "arithmetic"):
		arithmeticMeanVector = np.array([])
		for j in range(0,len(newVectors[0])):
			total = 0
			for i in range(0,len(newVectors)):
				total += newVectors[i][j]
			arithmeticMean = total/len(newVectors) 
			arithmeticMeanVector = np.append(arithmeticMeanVector,arithmeticMean)
		return arithmeticMeanVector

	# geometric mean

	if(normalizeWay == "geometric"):
		geometricMeanVector = np.array([])
		for j in range(0,len(newVectors[0])):
			total_product = 1
			for i in range(0,len(newVectors)):
				total_product *= newVectors[i][j]
			geometricMean = pow(total_product,1/len(newVectors))
			geometricMeanVector = np.append(geometricMeanVector,geometricMean)
		return geometricMeanVector
	
			
def cosSimilarity(vect1, user_impressions):
	
	#scores = np.array([])
  scores = []
  if vect1.size == 0:
    for i in range(0,len(user_impressions[0])):
      scores.append(random.uniform(0,1))
  
    return scores
  
  for vector in user_impressions:
	  cosValue = np.dot(vect1,vector)/(np.linalg.norm(vect1)*np.linalg.norm(vector))
		#scores = np.append(scores,cosValue)
	  scores.append(cosValue)
  return scores 

def sortCandidateNews(scores):
	
	index = [ i for i in range(1,len(scores)+1) ]
	indexScore = dict(zip(index,scores))
	sortedIndexScore={ k:v for k,v in sorted(indexScore.items(),key=lambda x:x[1],reverse=True)}
	order = list(sortedIndexScore)
	for i in range(0,len(order)):
		indexScore[order[i]] = i+1
	
	result = list(indexScore.values())
	return result

	
if __name__ == '__main__':
  x = np.array([])
  print(cosSimilarity(x,np.array([[1,2,3],[4,5,6],[7,8,9]])))
  print(normalizeHistory(x))
  print(sortCandidateNews(np.array([0.4,0.1,0.2])))
