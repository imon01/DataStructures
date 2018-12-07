import gc
import os
import sys

import argparse 
import numpy as np
from random import randint



class BaseNode(object):
	"""
	"""
	"""
	"""
	
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return str(self.value)
	
	def get_data(self):
		return self.value

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class BinaryNode(BaseNode):		
	"""
	"""
	"""
	"""
	def __init__(self, value=None, left=None, right=None):
		super().__init__(value)
		self.left = left
		self.right = right
		self.parent = None
		self.height = 0
	
	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		#if( right is None):
		#	raise TypeError	
		self.right = right 

	def set_parent(self, parent):
		self.parent = parent 

	def set_height(self, height=0):
		self.height +=height

	def clear_height(self, value):
		self.height = value

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right


	def get_parent(self):
		return self.parent	

	def get_height(self):
		return self.height


class AVLNode(BinaryNode):
	
	def __init__(self, value=None):
			super().__init__(value)
			self.bf = 0

	def set_bf(self, value):
		self.bf +=value

	def get_bf(self):
		return self.bf




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Tree(object):
	"""
	"""
	"""
	"""
	def __init__(self, node=None):
		self.root = node 
			
	
	def print(self, order=None, depth_factor=10):
		#error check 
		if order is None or order =="pre":
			self.preAux(self.root, 0, depth_factor)

		if order == "in":
			self.inAux(self.root, 0, depth_factor)

		if order == "post":
			self.postAux(self.root, 0, depth_factor)


	def preAux(self, node, level, depth_factor):
		if node is None:
			return	
		if node is self.root:
				print("R: " + str(node) )
		else:	
			print( "."*level*depth_factor + str(node) )
		self.preAux(node.get_left(), level+1, depth_factor)
		self.preAux(node.get_right(), level+1, depth_factor)

	def inAux(self, node, level, depth_factor):
		if node is None:
			return
		self.inAux(node.get_left(), level+1, depth_factor)
		if node is self.root:
			print("R: " + str(node) )
		else:	
			print( "."*level*depth_factor + str(node) )
		self.inAux(node.get_right(), level+1, depth_factor)
	
	def postAux(self, node, level, depth_factor):
		if node is None:
			return	
		self.postAux(node.get_left(), level+1, depth_factor)
		self.postAux(node.get_right(), level+1, depth_factor)
		if node is self.root:
			print("R: " + str(node) )
		else:	
			print( "."*level*depth_factor + str(node) )
		
		
	def getHeight(self, node):
		if node is None:
			return 0
		left = 1 + self.getHeight( node.get_left())
		right = 1 + self.getHeight( node.get_right())

		if( left < right):
			return right

		return left


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Heap(object):
	
	def __init__(self, array):
		self.array = array
		self.index = 0
		self.count = 0
		if array[0] is not None:
			self.count+=1

	def insert(self, value):
		raise NotImplementedError("Subclass failed abstract method implementation")

	def heapify(self):
		raise NotImplementedError("heapify: unimplemented abstract method ")

	
	@property		
	def root(self):
		return self.array[0]	
	
	def __str__(self):
		return str(self.array)

	def delete(self, value=None):
		raise NotImplementedError("delete: unimplemented abstract method")
			
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
class MinHeap(Heap):
	def __init__(self, value=None):
		array = [None]
		if value is not None:
			array[0] = value	
		super().__init__(array)	
								
	def insert(self, value):
		
		if self.array[0] == None:
			self.array[0] = value	
			self.count += 1
			return
		self.array.append(value)
		self.count += 1
		self.heapify()		

	def heapify(self):
		
		c_idx = len(self.array)-1
		p_idx = int( (c_idx -2) /2) 
		
		#if odd
		if c_idx %2 : 
			p_idx = int((c_idx-1)/2)

		heap = self.array
		t = None
		while heap[c_idx] < heap[p_idx]:
			t = heap[p_idx]
			heap[p_idx] = heap[c_idx]
			heap[c_idx] = t		
			c_idx = p_idx
			p_idx = int(  (c_idx - 2)/2)
			if c_idx%2:
				p_idx = int(  (c_idx - 1)/2)
				
			if p_idx < 0:
				break		


	def delete(self, value=None):
		#error check: self.array is non-empty
		if self.count == 0:
			raise ValueError("Can' delete from empty array")	

		idx = 0	
		value = self.array[0]
		array = self.array	
		lc_idx, rc_idx = idx*2 +1, idx*2+2
		while 1:
			#edge case: check lc, rc bounds
			if lc_idx > self.count  :
				break
			if lc_idx < self.count and self.count <= rc_idx:
				array[idx] = array[lc_idx]
				break

			#if lc > rc:
			if array[lc_idx] < array[rc_idx]:
				array[idx] = array[lc_idx]
				idx = lc_idx
			else:
				array[idx] = array[rc_idx]
				idx = rc_idx	
			lc_idx, rc_idx = idx*2 +1, idx*2+2
			 
		self.count -=1
		return value
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
class MaxHeap(Heap):

	def __init__(self, value=None):
		array = [None]	
		if value is not None:
			array[0] = value	
		super().__init__(array)	
	

	def insert(self, value):
		
	
		if self.array[0] == None:
			self.array[0] = value	
			self.count += 1
			return
		self.array.append(value)
		self.count += 1
		self.heapify()		


	def heapify(self):
		c_idx = len(self.array)-1
		p_idx = int( (c_idx -2) /2) 
		
		#if odd
		if c_idx %2 : 
			p_idx = int((c_idx-1)/2)

		heap = self.array
		t = None
		while heap[c_idx] > heap[p_idx]:
			t = heap[p_idx]
			heap[p_idx] = heap[c_idx]
			heap[c_idx] = t		
			c_idx = p_idx
			p_idx = int(  (c_idx - 2)/2)
			if c_idx%2:
				p_idx = int(  (c_idx - 1)/2)
				
			if p_idx < 0:
				break		
				
	def delete(self):
		#error check: self.array is non-empty
		if self.count == 0:
			raise ValueError("Can' delete from empty array")	
		value = self.array[0]

		idx = 0	
		array = self.array	
		lc_idx, rc_idx = idx*2 +1, idx*2+2
		while 1:
			print("array length: "+str( self.count) + "\t\tlc: "+str(lc_idx))	
			#edge case: check lc, rc bounds
			#if no left child, then no children
			if lc_idx  > self.count:
				break
			if lc_idx < self.count and rc_idx >= self.count:
				array[idx] = array[lc_idx]
				break
			#if lc > rc:
			if array[lc_idx] > array[rc_idx]:
				array[idx] = array[lc_idx]
				idx = lc_idx
			else:
				array[idx] = array[rc_idx]
				idx = rc_idx	
			lc_idx, rc_idx = idx*2 +1, idx*2+2
		
		self.count -=1
		return value

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class AVLTree(Tree):
	
	"""
	"" AVL Tree implementation
	"""
	""
	""
	""
 
	def __init__(self,value=None):
		if value is not None:	
			super(AVLTree, self).__init__( AVLNode(value))
		else:
			super(AVLTree, self).__init__()

	def insert(self, value):
		"""
		Remarks:  	variable 'pivot_node' captures the node with an unsatisfactory
					BF value. That is, the last node with BF != 0, and must be 
					rotated appropriately.

		"""


		if self.root is None:
			self.root = AVLNode(value)	
			return

		call_left = True
		pivot_node = None
		prev = None
		curr = self.root
		duplicate = False
		while curr is not None:
			t = curr.get_data()	
			if t  == value:
				duplicate = True
				break
			
			curr.set_height(1)#increments height by one
			prev = curr
			if  value  < t:
				curr.set_bf(1)
				
				call_left = False	
				#pivot right
				if curr.get_bf() > 1:
					pivot_node = curr 
				curr = curr.get_left()
			else:
				curr.set_bf(-1)
				call_left = True
				#pivot left
				if curr.get_bf() < -1:
					pivot_node = curr
				curr = curr.get_right()
			
		if duplicate:
			sys.stdout.write("duplicate value "+ str(value) + "\n")
			sys.stdout.flush()
			return

		node = AVLNode(value)
		if value < prev.get_data():
			prev.set_left( node )			
		else:
			prev.set_right( node )

		
		node.set_parent(prev)

		if pivot_node is None or abs(pivot_node.get_bf()) <= 1:
			return

		if call_left:
			self.leftRotate(pivot_node)			
		else:
			self.rightRotate(pivot_node)

	def balanceFactor(self, node):
		l,r = 0,0
		nL, nR = node.get_left(), node.get_right()
		if nL is not None:
			 l = nL.get_height()

		if nR is not None:
			r = nR.get_height()

		print("roots.bf = " + str(self.root.bf))
		return  (l-r)	


	def balanceFactor(self, node=None):
			
		if node is None:
			if self.root is None:
				return -1
			node = self.root
	
		print("roots.bf = " + str(self.root.bf))
		return self.getHeight( node.get_left()) - self.getHeight( node.get_right() ) 


	def leftRotate(self, node):
		#Debugging messages
		print("__Call___: leftRotate")
		print( str(node) +  " bf= "+ str(node.bf))				

		parent = node.get_parent()
		pivot_node = node.get_right() 

		pivot_l_subtree = pivot_node.get_left()
		node.set_right( pivot_l_subtree)

		if pivot_l_subtree is not None:
			pivot_l_subtree.set_parent(node)

		
		node.set_bf(1)
		node.set_height(-1)	
		pivot_node.set_bf(1)
		pivot_node.set_left(node)
		node.set_parent(pivot_node)
		pivot_node.clear_height( self.balanceFactor(pivot_node))		


		#changing root node
		if parent is None:
			pivot_node.set_parent(None)
			self.root = pivot_node
			return

		self.updatePostRotate(node, parent, pivot_node, "left")
		

	def rightRotate(self, node):
		#Debugging messages, remove once done
		print("__Call___: rightRotate")
		print( str(node) +  " bf= "+ str(node.bf))				

		parent = node.get_parent()	
		pivot_node = node.get_left()
	
		pivot_r_subtree = pivot_node.get_right()
		node.set_left( pivot_r_subtree)

		if pivot_r_subtree is not None:
			pivot_r_subtree.set_parent(node)

		node.set_bf(-1)
		node.set_height(-1)
		pivot_node.set_bf(-1)
		pivot_node.set_right(node)
		node.set_parent(pivot_node)	
		pivot_node.clear_height( self.balanceFactor(pivot_node) )	
			
		if parent is None:
			pivot_node.set_parent(None)
			self.root = pivot_node 
			return
	
		self.updatePostRotate(node, parent, pivot_node, "right")
	
	def updatePostRotate(self, node, parent, pivot_node, rotate):
		"""
			Remarks:	Updating balance factor for nodes, starting at node and 
						ending at root.
		"""

		if parent.get_data() < node.get_data():
			parent.set_right(pivot_node)
		else:
			parent.set_left(pivot_node) 

		value = -1
		if rotate == "left":
			value = 1

		while parent is not None:
			parent.set_bf(value)
			parent = parent.get_parent()

			
	def leftRight(self, node):
		self.leftRotate(node)
		self.rightRotate(node)

	def rightLeft(self, node):
		self.rightRotate(node)
		self.leftRotate(node)

	
	def print(self, order=None, factor=5):
		super().print(order, factor)


	
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class RBTree(Tree):
	"""
		TODO
	"""
	
	def __init__(self, value):
	
		if value is not None:
			super().__init__( BinaryNode(value))	
		else:
			super().__init__(value)
		self.root.color = 1
		
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class BinarySearchTree:

		def __init__(self, value=None):
					
			self.root =None	
			if value is not None:
				self.root = BinaryNode(value)

		
	
		def insert(self, value):
			if self.root is None:
				self.root = Node(value)
				return
	
			parent = None	
			curr = self.root
			found = False	
			while( curr is not None ):
				if curr.get_data() == value:
					found = True
					break	
			
				parent = curr	
				if curr.get_data() < value:
					curr = curr.get_left()	
				else:
					curr = curr.get_right()	
			
			if found:
				sys.stdout.write("duplicate value "+ str(value) + "\n")
				sys.stdout.flush()
				return
		
			if parent.get_data() <= value:
				parent.set_left( BinaryNode(value)	 )
			else:
				parent.set_right( BinaryNode(value))

		def get_height(self):
			pass
	
		def get_depth(self, value):
			if value == self.root.get_data():
				return 0
	
		def print(self, order=None, depth_factor=5):
			
			#error check 
			if order is None or order =="pre":
				self.pre_aux(self.root, 0, depth_factor)

			if order == "in":
				self.in_aux(self.root, 0, depth_factor)

			if order == "post":
				self.post_aux(self.root, 0, depth_factor)


		def pre_aux(self, node, level, depth_factor):
			if node is None:
				return	
			print( "."*level*depth_factor + str(node) )
			self.pre_aux(node.get_left(), level+1, depth_factor)
			self.pre_aux(node.get_right(), level+1, depth_factor)

		def in_aux(self, node, level, depth_factor):
			if node is None:
				return
			self.pre_aux(node.get_left(), level+1, depth_factor)
			print( "."*level*depth_factor + str(node) )
			self.pre_aux(node.get_right(), level+1, depth_factor)
		
		def post_aux(self, node, level, depth_factor):
			if node is None:
				return	
			self.pre_aux(node.get_left(), level+1, depth_factor)
			self.pre_aux(node.get_right(), level+1, depth_factor)
			print( "."*level*depth_factor + str(node) )

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


