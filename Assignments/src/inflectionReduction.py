from util import *

# Add your import statements here




class InflectionReduction:
    def __init__(self):
        self.lemmatizer = nltk.stem.WordNetLemmatizer()
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
        print(self.lemmatizer.lemmatize('corpora'))
        #raise AssertionError
        #Fill in code here
        for sentence in text:
            reducedSentence = [self.lemmatizer.lemmatize(word)
             for word in sentence]
            reducedText.append(reducedSentence)



        return reducedText
if __name__=="__main__":
    a = InflectionReduction()
    b = [['my','names','are','corpora'],['her','women','eating','analysis','leaves','operations'],['to','being','desirable']]
    print(a.reduce(b))