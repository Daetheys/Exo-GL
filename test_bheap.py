import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists
from bheap import BinHeap
import random

#On va tester chaque methode au fur et a mesure

def test_rotten_green_test():
    #Just to check if the module works correctly
    pass

#Petits tests en boite noire (on verifie juste que le code fait bien son travail de tas, on s'en fiche de percUp percDown)

def test_insert1():
    B = BinHeap()
    B.insert(3)
    assert B.delMin() == 3

def test_insert2(): #1 -> Boucle infinie dans percUp
    B1 = BinHeap()
    for k in range(50):
	B1.insert(k)
    for k in range(50):
	vmin = B1.delMin()
	assert vmin == k
        
def test_build_list():
    l = [2,4,5,1,23,4,5,7,8,9,14,5,4,12]
    B = BinHeap()
    B.buildHeap(l)
    l.sort()
    print(l)
    l2 = []
    for i in range(len(l)):
        l2.append(B.delMin())
	#assert B.delMin() == l[i]
    print(l2)
		
#Tests plus precis sur la structure de donnees pour verifier que tout est en ordre pour les plus gros tests qui suivent
		
def test_init():
    B = BinHeap()
    assert B.heapList == [0]
    assert B.currentSize == 1

#Test fondamental : test si le tas fait bien ce qu'on lui demande de faire
@given(lists(elements=integers()))
def test_fonda(l):
    B = BinHeap()
    B.buildHeap(l)
    last_v = None
    print(B.heapList)
    while B.currentSize > 1:
        v = B.delMin()
        print(last_v,v)
        assert last_v == None or last_v <= v
        last_v = v
        
@given(lists(elements=lists(elements=integers())))
def test_fonda2(ll): #Ajoute et enleve des elements à la suite au hazard
    B = BinHeap()
    lmin = []
    count = 0
    for l in ll:
        for e in l:
            B.insert(e)
        count += len(l)
        lmin += l
        lmin.sort()
        if random.random() > 0.5:
            for i in range(count):
                count -= 1
                v = B.delMin()
                assert v == lmin[0]
                del lmin[0]
    for i in range(count):
        count -= 1
        v = B.delMin()
        assert v == lmin[0]
        del lmin[0]
            
