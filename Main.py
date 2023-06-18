import csv
import numpy as np
import itertools

def Candidate_Elimination(X):
	Sample = ['']*(len(X[0])-1)
	Geo,Geom = [],[]
	for i in range(len(X)):
		delete_Geo = []
		if X[i][-1] == "Yes":
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

		if X[i][-1] == "No":
			# Geo_list = []
			for j in range(len(X[i])-1):
				if X[i][j] != Sample[j] and Sample[j] != "?": 
					Geo_list = ['?']*j
					Geo_list.append(Sample[j])
					while len(Geo_list) < len(Sample):
						Geo_list.append("?")
					Geo.append(Geo_list)
	return Geom,Sample

def Find_S(data_X,S):
	for i in range(len(data_X)-1) :
		if data_X[i] == S[i] or S[i] == '':
			S[i] = data_X[i] 
		if data_X[i] != S[i] and S[i] != '':
			S[i] = '?' 

X = []
with open('data/data5.csv') as fileR :
	data = csv.reader(fileR)
	for i in data :
		del i[0]
		X.append(i)
Head = X[0]
del X[0]
S = ['']*(len(X[0])-1)
for data_X in X:
	if data_X[-1] == "Yes":
		Find_S(data_X,S)
# print(X) #++++++++++++++++++++++++++++++
print("Hypothesis Find-S ->",[S]) #+++++++++++++++++++++

#----------------------->

Hd = np.array(X)
n = Hd.shape[1]
a,count_Hypo = [],1
point = 1
# print(Hd)
for i in range(n):
	a.append(sorted(list(set(Hd[:,i]))))
# print(a)

Hypo_all = list(itertools.product(*a))
# print("\nHypothesis all") #++++++++++++++++++++++++++++
for i in range(len(Hypo_all)) :
	Hypo_all_sort = list(Hypo_all[i])
	per = ""
	answer = Hypo_all_sort[-1]
	del Hypo_all_sort[-1]
	array_X = np.array(X)
	answer_X = list(array_X[:,-1])
	# print(answer_X)
	array_X = np.delete(array_X,len(X[0])-1,axis = 1).tolist()
	# print(array_X)
	for j in range(len(array_X)):
		if Hypo_all_sort == array_X[j] :
			if answer != answer_X[j] : per = "continue"
	if per == "continue" : continue
	# print(count_Hypo,Hypo_all_sort,answer) #++++++++++++++++++++++++++++++
	count_Hypo += 1

def Candidate_Elimination_V2(X,a):
	Sample = ['']*(len(X[0])-1)
	Geo,Geom = [],[]
	print(a)
	for i in range(len(X)):
		delete_Geo = []
		if X[i][-1] == "Yes":
			for j in range(len(Geo)):
				for GeoFor in range(len(Geo[j])):
					for XFor in range(len(X[i])):
						if Geo[j][GeoFor] != '?':
							if X[i][XFor] != Geo[j][GeoFor] and XFor == GeoFor:
								delete_Geo.append(j)
								# print(j)
			count_delete = 0
			for delete in list(set(delete_Geo)):
				del Geo[delete-count_delete]
				count_delete += 1

		if X[i][-1] == "No":
			if len(Geo) >= 1 :
				Gro_store,GeoF = [],[]
				for j in range(len(Geo)):
					B_count = "None"
					for k in range(len(Geo[j])):
						if Geo[j][k] != "?":
							for num in range(len(X[i])-1):
								if num == k and Geo[j][k] == X[i][num]:
									for num2 in range(len(X[i])-1):
										if num2 == num :
											continue
										for result in range(len(a[num2])-1):
											if X[i][num2] != a[num2][result] and B_count == "None":
												for lis in Geo[j] :
													GeoF.append(lis)
												GeoF[num2] = a[num2][result]
												Gro_store.append(GeoF)
												delete_Geo.append(j)
												GeoF = []
				delete_Geo = list(set(delete_Geo))
				count_delete = 0
				for delete in delete_Geo:
					del Geo[delete-count_delete]
					# print(Geo)
					count_delete += 1
				for dem in Gro_store:
					Geo.append(dem)




			else :
				for j in range(len(X[i])-1):
					if X[i][j] != Sample[j] and Sample[j] != "?":
						for k in range(len(a[j])):
							Geo_list = ['?']*j
							if a[j][k-1] != X[i][j]:
								Geo_list.append(a[j][k-1])
								while len(Geo_list) < len(Sample):
									Geo_list.append("?")
								Geo.append(Geo_list)
		print(i+1,Geo)           # Step
	return Geo
Geo = Candidate_Elimination_V2(X,a)
product_Geo = itertools.product(Geo,S)
list_product_Go = []
product = []

#----------------------------------------------------------------------------------------------------------
# for i in product_Geo:
# 	product_Geo_1,product_Geo_2 = ''.join(i[0]).replace('?',''),i[1]
# 	if product_Geo_2 != '?':
# 		if sorted([product_Geo_1,product_Geo_2]) not in list_product_Go or list_product_Go == None:
# 			list_product_Go.append([product_Geo_1,product_Geo_2])
# for j in range(len(list_product_Go)) :
# 	list_product = ['?']*(len(X[0])-1)
# 	for k in range(2):
# 		for i in range(len(S)):
# 			if S[i] == list_product_Go[j][k]: 
# 				list_product[i] = list_product_Go[j][k]
# 	product.append(list_product)
#----------------------------------------------------------------------------------------------------------

if Geo != [S] :
	product.append(S)
	for i in Geo:
		product.append(i)

if Geo == [S] : product = Geo

print(product)

# inp = ['Round','Triangle','Round','Purple','Yes']
# score = 0

# for i in range(len(inp)):
# 	for j in range(len(product)) :
# 		if inp[i] == product[j][i] : 
# 			score += 1
# print(score)