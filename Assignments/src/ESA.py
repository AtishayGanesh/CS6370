# from util import *

# Add your import statements here
import numpy as np


class InformationRetrievalESA():

	# def __init__(self):
		# self.index = None
		# self.N = None
		# self.rev_index = None

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
		return index, rev_index, len(docIDs)
		# self.index = index
		# self.N = len(docIDs)
		# self.rev_index = rev_index
		# self.docs = docs
		# self.docIDs = docIDs


	def rank(self, queries, doc_index, doc_rev_index, doc_N, wiki_index, wiki_rev_index, wiki_N):
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
		# index = self.index
		# N = self.N
		# rev_index = self.rev_index
		doc_IDs_ordered = []
		doc_mags = {}
		doc_wordIDF = {}
		wiki_wordIDF = {}
		for word in doc_rev_index:
			doc_wordIDF[word] = np.log((doc_N+0.5)/(len(doc_rev_index[word])+0.5))

		for word in wiki_rev_index:
			wiki_wordIDF[word] = np.log((wiki_N+0.5)/(len(wiki_rev_index[word])+0.5))

		index = {}
		for docID in doc_index:
			for word in doc_index[docID]:
				if(word in wiki_rev_index):
					for concID in wiki_rev_index[word]:
						if(docID in index):
							if(concID in index[docID]):
								index[docID][concID] += doc_wordIDF[word]*doc_index[docID][word]*wiki_wordIDF[word]*wiki_rev_index[word][concID]
							else:
								index[docID][concID] = doc_wordIDF[word]*doc_index[docID][word]*wiki_wordIDF[word]*wiki_rev_index[word][concID]
						else:
							index[docID] = {}
							index[docID][concID] = doc_wordIDF[word]*doc_index[docID][word]*wiki_wordIDF[word]*wiki_rev_index[word][concID]

		for docID in index:
			curr_doc_mag = 0.0
			for conc in index[docID]:
				curr_doc_mag += (index[docID][conc])**2
			doc_mags[docID] = np.sqrt(curr_doc_mag) + 0.01

		for query in queries:
			query_vector_word={}
			for sentence in query:
				for word in sentence:
					if(word in query_vector_word):
						query_vector_word[word] += 1
					else:
						query_vector_word[word] = 1
			query_vector={}
			for word in query_vector_word:
				if(word in wiki_rev_index):
					for concID in wiki_rev_index[word]:
						if(not(word in doc_wordIDF)):
							doc_wordIDF[word] = np.log((doc_N+0.5)/(0.5))
						if(concID in query_vector):
							query_vector[concID] += doc_wordIDF[word]*query_vector_word[word]*wiki_wordIDF[word]*wiki_rev_index[word][concID]
						else:
							query_vector[concID] = doc_wordIDF[word]*query_vector_word[word]*wiki_wordIDF[word]*wiki_rev_index[word][concID]
			query_doc_sim = []
			query_mag = 0.0
			for conc in query_vector:
				query_mag += (query_vector[conc])**2
			query_mag = np.sqrt(query_mag) + 0.01
			for docID in index:
				cos_sim = 0.0
				for conc in query_vector:
					if(conc in index[docID]):
						cos_sim +=  (query_vector[conc]*index[docID][conc])
				cos_sim /= (query_mag*doc_mags[docID])
				query_doc_sim.append([cos_sim, docID])
			curr_doc_IDs_ordered = []
			query_doc_sim.sort(reverse = True)
			for ranking in query_doc_sim:
				curr_doc_IDs_ordered.append(ranking[1])
			doc_IDs_ordered.append(curr_doc_IDs_ordered)

		return doc_IDs_ordered


if __name__ == '__main__':
	
	docs = [[["dog", "animal"], ["cat", "animal"]],[["crow", "bird"], ["cat", "animal"]]]
	docIDs = [110,111]
	wiki_docs = [[["wikidog", "wikianimal"], ["wikicat", "wikianimal"]],[["crow", "bird"], ["cat", "animal"]]]
	wiki_docIDs = [0,1]
	queries = [[["is", "dog", "animal"], ["cat"]], [["is", "crow", "bird"], ["cat"]]]
	a = InformationRetrievalESA()
	doc_index, doc_rev_index, doc_N = a.buildIndex(docs, docIDs)
	wiki_index, wiki_rev_index, wiki_N = a.buildIndex(wiki_docs, wiki_docIDs)
	c = a.rank(queries, doc_index, doc_rev_index, doc_N, wiki_index, wiki_rev_index, wiki_N)
	print(c)