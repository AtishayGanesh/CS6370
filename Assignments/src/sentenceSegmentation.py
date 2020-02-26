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

if __name__=="__main__":
    a = SentenceSegmentation()
    #t =  "It was o. reynolds who first expressed the so-called apparent or turbulent stresses by the mean values of the products of the velocity components."
    #t = "a free-flight investigation of ablation of a blunt body to a mach number of 13 .1.   a five-stage rocket-propelled research-vehicle system was flown to a maximum mach number of 13.1 at an altitude of approximately 78,000 feet to determine ablation characteristics of teflon in free flight ."
    t = "the blade designed by o. ram had length in cm of 1. his contributions to science were amazing."
    b = a.punkt(t)
    print(b)
    b = a.naive(t)
    print(b)