Linked List implementation.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class LL_Node(BaseNode):
	def __init__(self, value=None, node=None):
		super().__init__(value)	
		self.next = None 

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next
	
#	def get_data(self):
#		return self.value	

class LList:
	def __init__(self):
		self.head = None
		self.last = None	
		self.length = 0
			
	def get_length(self):
		return self.length	

	def get_head(self):
		return self.head
	
	def add(self, value):
	
		node = LL_Node(value, self.head)

		if( self.head is None):
			self.head = node

		if( self.last is None):
			self.last = node
		else:
			self.last.set_next(node)
			self.last = node	
			
		self.length += 1

	def print(self):
		
		curr = self.head

		while curr is not None:
			print( curr, " ", end="")
			curr = curr.get_next()
		print()
	
	def reverse(self):
		
		curr = self.head
		prev = None
		sto = None
		while curr is not None:
			sto = curr.get_next()
			curr.set_next(prev)
			prev = curr
			curr = sto 
	
		self.head = prev

	def toDigit(self):
		curr = self.head
		i, n = 0,0
		t = 0
		while( curr is not None):
			if i > 7:
				break
			t = curr.get_data()*(10**i)
			n+= t 
			i+=1
			curr = curr.get_next()
		print()	
		return n

	def sort(self):
		#TODO
		pass	
		

	def merge(self, l):
		#
		#	l := list to merge with
		#

		this_curr = self.head
		merge_curr = l.get_head()
		cache = None 
	
		l_head = l.get_head()	
		prev = None	
		len1 = self.length
		len2 = l.get_length()

		if l_head.get_data() <= self.head.get_data():
			self.head = l_head

		while( 1 ):
			if  merge_curr is None:
				break
			if this_curr is None and merge_curr is not None:
				prev.set_next(merge_curr)
				break
	
			if merge_curr.get_data() <= this_curr.get_data() :
				if prev is not None: 	
					prev.set_next(merge_curr)
				cache = merge_curr.get_next()
				merge_curr.set_next(this_curr)
				merge_curr = cache

			prev = this_curr
			this_curr = this_curr.get_next()	

		self.length += len2
		l.head = None	
		gc.collect()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Ad hoc testing functions for Data structure classes.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def __test_LL__():

	print("BEGIN:: __test_LL__")
	L1 = LList()	
	L2 = LList()	
	for i in range(0, 4):
		L1.add(randint(0, 9))
		L2.add(randint(0, 9))

	L1.print()
	print("L1 to digit: " + str( L1.toDigit()))
	L2.print()
	print("L2 to digit: " + str( L2.toDigit()))

	L1.merge(L2)
	L1.print()
	print("\nPost Merge L1 to digit: " + str( L1.toDigit()))

	print("END:: __test_LL__")

