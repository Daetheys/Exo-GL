import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists
from bheap import BinHeap,EmptyHeap
import random

#On va tester chaque methode au fur et a mesure

def test_rotten_green_test():
    #Just to check if the module works correctly
    pass

#Petits tests en boite noire (on verifie juste que le code fait bien son travail de tas, on s'en fiche de __percUp __percDown qui sont des fonctions internes)

def test_insert1():
    B = BinHeap()
    B.insert(3)
    assert B.delMin() == 3

def test_insert2(): #1 -> Boucle infinie dans __percUp
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
    l2 = []
    for i in range(len(l)):
        print(B.heapList)
        l2.append(B.delMin())
    assert l2 == l
		
#Tests plus precis sur la structure de donnees pour verifier que tout est en ordre a l'interieur pour les plus gros tests qui suivent (white box)
		
def test_init():
    B = BinHeap()
    assert B.heapList == [0]
    assert B.currentSize == 1

def test_mechant():
    B = BinHeap()
    try:
        B.delMin()
        assert False
    except EmptyHeap:
        pass
    
#C'est pas beau de tester les private mais c'est pour la bonne cause
def test_percUp():
    l = [0,1,2,3,4,5,6,1]
    B = BinHeap()
    B.heapList = l
    B.currentSize = len(l)
    B.percUp(7)
    assert B.heapList == [0,1,2,1,4,5,6,3]
	
def test_percDown():
    l = [0,5,1,2,3,4,5,6]
    B = BinHeap()
    B.heapList = l
    B.currentSize = len(l)
    B.percDown(1)
    assert B.heapList == [0,1,3,2,5,4,5,6]

def test_minChild():
    l = [0,5,3,2,1,4]
    B = BinHeap()
    B.heapList = l
    B.currentSize = len(l)
    assert B.minChild(2) == 4
    assert B.minChild(1) == 3
	
def assert_heap_struct(l,i): #Test la structure du sous tas commencant a i
	if i*2<len(l):
		if l[i]<=l[i*2]:
			assert_heap_struct(l,i*2)
		else:
			assert False
	if i*2+1<len(l):
		if l[i]<=l[i*2+1]:
			assert_heap_struct(l,i*2+1)
		else:
			assert False

#Test fondamental : test si le tas fait bien ce qu'on lui demande de faire (black box)
@given(lists(elements=integers()))
def test_fonda(l):
    B = BinHeap()
    B.buildHeap(l)
    
    assert_heap_struct(B.heapList,1) #Exception : Petit test en white box juste pour verifier que tout se passe bien
    
    last_v = None
    print(B.heapList)
    while B.currentSize > 1:
        v = B.delMin()
        print(last_v,v)
        assert last_v == None or last_v <= v
        last_v = v
        
@given(lists(elements=lists(elements=integers())))
def test_fonda2(ll): #ll est une liste de liste d'elements a ajouter. On va ajouter successivement tous les elements des listes a B puis entre chaque liste, on va enlever les elements de maniere assez aleatoire.
    #Ajoute et enleve des elements a la suite au hazard
    B = BinHeap()
    lmin = []
    count = 0
    for l in ll:
        for e in l:
            B.insert(e) #Ajout des elements
            
            assert_heap_struct(B.heapList,1) #Exception : Petit test en white box juste pour verifier que tout se passe bien
            
        count += len(l)
        lmin += l
        lmin.sort() #Pour verifier la sortie
        for i in range(random.randint(0,count)): #On enleve un nombre alea d'elements
            count -= 1
            v = B.delMin() #Suppression d'un element
    
                
    	    assert_heap_struct(B.heapList,1) #Exception : Petit test en white box juste pour verifier que tout se passe bien
    			
                
            assert v == lmin[0]
            del lmin[0]
    for i in range(count): #On vide tout ce qui reste (on n'est pas certain que le tas soit vide a l'issu de la derniere iteration des ajouts des listes et des suppressions alea)
        count -= 1
        
        
    	assert_heap_struct(B.heapList,1) #Exception : Petit test en white box juste pour verifier que tout se passe bien
    	
        
        v = B.delMin()
        assert v == lmin[0]
        del lmin[0]
            
