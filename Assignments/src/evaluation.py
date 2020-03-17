from util import *

# Add your import statements here




class Evaluation():

    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The precision value as a number between 0 and 1
        """
        pred_k = set(query_doc_IDs_ordered[0:k])
        true_k = set(true_doc_IDs)



        precision = len(pred_k&true_k)/len(pred_k)
        return precision


    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        doc_IDs_ordered : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        query_ids : list
            A list of IDs of the queries for which the documents are ordered
        qrels : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean precision value as a number between 0 and 1
        """

        dict_sorted_queries = dict(
            zip(query_ids, [[[],[],[],[]] for i in doc_IDs_ordered]))
        for elt in qrels:

            q,p,i = elt['query_num'],elt['position'],elt['id']

            if q in query_ids:
                dict_sorted_queries[q][p-1].append(i)

        for key in dict_sorted_queries.keys():
            val = dict_sorted_queries[key]
            dict_sorted_queries[key] = val[0]+val[1]+val[2]+val[3]



        sum_precisions = 0
        for i,query in enumerate(query_ids):
            sum_precisions+= self.queryPrecision(
                doc_IDs_ordered[i],query,dict_sorted_queries[query],k)



        meanPrecision = sum_precisions/len(query_ids)

        #Fill in code here

        return meanPrecision

    
    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The recall value as a number between 0 and 1
        """

        recall = -1

        pred_k = set(query_doc_IDs_ordered[0:k])
        true_k = set(true_doc_IDs)



        recall = len(pred_k&true_k)/len(true_k)

        return recall


    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean recall value as a number between 0 and 1
        """
        dict_sorted_queries = dict(
            zip(query_ids, [[[],[],[],[]] for i in doc_IDs_ordered]))
        for elt in qrels:

            q,p,i = elt['query_num'],elt['position'],elt['id']

            if q in query_ids:
                dict_sorted_queries[q][p-1].append(i)

        for key in dict_sorted_queries.keys():
            val = dict_sorted_queries[key]
            dict_sorted_queries[key] = val[0]+val[1]+val[2]+val[3]



        sum_recalls = 0
        for i,query in enumerate(query_ids):
            sum_recalls+= self.queryRecall(
                doc_IDs_ordered[i],query,dict_sorted_queries[query],k)



        meanRecall= sum_recalls/len(query_ids)

        #Fill in code here

        return meanRecall


    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The fscore value as a number between 0 and 1
        """
        p = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        r = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        if p == 0 or r == 0:
            return 0

        fscore = 2*p*r/(p+r)

        #Fill in code here


        return fscore


    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value
        
        Returns
        -------
        float
            The mean fscore value as a number between 0 and 1
        """

        dict_sorted_queries = dict(
            zip(query_ids, [[[],[],[],[]] for i in doc_IDs_ordered]))
        for elt in qrels:

            q,p,i = elt['query_num'],elt['position'],elt['id']

            if q in query_ids:
                dict_sorted_queries[q][p-1].append(i)

        for key in dict_sorted_queries.keys():
            val = dict_sorted_queries[key]
            dict_sorted_queries[key] = val[0]+val[1]+val[2]+val[3]



        sum_fscore = 0
        for i,query in enumerate(query_ids):
            sum_fscore+= self.queryFscore(
                doc_IDs_ordered[i],query,dict_sorted_queries[query],k)



        meanFscore= sum_fscore/len(query_ids)

        #Fill in code here

        return meanFscore
    

    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The nDCG value as a number between 0 and 1
        We further penalize for missing right documents 
        and also for fetching bad documents
        """

        pred_k  = query_doc_IDs_ordered
        true_scores = []
        cts = [0]*len(true_doc_IDs)
        for elt in pred_k:
            if elt in true_doc_IDs[0]:
                pred_score = 3
                cts[0]+=1
            elif elt in true_doc_IDs[1]:
                pred_score = 2
                cts[1]+=1

            elif elt in true_doc_IDs[2]:
                pred_score = 1
                cts[2]+=1

            elif elt in true_doc_IDs[3]:
                pred_score = 0
                cts[3]+=1

            else:
                pred_score = -1
            true_scores.append(pred_score)
        true_scores = [true_scores]

        pred_scores = [list(np.arange(len(true_scores[0]),0,-1))]

        #penalizing misses now
        total_rel= np.array([len(i) for i in true_doc_IDs])

        missed = total_rel -np.array(cts)
        true_scores[0] += list(np.concatenate([ (3-i)*np.ones(missed[i]) for i in range(4)]))
        pred_scores[0]+=[0]*np.sum(missed)


        nDCG = sklearn.metrics.ndcg_score(true_scores,pred_scores,k)

        return nDCG

    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean nDCG value as a number between 0 and 1
        """
        dict_sorted_queries = dict(
            zip(query_ids, [[[],[],[],[]] for i in doc_IDs_ordered]))
        for elt in qrels:

            q,p,i = elt['query_num'],elt['position'],elt['id']

            if q in query_ids:
                dict_sorted_queries[q][p-1].append(i)



        sumNDCG = 0
        for i,query in enumerate(query_ids):
            sumNDCG+= self.queryNDCG(
                doc_IDs_ordered[i],query,dict_sorted_queries[query],k)



        meanNDCG= sumNDCG/len(query_ids)


        return meanNDCG



    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The average precision value as a number between 0 and 1
        """
        sum_prec = 0
        prev_rec = 0
        for i in range(1,k+1):
            rec = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs,i)
            sum_prec += self.queryPrecision(
                query_doc_IDs_ordered, query_id, true_doc_IDs,i)*(rec-prev_rec)
            prev_rec = rec

        avgPrecision = sum_prec

        #Fill in code here

        return avgPrecision


    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The MAP value as a number between 0 and 1
        """

        dict_sorted_queries = dict(
            zip(query_ids, [[[],[],[],[]] for i in doc_IDs_ordered]))
        for elt in qrels:

            q,p,i = elt['query_num'],elt['position'],elt['id']

            if q in query_ids:
                dict_sorted_queries[q][p-1].append(i)

        for key in dict_sorted_queries.keys():
            val = dict_sorted_queries[key]
            dict_sorted_queries[key] = val[0]+val[1]+val[2]+val[3]



        sumAvgPrecision = 0
        for i,query in enumerate(query_ids):
            sumAvgPrecision+= self.queryAveragePrecision(
                doc_IDs_ordered[i],query,dict_sorted_queries[query],k)



        meanAveragePrecision= sumAvgPrecision/len(query_ids)


        return meanAveragePrecision