def __test_BTree__():
	print("BEGIN:: __test_BTree__()")	
#	btree = BinarySearchTree(10)
#	for i in [8, 9, 10, 1, 20, 21, 3]:
#		btree.insert(i)
#	for s in ["pre", "in", "post"]:
#		btree.print(s)
#		print()

	tree2 = BinarySearchTree()

	for i in range(0, 15):
		tree2.insert( randint(0, 100))
	
	for s in ["pre", "in", "post"]:
		tree2.print(s)
		print()

	print("END:: __test_BTree__()")	

def __test_RBTree__():
	
	print("BEGIN:: __test_RBTree__()")	
	print("END:: __test_RBTree__()")	


def __test_AVLTree__():
	
	print("BEGIN:: __test_AVLTree__()\n")

	test_table={
		"balance":__AVL_Balance__,
		"left": __AVL_Left__,
		"right":__AVL_Right__
	}	

	test = input("test name: ")

	for f in test_table:
		if test == f:
			user = input("input values:")	
			args = [ int(token) for token in user.split(" ")]
			test_table[f](args)
	
	print("END:: __test_AVLTree__()")	

def __AVL_Balance__( args):

	print("AVL: testing balance")
	t_balance = AVLTree()

	for i in args:
		t_balance.insert(i)
	t_balance.print("in")
	print("Balance Factor: "+ str( t_balance.balanceFactor()))	


