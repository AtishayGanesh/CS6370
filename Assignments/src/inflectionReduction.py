from util import *

# Add your import statements here
from time import time



class InflectionReduction:
    def __init__(self):
        self.stemmer = nltk.stem.porter.PorterStemmer()
        self.characters = './\\\'\",!@#$%%^&*()\{\}'
    def reduce(self, text):
        """
        Stemming/Lemmatization

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            stemmed/lemmatized tokens representing a sentence
        """

        reducedText = []
        #Fill in code here
        for sentence in text:
            reducedSentence =[]
            for word in sentence:
                strippedWord = word.strip(self.characters)
                if word:
                    reducedSentence.append(self.lemmatizer.stem(strippedWord))
            reducedText.append(reducedSentence)



        return reducedText