if __name__ == '__main__':
    
    a = Evaluation()
    l =[{"query_num": "7", "position": 2, "id": "20"},
    {"query_num": "7", "position": 3, "id": "56"},
    {"query_num": "7", "position": 3, "id": "57"},
    {"query_num": "7", "position": 3, "id": "58"},
    {"query_num": "7", "position": 4, "id": "19"},
    {"query_num": "7", "position": 1, "id": "492"},
    {"query_num": "8", "position": 1, "id": "48"},
    {"query_num": "8", "position": 1, "id": "122"},
    {"query_num": "8", "position": 3, "id": "20"},
    {"query_num": "8", "position": 3, "id": "58"},
    {"query_num": "8", "position": 3, "id": "196"},
    {"query_num": "8", "position": 1, "id": "354"},
    {"query_num": "8", "position": 1, "id": "360"},
    {"query_num": "8", "position": 3, "id": "197"},
    {"query_num": "8", "position": 3, "id": "999"},
    {"query_num": "8", "position": 3, "id": "1112"},
    {"query_num": "8", "position": 1, "id": "1005"},
    {"query_num": "8", "position": 1, "id": "492"},
    {"query_num": "9", "position": 2, "id": "21"},
    {"query_num": "9", "position": 2, "id": "22"},
    {"query_num": "9", "position": 2, "id": "550"},
    {"query_num": "9", "position": 1, "id": "534"}]
    doc_IDs_ordered, query_ids, qrels,k = ([['492','20','35','57','56','59','58','19'],
        ['1','3','2','5','6'],['534','21','22','550','675']], ['7','8','9'],l,5)
    print(a.meanPrecision(doc_IDs_ordered, query_ids, qrels,k))
    print(a.meanRecall(doc_IDs_ordered, query_ids, qrels,k))
    print(a.meanFscore(doc_IDs_ordered, query_ids, qrels,k))
    print(a.meanAveragePrecision(doc_IDs_ordered, query_ids, qrels,k))
    print(a.meanNDCG(doc_IDs_ordered, query_ids, qrels,k))


