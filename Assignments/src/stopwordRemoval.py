from util import *

from nltk.corpus import stopwords 


class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""
		stop_words = set(stopwords.words('english')) 
		stopwordRemovedText = []

		for tokenizedsentence in text:
			filtered_sentence = [] 
  
			for w in tokenizedsentence: 
			    if w not in stop_words: 
			        filtered_sentence.append(w)
			stopwordRemovedText.append(filtered_sentence) 

		#Fill in code here

		return stopwordRemovedText
