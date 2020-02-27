from util import *

# Add your import statements here
# nltk.download('stopwords')
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
		print(stop_words)
		stopwordRemovedText = []

		for tokenizedsentence in text:
			filtered_sentence = [] 
  
			for w in tokenizedsentence: 
			    if w not in stop_words: 
			        filtered_sentence.append(w)
			stopwordRemovedText.append(filtered_sentence) 

		#Fill in code here

		return stopwordRemovedText


# tester = [["plate", "in", "an", "incompressible", "a", "an", "the", "fluid", "of", "small", "viscosity"],["hello", "hi", "how"]] #the study of high-speed viscous flow past a two-dimensional body it is usually necessary to consider a curved shock wave emitting from the nose or leading edge of the body .  consequently, there exists an inviscid rotational flow region between the shock wave and the boundary layer .  such a situation arises, for instance, in the study of the hypersonic viscous flow past a flat plate .  the situation is somewhat different from prandtl's classical boundary-layer problem . in prandtl's original problem the inviscid free stream outside the boundary layer is irrotational while in a hypersonic boundary-layer problem the inviscid free stream must be considered as rotational .  the possible effects of vorticity have been recently discussed by ferri and libby .  in the present paper, the simple shear flow past a flat plate in a fluid of small viscosity is investigated .  it can be shown that this problem can again be treated by the boundary-layer approximation, the only novel feature being that the free stream has a constant vorticity .  the discussion here is restricted to two-dimensional incompressible steady flow ."
# a = StopwordRemoval()
# b = a.fromList(tester)
# print(b)

	