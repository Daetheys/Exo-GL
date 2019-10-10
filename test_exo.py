import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists
from exo import parti,sort,IncorrectType

def verify_correctness(l,v,i,j):
	#Check if l,i,j verifies the property 
	for a in range(i):
		assert l[a] < v
	for a in range(i,j):
		assert l[a] == v
	for a in range(j,len(l)):
		assert l[a] > v
	return True
	
def verify_sort(l):
	for i in range(len(l)-1):
		assert l[i] <= l[i+1]
#Tests
		
def test_rotten_green_test():
	#Just to check if the module works correctly
	pass

@given(lists(elements=integers()),integers())
def test_random_parti(l,v):
	#Random test using hypothesis
	l2,i,j = parti(l,v)
	assert verify_correctness(l2,v,i,j)
	
@given(lists(elements=integers()))
def test_random_sort(l):
	#Test the sort function
	verify_sort(sort(l))
	
def test_not_nice_parti():
	l = [4521,None,631,None,None,468321]
	try:
		parti(l,5)
		assert False
	except IncorrectType:
		pass
	
	l = [1424,12324,12348,6845]
	try:
		parti(l,None)
		assert False
	except IncorrectType:
		pass

	try:
		parti(None,None)
		assert False
	except IncorrectType:
		pass
	
def test_not_nice_sort():
	l = [None,4152,1474,12,41,6,5112,4,55,21,3,2,465]
	try:
		sort(l)
		assert False
	except IncorrectType:
		pass
	
	try:
		sort(None)
		assert False
	except IncorrectType:
		pass
	