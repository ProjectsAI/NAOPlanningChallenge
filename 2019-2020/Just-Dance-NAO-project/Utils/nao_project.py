# Importing modules 

from operator import ge
from operator import sub
from operator import add
from operator import le

from functools import partial

from py_search.uninformed import breadth_first_search
from py_search.uninformed import depth_first_search
from py_search.uninformed import iterative_deepening_search

from py_plan.total_order import StateSpacePlanningProblem
from py_plan.base import Operator

class project:
	def __init__(self,constraint_moves,moves,time=180,search_type='iterdeep',threshold = 0.1):
		self.constraint_moves = constraint_moves
		self.moves = moves
		self.time = time
		self.search_type = search_type
		self.threshold = threshold
		
	# Defining three types of Non-Informed Search Strategies 

	def breadth(self,x):
		return breadth_first_search(x, forward=True, backward=False)
		
	def depth(self,x):
		return depth_first_search(x, forward=True, backward=False)
		
	def iterative_deepening(self,x):
		return iterative_deepening_search(x)

	# Defining the algorithm A 

	def A(self,result,constraint_move):
		final_move = constraint_move[0]
		cost_final_move = constraint_move[1]
		
		#################
		##  OPERATIONS ##
		#################

		# Applying an intermediate position: move
		move = Operator('move',
		[('Move','?m'),					# Preconditions: move: m,
		 ('Cost','?m','?c'),				# Cost of the move m (time required): c,
		 ('Time','?t'),						# Time when move m is performed: t,
		 ('StateCounter','?s'),				# Counter of the executed moves: s,
		 (ge,'?t','?c')						# Available time t must be greater than c.
		 ],
		[('not',('Time','?t')),			# Postconditions: available time must be less than or equal to t,
		 ('Time',(sub,'?t','?c')),			# Available time becomes t-c ,
		 ('not',('StateCounter','?s')),		# Counter is no longer s,
		 ('StateCounter',(add,'?s',1)),		# Counter is updated to s+1,
		 ('not',('Move','?m'))				# Move '?m' is no more available
		 ])
		 

		 
		# Applying check to verify the successful conditions, i.e. a path given the problem description and satisfies all the constraints (It is not possible to do this operation directly from the Goal state since it is not possible to express conditions of >,<,>=,<= ): check
		check = Operator('check',
		[								# Preconditions: check
		('StateCounter','?s'),				# Counter of the executed moves: s,
		('Time','?t'),						# Time left: t,
		(le,'?t',self.threshold),			# Time left must be less than a given threshold,
		(ge,'?s',5)							# Counter of the executed moves must be greater than or equal to 5,
		],
		[('not',('Check','NO')),	 	# Postconditions: moving from Check NO to Check YES
		('Check','YES')])
		 
		 

		period = round((self.time/7) - cost_final_move,2)	# Available time for the execution of at least five moves
		
		# Initial state given by:
		# Time = available time for the execution of at least five moves
		# StateCounter = counter of the executed moves
		# Moves = name of every possible move
		# Cost = time required to execute each move
		move_cost_list = [[('Move',i[0]),('Cost',i[0],i[1])] for indx,i in enumerate(self.moves)]
		start = [('Time',period),('StateCounter',0)]
		for k in move_cost_list:
			start += k
		
		# Checking if the termination conditions are satisfied
		goal = [('Check','YES')]

		# Defining the problem and search for the path towards the solution
		p = StateSpacePlanningProblem(start, goal, [move,check]) 
		temp_result = []
		if self.search_type == 'breadth':
			temp_path = (next(self.depth(p)).path())
			for i in range(len(temp_path)-1):
				temp_result.append(temp_path[i][1]['?m'])
			print(temp_result)
		elif self.search_type == 'depth':
			temp_path = (next(self.depth(p)).path())
			for i in range(len(temp_path)-1):
				temp_result.append(temp_path[i][1]['?m'])
			print(temp_result)
		elif self.search_type == 'iterdeep':
			temp_path = (next(self.depth(p)).path())
			for i in range(len(temp_path)-1):
				temp_result.append(temp_path[i][1]['?m'])
			print(temp_result)
		else:
			print(' the only possible values for the argument search_type are "depth", "breadth", "iterdeep" ')

		result += temp_result
		result.append(final_move)
