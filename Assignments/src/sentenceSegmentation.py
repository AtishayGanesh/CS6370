from util import *

# Add your import statements here




class SentenceSegmentation():

    def naive(self, text):
        """
        Sentence Segmentation using a Naive Approach

        Parameters
        ----------
        arg1 : str
            A string (a bunch of sentences)

        Returns
        -------
        list
            A list of strings where each string is a single sentence
        """
        self.sentenceDelimiters = "[.?!#][/\s]|.\""
        segmentedText = re.split(self.sentenceDelimiters,text)
        return segmentedText





    def punkt(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : str
            A string (a bunch of sentences)

        Returns
        -------
        list
            A list of strings where each string. New is a single sentence
        """
        self.tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
        segmentedText = self.tokenizer.tokenize(text)

        return segmentedText