def __AVL_Left__(args):

	print("AVL: left imbalance (heavy) ")
	print("case: 1")

#	t1 = AVLTree()
#	for i in [8, 7, 6]:
#		t1.insert(i)
#		t1.print("in")
#		print()
#	print("Balance Factor: "+ str( t1.balanceFactor()) + "\n")	

	print("case: 2")
	t2 = AVLTree()
	for i in args:
		t2.insert(i)
		t2.print("in")
		print()
	print("Balance Factor: "+ str( t2.balanceFactor()) + "\n")	
	
#	print("case: 3")




def __AVL_Right__(args): 	
	print("AVL: right imbalance (heavy) ")
	print("case: 1")

	t1 = AVLTree()
	for i in args:
		t1.insert(i)
		t1.print("in")
		print()
	print("Balance Factor: "+ str( t1.balanceFactor()) + "\n")	


	print("case: 2")
	print("case: 3")

def __AVL_LR__():
	pass

def __AVL_LL__():
	pass

def __AVL_RL__():
	pass

def __AVL_RR__():
	pass	



def __test_min_heap__():

	t2 = [ 1, 9, 8, 16, 55, 17, 61, 0]
	
	h = MinHeap()

	for i in t2:
		h.insert(i)
		print(h)
	#h.insert(  i for i in t2)

	print(h)

