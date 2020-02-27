from util import *

# Add your import statements here



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
        for sentence in text:
            reducedSentence =[]
            for word in sentence:
                strippedWord = word.strip(self.characters)
                if strippedWord !='':
                    reducedSentence.append(self.stemmer.stem(strippedWord))
            reducedText.append(reducedSentence)



        return reducedText
