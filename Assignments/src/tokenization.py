from util import *

# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		delimiters = "; |, |\* |\n| |: "
		for sentence in text:
			words = re.split(delimiters,sentence)
			tokenizedText.append(words)

		#Fill in code here

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		for sentence in text:
			words =  nltk.tokenize.treebank.TreebankWordTokenizer().tokenize(sentence)
			tokenizedText.append(words)
		#Fill in code here

		return tokenizedText

tester = ["simple shear flow past a flat plate in an* incompressible fluid, of small: viscosity","hello hi how"] #the study of high-speed viscous flow past a two-dimensional body it is usually necessary to consider a curved shock wave emitting from the nose or leading edge of the body .  consequently, there exists an inviscid rotational flow region between the shock wave and the boundary layer .  such a situation arises, for instance, in the study of the hypersonic viscous flow past a flat plate .  the situation is somewhat different from prandtl's classical boundary-layer problem . in prandtl's original problem the inviscid free stream outside the boundary layer is irrotational while in a hypersonic boundary-layer problem the inviscid free stream must be considered as rotational .  the possible effects of vorticity have been recently discussed by ferri and libby .  in the present paper, the simple shear flow past a flat plate in a fluid of small viscosity is investigated .  it can be shown that this problem can again be treated by the boundary-layer approximation, the only novel feature being that the free stream has a constant vorticity .  the discussion here is restricted to two-dimensional incompressible steady flow ."
a = Tokenization()
b = a.pennTreeBank(tester)
print(b)