def __test_stream_median__():
	
	h_min = MinHeap()
	h_max = MaxHeap()
	stream = [ 9, 10, 8, 6, 5, 7, 6, 20, 1, 19, 18, 61, 55, 37, 61, 0]
	h_max.insert( stream.pop(0))
	h_min.insert( stream.pop(0))

	for i in stream:

		if i  < h_max.root:
			h_max.insert(i)
		else:
			h_min.insert(i)

		if h_max.count +1 > h_min.count:
			h_min.insert(h_max.delete())
		else:
			h_max.insert( h_min.delete())
	
	median =  int((h_max.root + h_min.root )/2)

	stream = [ 10, 9, 8, 6, 5, 7, 6, 20, 1, 19, 18, 61, 55, 37, 61, 0]
	print(h_min)
	print(h_max)
	print("median: " + str(median))
	print("actual median: " + str( np.median(stream)))



def __test_max_heap__():
	t2 = [ 10, 9, 8, 6, 5, 7, 6, 20]
	
	h = MaxHeap()

	for i in t2:
		h.insert(i)
		print(h)
	#h.insert(  i for i in t2)

	print(h)

	
def __test_heap__():
	table = {"min": __test_min_heap__,
			"max": __test_max_heap__,
			"median": __test_stream_median__
			}

	test_type = input("min, max, median: ")

	if test_type in table:
		print("running "+ test_type +"....")	
		table[ test_type]()
	else:
		print("invalid test: "+ test_type)



def main():

	test_table ={
		"ll" : __test_LL__,
		"binary trb tb": __test_BTree__,
		"avl tree": __test_AVLTree__,
		"rb tbree" : __test_RBTree__,
		"heap": __test_heap__,
		"": None
		}
	
	test = sys.argv[1] 
	if test in test_table:
		test_table[test]()
	else:
		print("Error: test= \"" + test + "\" not found" )


def profiler(frame, event, arg):
    print(event, frame.f_code.co_name, frame.f_lineno, "->", arg)

if __name__== "__main__":
	main()
