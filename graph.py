"""
	Graph algorithms

"""


import sys



def mht(n, l):	
	""" 
	" Minimum height tree solution
	"
	" list l: list of edges
	" int n: vertex count
	"""
	def pop(S):
		if not l:
			return S.pop(len(S)-1)

	def push(S, v):
		S.append(v)



	mht_table = {}
	graph = {}
	for edge in l:
		
		u,v = edge
		if u not in graph:
			graph.setdefault(u, [v])
		else:
			graph[u].append(v)
		if v not in graph:
			graph.setdefault(v, [u])
		else:
			graph[v].append(u)

	print(graph)
	vertices = [ k for k in graph]
	print(vertices)
	Stack = []
	visited = []
	adj_list = None
	adj_flag = False
	u = None
	for v in vertices:
		root = v
		Stack.clear()
		Stack.append( root)
		mht_table.setdefault(v, 0)
		visited.clear()	
		while Stack:
			u = Stack.pop( len(Stack) -1) 
			visited.append(u)
			adj_list = graph[u]
			adj_flag = False	
			for v in adj_list:
				if v not in visited:
					push(Stack, v)
					visited.append(v)
					adj_flag = True
			if adj_flag:
				mht_table[root]+=1	

	
	min_mht = 	n
	for r in mht_table:
		print("Root: "+str(r) + ",\theight:  " + str(mht_table[r]))
		if min_mht < mht_table[r]:
			min_mht = mht_table[r]
def top_preprocess(Graph):
	EC = {}
	adj_list= None

	for v in Graph:
		EC.setdefault(v, 0)


	for v in Graph:
		adj_list = Graph[v]
		for u in adj_list:
			if u not in EC:
				EC.setdefault(u, 0)
			EC[u] +=1
		

	return EC

def topological_sort( Graph, Edge_Count):

	"""
	"""	
	"""	
	"""
	#Sorted List	
	SL = []

	#No edge list	
	NEL = []
	Visited_table = []
	for v in Edge_Count:
		if Edge_Count[v] == 0:
			NEL.append(v)
			#Visited_Table.append(v)

	vertex = None
	cycle = False

	while NEL:
		vertex = NEL.pop(0)
		SL.append(vertex)
		
		adj_list = Graph[vertex]
		for neighbor in adj_list:
			#if neighbor not in Visited_table:
			#	Visited_Table.append(neighbor)
			#else:
			#	cycle = true:				
			Edge_Count[neighbor] -=1
			if Edge_Count[neighbor] == 0:
				NEL.append(neighbor)
	
	#if sorted list count != |Vertices|	
	if len(SL) != len(Graph):
		print("Cycle Detected!")
		return []

	return SL

def __graph_run__(Graph):
	EC = top_preprocess(Graph)
	SL = topological_sort(Graph, EC)
	for v in SL:
		print( v, end= " --> ", flush=False)
	print()

def __test_top__():

		
	G1_Cycle={ 1: [2], 2:[3,4], 3:[5], 4:[5], 5:[6], 6:[10], 10:[11], 11:[5], 7:[8], 8:[]}
	G2_Cycle={ 1: [2,3], 2:[4], 3:[4], 4:[5], 5:[4]}
	G1_None={ 1: [2], 3:[2], 4:[2], 2:[5, 10], 5:[6, 7, 8, 9, 10], 6:[7, 10], 7:[8, 10], 8:[9,10], 9:[10], 10:[]}
	G2_None={ 1: [2], 2:[3,4], 3:[5], 4:[5], 5:[6], 6:[10], 10:[11], 11:[], 7:[8], 8:[]}
	G_Table = [ G1_Cycle, G2_Cycle, G1_None, G2_None]

	for g in G_Table:
		__graph_run__(g)


def detect_cycle(Graph):
	pass
	
def A_Star(graph, start, end):

	def heuristic(v, u):
		pass		

	return

def main():

	mht(4, [[1, 0], [1, 2], [1, 3]])
	mht(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])	

if __name__ == "__main__":
	main()
