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
	
			
def cosSimilarity(vect1, user_impressions, feedback = []):

	"""
	vect1 is a 1D np.array; user_impressions is a 2D np.array that stores vector of impressions
	feedback = [0.3,0.2] then feedback value = 0.5*cosValue + 0.3*largestImp + 0.2*secondImp
	return a np.array of scores of each impression
	"""	
	
	if sum(feedback) > 0.5 :
		print("sum of feedback should better not be larger than 0.5")

	if vect1.size == 0 :
		scores = np.array([np.random.uniform(0,1) for i in range(0,len(user_impressions[0]))])
		return scores
				
	cosValue = np.array([ np.dot(vect1,vector)/(np.linalg.norm(vect1)*np.linalg.norm(vector))\
						  for vector in user_impressions])

	#without relavance feedback or the feedback list is longer than user_impressions
	if feedback == [] and len(user_impressions) <= len(feedback) :
		return cosValue

	
	copyCosValue = [i for i in cosValue]
	#find the n largest index 
	largestNIndex = []
	for i in range(0, len(feedback)): 
		tempLargest = 0    
		for j in range(len(copyCosValue)):     
			if copyCosValue[j] > copyCosValue[tempLargest]:
				tempLargest = j
		copyCosValue[tempLargest] = -1
		largestNIndex.append(tempLargest)

	# feedbackVect = (1-sum(feedback))*vect1 + feedback[0]*user_impression +
	#				  feedback[1]*user_impression

	feedbackVect = np.multiply(vect1,1-sum(feedback))
	for i in range(0,len(feedback)):
		feedbackVect = np.add(feedbackVect,np.multiply(user_impressions[largestNIndex[i]]\
														,feedback[i]))
	
	feedbackValue = np.array([np.dot(feedbackVect,vector)/(np.linalg.norm(feedbackVect)\
							*np.linalg.norm(vector))  for vector in user_impressions])

	return feedbackValue


def sortCandidateNews(scores):

	"""
	returns a list of rankings of scores
	"""
	index = np.argsort(scores)[::-1]
	result = np.empty(len(scores),int)
	for i in range(0,len(scores)):
		result[index[i]] = i+1
	return list(result)

if __name__ == '__main__':
	x = np.array([1,2,3])
	y = np.array([[3,2,1],[4,5,6],[7,0,0]])
	print(cosSimilarity(x,y))
	print(cosSimilarity(x,y,feedback=[0.3,0.1]))
  #print(normalizeHistory(x))
#	print(sortCandidateNews(np.array([3,1,2])))
