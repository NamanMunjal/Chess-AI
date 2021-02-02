class Node():
	def __init__(self,parent,board,move,point):
		self.parent=parent
		self.board=board
		self.move=move
		self.point=point
		self.children=[]

	def addChild(self,child):
		child.parent=self
		self.children.append(child)