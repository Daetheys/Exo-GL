class IncorrectType(Exception):
	pass
	
def parti(l,v):
	#Return a liste l2 and 2 integers i and j such as for all 
	#a in l[0:i], a<v, 
	#a in l[i:j], a=v, 
	#a in l[j:],  a>v
	print(type(l),type(v))
	if not(isinstance(l,list)) or not(isinstance(v,int)) and not(isinstance(v,long)):
		raise IncorrectType #C'est pas gentil de tester un mauvais type
	liv = []
	nbev = 0
	lsv = []
	for i in l:
		if i is None:
			raise IncorrectType #C'est pas gentil de donner une liste dont les nombres sont du mauvais type
		if i < v:
			liv.append(i)
		elif i ==v :
			nbev += 1
		else:
			assert i > v
			lsv.append(i)
	return liv+([v]*nbev)+lsv,len(liv),len(liv)+nbev
	
def sort(l):
	if not(isinstance(l,list)):
		raise IncorrectType #C'est pas gentil de tester un mauvais type
	if len(l) <= 1:
		return l
	v = l[0]
	l2,i,j = parti(l,v)
	ls1 = sort(l2[0:i])
	ls2 = sort(l2[j:])
	return ls1 + l2[i:j] + ls2
	