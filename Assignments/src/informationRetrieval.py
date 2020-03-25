from util import *

# Add your import statements here



class InformationRetrieval():

    def __init__(self):
        self.index = None
        self.N = None
        self.rev_index = None

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """
        index = {}
        rev_index = {}
        doc_counter = 0
        for document in docs:
            for sentence in document:
                for word in sentence:
                    if(word in index):
                        if(docIDs[doc_counter] in index[word]):
                        	index[word][docIDs[doc_counter]] += 1
                        else:
                        	index[word][docIDs[doc_counter]] = 1
                    else:
                    	index[word] = {}
                    	index[word][docIDs[doc_counter]] = 1	

                    if(docIDs[doc_counter] in rev_index):
	                    if(word in rev_index[docIDs[doc_counter]]):
	                    	rev_index[docIDs[doc_counter]][word] += 1
	                    else:
	                    	rev_index[docIDs[doc_counter]][word] = 1
                    else:
	                    rev_index[docIDs[doc_counter]] = {}
	                    rev_index[docIDs[doc_counter]][word] = 1
            doc_counter += 1
        #Fill in code here

        self.index = index
        self.N = len(docIDs)
        self.rev_index = rev_index
        # self.docs = docs
        # self.docIDs = docIDs


    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query
        

        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """
        index = self.index
        N = self.N
        rev_index = self.rev_index
        doc_IDs_ordered = []
        doc_mags = {}
        wordIDF = {}
        for word in index:
        	wordIDF[word] = np.log((self.N+0.5)/(len(index[word])+0.5))
        for docID in rev_index:
        	curr_doc_mag = 0.0
        	for word in rev_index[docID]:
        		curr_doc_mag += (rev_index[docID][word]*wordIDF[word])**2
        	doc_mags[docID] = np.sqrt(curr_doc_mag) + 0.01
        for query in queries:
        	query_vector={}
        	for sentence in query:
        		for word in sentence:
        			if(word in query_vector):
        				query_vector[word] += 1
        			else:
        				query_vector[word] = 1
        	query_doc_sim = []
        	query_mag = 0.0
        	for word in query_vector:
        		if(word in wordIDF):
        			query_mag += (query_vector[word]*wordIDF[word])**2
        		else:
        			wordIDF[word] = np.log((self.N+0.5)/(0.5))
        			query_mag += (query_vector[word]*wordIDF[word])**2
        	query_mag = np.sqrt(query_mag) + 0.01
        	for docID in rev_index:
        		cos_sim = 0.0
        		for word in query_vector:
        			if(word in rev_index[docID]):
        				cos_sim +=  (query_vector[word]*rev_index[docID][word]*(wordIDF[word]**2))
        		cos_sim /= (query_mag*doc_mags[docID])
        		query_doc_sim.append([cos_sim, docID])
        	curr_doc_IDs_ordered = []
        	query_doc_sim.sort(reverse = True)
        	for ranking in query_doc_sim:
        		curr_doc_IDs_ordered.append(ranking[1])
        	doc_IDs_ordered.append(curr_doc_IDs_ordered)

        #Fill in code here
    
        return doc_IDs_ordered


if __name__ == '__main__':
    
    docs = [[["dog", "animal"], ["cat", "animal"]],[["crow", "bird"], ["cat", "animal"]]]
    docIDs = [110,111]
    queries = [[["is", "dog", "animal"], ["cat"]], [["is", "crow", "bird"], ["cat"]]]
    a = InformationRetrieval()
    b = a.buildIndex(docs, docIDs)
    c = a.rank(queries)
    print(c)