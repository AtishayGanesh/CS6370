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
                    if(word in rev_index):
                        if(docIDs[doc_counter] in rev_index[word]):
                            rev_index[word][docIDs[doc_counter]] += 1
                        else:
                            rev_index[word][docIDs[doc_counter]] = 1
                    else:
                        rev_index[word] = {}
                        rev_index[word][docIDs[doc_counter]] = 1    

                    if(docIDs[doc_counter] in index):
                        if(word in index[docIDs[doc_counter]]):
                            index[docIDs[doc_counter]][word] += 1
                        else:
                            index[docIDs[doc_counter]][word] = 1
                    else:
                        index[docIDs[doc_counter]] = {}
                        index[docIDs[doc_counter]][word] = 1
            doc_counter += 1
        #Fill in code here

        self.index = index
        self.N = len(docIDs)
        self.rev_index = rev_index
        # self.docs = docs
        # self.docIDs = docIDs


    def rank(self, queries,n_components):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query
        arg2 : int
            An integer which denotes number of singular values to be 
            considered

        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """
        print('started rank')
        index = self.index
        N = self.N
        rev_index = self.rev_index
        doc_IDs_ordered = []
        doc_mags = {}
        doc_mag_list = []
        wordIDF = {}
        print('started wordIDF')
        for word in rev_index:
            wordIDF[word] = np.log((self.N+0.5)/(len(rev_index[word])+0.5))
        for docID in index:
            curr_doc_mag = 0.0
            for word in index[docID]:
                curr_doc_mag += (index[docID][word]*wordIDF[word])**2
            doc_mags[docID] = np.sqrt(curr_doc_mag) + 0.01
            doc_mag_list.append(np.sqrt(curr_doc_mag) + 0.01)

        list_words = list(rev_index.keys())
        list_docs = list(index.keys())
        word_locs = dict(zip(list_words,(list(range(len(list_words))))))
        tfidf_matrix =[]
        print('started tfidf_matrix')
        for i in index.keys():
            tfidf_row = np.zeros(len(list_words))
            total_len = 0 
            for word in index[i]:
                word_location =word_locs[word]
                tfidf_row[word_location] = index[i][word]*wordIDF[word]
                total_len +=index[i][word]
            #tfidf_row /= total_len
            tfidf_matrix.append(tfidf_row)
        tfidf_matrix = np.array(tfidf_matrix)
        print('started SVD')
        svd = TruncatedSVD(n_components=n_components,n_iter=10,random_state=420)
        svd.fit(tfidf_matrix)
        tfidf_smallened = svd.transform(tfidf_matrix)
        print(svd.singular_values_)

        
        ct = 0
        print('started qrel')
        for query in queries:
            query_vector={}
            for sentence in query:
                for word in sentence:
                    if(word in query_vector):
                        query_vector[word] += 1
                    else:
                        query_vector[word] = 1
            query_mag = 0.0
            query_row =np.zeros(len(list_words))
            q_len =0

            for word in query_vector:
                try:

                    if(word in wordIDF):
                        query_mag += (query_vector[word]*wordIDF[word])**2
                        query_row[word_locs[word]] = query_vector[word]*wordIDF[word]
                        q_len +=query_vector[word]
                    else:
                        query_mag += (query_vector[word]*np.log((self.N+0.5)/(0.5)))**2
                except:
                    print(len(wordIDF),len(word_locs))

            query_mag = np.sqrt(query_mag) + 0.01
            query_row/=(query_mag)

            query_smaller = svd.transform(query_row.reshape(1,-1))[0]

            cos_sim = (tfidf_smallened@query_smaller.T)/np.array(doc_mag_list)

            query_doc_sim = list(zip(cos_sim,list_docs))
            # query_doc_sim2 = []  
            # for docID in index:
            #     cos_sim2 = 0.0
            #     for word in query_vector:
            #         if(word in index[docID]):

            #             cos_sim2 +=  (query_vector[word]*index[docID][word]*(wordIDF[word]**2))
            #     cos_sim2 /= (query_mag*doc_mags[docID])
            #     query_doc_sim2.append([cos_sim2, docID])
            curr_doc_IDs_ordered = []
            qds = query_doc_sim[0:1399]
            qds.sort(reverse=True)

            for ranking in qds:
                curr_doc_IDs_ordered.append(ranking[1])
            doc_IDs_ordered.append(curr_doc_IDs_ordered)
        return doc_IDs_ordered


if __name__ == '__main__':
    
    docs = [[["dog", "animal"], ["cat", "animal"]],[["crow", "bird"], ["cat", "animal"]]]
    docIDs = [110,111]
    queries = [[["is", "dog", "animal"], ["cat"]], [["is", "crow", "bird"], ["cat"]]]
    a = InformationRetrieval()
    b = a.buildIndex(docs, docIDs)
    c = a.rank(queries)
    print(c)