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

	"""
	vect1 is a 1D np.array; user_impressions is a 2D np.array that stores vector of impressions
	return a list of scores of each impression
	"""	
	if vect1.size == 0:
		scores = np.array([np.random.uniform(0,1) for i in range(0,len(user_impressions[0]))])
		return scores
				
	cosValue = np.array([ np.dot(vect1,vector)/(np.linalg.norm(vect1)*np.linalg.norm(vector))\
						for vector in user_impressions])
	return cosValue 

def sortCandidateNews(scores):

	"""
	returns a list of rankings of scores
	"""
	index = np.argsort(scores)[::-1]
	result = np.array([])
	return index

if __name__ == '__main__':
	x = np.array([1,2,3])
	print(cosSimilarity(x,np.array([[1,2,3],[4,5,6],[7,8,9]])))
  #print(normalizeHistory(x))
	print(sortCandidateNews(np.array([8,4,2,1,10])))
