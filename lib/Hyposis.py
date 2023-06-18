import csv
import numpy as np
import itertools

class Hypo():
	def Create(self,title = "__Hypothesis__",content = ['Head 1','Head 2','Head 3'],solution = "Result") :
		filename = title+'.csv'
		HeadHypo = ['Sample.']
		HeadHypo += content
		HeadHypo += [solution]
		# print(Head Hypo)
		with open(filename,'w') as csvfile :
			write = csv.writer(csvfile)
			write.writerow(HeadHypo)

	def Format(self,file):
		X = []
		with open(file) as fileR :
			data = csv.reader(fileR)
			for i in data :
				del i[0]
				X.append(i)
		Head = X[0]
		del X[0]
		return X

	def FindS(self,data,Correct):
		S = ['']*(len(data[0])-1)
		for data_X in data:
			if data_X[-1] == Correct:
				for i in range(len(data_X)-1) :
					if data_X[i] == S[i] or S[i] == '':
						S[i] = data_X[i] 
					if data_X[i] != S[i] and S[i] != '':
						S[i] = '?' 
		return [S]

	def HypoAll(self,data):
		global a
		Hd = np.array(data)
		n = Hd.shape[1]
		a,count_Hypo = [],1 
		point = 1
		# print(Hd)
		for i in range(n):
			a.append(sorted(list(set(Hd[:,i]))))
		# print(a)

		Hypo_all = list(itertools.product(*a))
		print("\nHypothesis all")
		for i in range(len(Hypo_all)) :
			Hypo_all_sort = list(Hypo_all[i])
			per = ""
			answer = Hypo_all_sort[-1]
			del Hypo_all_sort[-1]
			array_X = np.array(data)
			answer_X = list(array_X[:,-1])
			# print(answer_X)
			array_X = np.delete(array_X,len(data[0])-1,axis = 1).tolist()
			# print(array_X)
			for j in range(len(array_X)):
				if Hypo_all_sort == array_X[j] :
					if answer != answer_X[j] : per = "continue"
			if per == "continue" : continue
			print(count_Hypo,Hypo_all_sort,answer)
			count_Hypo += 1

	def Elimination(self,data,Correct = "Yes"):
		def Candidate_Elimination(X):
			Sample = ['']*(len(X[0])-1)
			Geo,Geom = [],[]
			for i in range(len(X)):
				delete_Geo = []
				if X[i][-1] == Correct:
					for j in range(len(X[i])-1):
						if X[i][j] == Sample[j] or Sample[j] == '':
							Sample[j] = X[i][j]
						if X[i][j] != Sample[j] and Sample[j] != '':
							Sample[j] = '?'
						for k in range(len(Geo)):
							for l in range(len(Geo[k])):
								if X[i][j] == Geo[k][l] and Geo[k][l] != "?" :
									delete_Geo.append(k)
									Geom.append(Geo[k])

				else :
					# Geo_list = []
					for j in range(len(X[i])-1):
						if X[i][j] != Sample[j] and Sample[j] != "?": 
							Geo_list = ['?']*j
							Geo_list.append(Sample[j])
							while len(Geo_list) < len(Sample):
								Geo_list.append("?")
							Geo.append(Geo_list)

			return Geom,Sample

		global list_product_Go
		Geo,Sample = Candidate_Elimination(data)
		product_Geo = itertools.product(Geo,Sample)
		list_product_Go = []
		product = []

		for i in product_Geo:
			product_Geo_1,product_Geo_2 = ''.join(i[0]).replace('?',''),i[1]
			if product_Geo_1 != product_Geo_2 and product_Geo_2 != '?':
				if sorted([product_Geo_1,product_Geo_2]) not in list_product_Go or list_product_Go == None:
					list_product_Go.append([product_Geo_1,product_Geo_2])
		for j in range(len(list_product_Go)) :
			list_product = ['?']*(len(data[0])-1)
			for k in range(2):
				for i in range(len(Sample)):
					if Sample[i] == list_product_Go[j][k]:
						list_product[i] = list_product_Go[j][k]
			product.append(list_product)

		return product

	def Score(self,inp,product = [['?']]):
		score = 0
		for i in range(len(inp)):
			for j in range(len(product)) :
				if inp[i] == product[j][i] : 
					score += 1

		part = "UNSURE"
		if len(product) == 1:
			if score == len(product[0]) : part = "ACCEPT"
			else : part = "REJECT"
			return score,part

		if score > len(product) : part = "ACCEPT"
		if score < len(product) : part = "REJECT"
		return score,part	


if __name__  == "__main__" :
	print("Lib Save")