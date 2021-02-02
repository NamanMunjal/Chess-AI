from evaluate import Evaluate
import copy
from node import Node

class play():
	
	def __init__(self,board,current_board):
		self.board=board
		self.points=[]
		self.pointstobeawarded={"WK":100,"WQ":9,"WH":3,"WW":3,"WP":1,"WR":5,
								"BK":-100,"BQ":-9,"BH":-3,"BW":-3,"BP":-1,"BR":-5,' ':0}
		self.playit(current_board)

	def playit(self,current_board):
		point=0
		points=[]
		depth=0
		try:
			while depth<=1:
				evaluation_ai=Evaluate(self.board,True)
				aiMoves=evaluation_ai.checkPossibleMoves()
				for aiMove in range(0,len(aiMoves)):
					player_ai=self.board[aiMoves[aiMove][0][0][0]][aiMoves[aiMove][0][0][1]]
					destination_piece=self.board[aiMoves[aiMove][0][1][0]][aiMoves[aiMove][0][1][1]]			
					parentNode=Node(parent=None,board=self.board,move=[[aiMoves[aiMove][0][0][0],aiMoves[aiMove][0][0][1]],[aiMoves[aiMove][0][1][0],aiMoves[aiMove][0][1][1]]],point=self.pointstobeawarded[self.board[aiMoves[aiMove][0][1][0]][aiMoves[aiMove][0][1][1]]])
					self.board[aiMoves[aiMove][0][0][0]][aiMoves[aiMove][0][0][1]]=' '
					self.board[aiMoves[aiMove][0][1][0]][aiMoves[aiMove][0][1][1]]=player_ai
					evaluation_human=Evaluate(self.board,False)
					humanMoves=evaluation_human.checkPossibleMoves()
					for humanMove in range(0,len(humanMoves)):
						player_human=self.board[humanMoves[humanMove][0][0][0]][humanMoves[humanMove][0][0][1]]
						destination_piece2=self.board[humanMoves[humanMove][0][1][0]][humanMoves[humanMove][0][1][1]]
						childNode=Node(parent=parentNode,move=None,board=self.board,point=self.pointstobeawarded[self.board[humanMoves[humanMove][0][1][0]][humanMoves[humanMove][0][1][1]]])
						parentNode.addChild(childNode)
						self.board[humanMoves[humanMove][0][0][0]][humanMoves[humanMove][0][0][1]]=' '
						self.board[humanMoves[humanMove][0][1][0]][humanMoves[humanMove][0][1][1]]=player_human
						evaluation_ai_2=Evaluate(self.board,True)
						aiMoves2=evaluation_ai_2.checkPossibleMoves()
						for aiMove2 in range(0,len(aiMoves2)):
							player_ai2=self.board[aiMoves2[aiMove2][0][0][0]][aiMoves2[aiMove2][0][0][1]]
							destination_piece3=self.board[aiMoves2[aiMove2][0][1][0]][aiMoves2[aiMove2][0][1][1]]
							child2Node=Node(parent=childNode,move=None,board=self.board,point=self.pointstobeawarded[self.board[aiMoves2[aiMove2][0][1][0]][aiMoves2[aiMove2][0][1][1]]])
							self.board[aiMoves2[aiMove2][0][0][0]][aiMoves2[aiMove2][0][0][1]]=' '
							self.board[aiMoves2[aiMove2][0][1][0]][aiMoves2[aiMove2][0][1][1]]=player_ai2
							childNode.addChild(child2Node)
							evaluation_human_2=Evaluate(self.board,False)
							humanMoves2=evaluation_human_2.checkPossibleMoves()
							for humanMove2 in range(0,len(humanMoves2)):
								destination_piece4=self.board[humanMoves2[humanMove2][0][1][0]][humanMoves2[humanMove2][0][1][1]]
								player_human2=self.board[humanMoves2[humanMove2][0][0][0]][humanMoves2[humanMove2][0][0][1]]
								child3Node=Node(parent=child2Node,board=self.board,move=None,point=self.pointstobeawarded[self.board[humanMoves2[humanMove2][0][1][0]][humanMoves2[humanMove2][0][1][1]]])
								self.board[humanMoves2[humanMove2][0][0][0]][humanMoves2[humanMove2][0][0][1]]=' '
								self.board[humanMoves2[humanMove2][0][1][0]][humanMoves2[humanMove2][0][1][1]]=player_human2
								child2Node.addChild(child3Node)
								evaluation_ai_3=Evaluate(self.board,True)
								aiMoves3=evaluation_ai_3.checkPossibleMoves()
								for aiMove3 in range(0,len(aiMoves3)):
									player_ai3=self.board[aiMoves3[aiMove3][0][0][0]][aiMoves3[aiMove3][0][0][1]]
									destination_piece5=self.board[aiMoves3[aiMove3][0][1][0]][aiMoves3[aiMove3][0][1][1]]
									child4Node=Node(parent=child3Node,move=None,board=self.board,point=self.pointstobeawarded[self.board[aiMoves3[aiMove3][0][1][0]][aiMoves3[aiMove3][0][1][1]]])
									child3Node.addChild(child4Node)
									self.board[aiMoves3[aiMove3][0][0][0]][aiMoves3[aiMove3][0][0][1]]=' '
									self.board[aiMoves3[aiMove3][0][1][0]][aiMoves3[aiMove3][0][1][1]]=player_ai3
									self.board[aiMoves3[aiMove3][0][0][0]][aiMoves3[aiMove3][0][0][1]]=player_ai3
									self.board[aiMoves3[aiMove3][0][1][0]][aiMoves3[aiMove3][0][1][1]]=destination_piece5
								self.board[humanMoves2[humanMove2][0][0][0]][humanMoves2[humanMove2][0][0][1]]=player_human2
								self.board[humanMoves2[humanMove2][0][1][0]][humanMoves2[humanMove2][0][1][1]]=destination_piece4
							self.board[aiMoves2[aiMove2][0][0][0]][aiMoves2[aiMove2][0][0][1]]=player_ai2
							self.board[aiMoves2[aiMove2][0][1][0]][aiMoves2[aiMove2][0][1][1]]=destination_piece3
						self.board[humanMoves[humanMove][0][0][0]][humanMoves[humanMove][0][0][1]]=player_human
						self.board[humanMoves[humanMove][0][1][0]][humanMoves[humanMove][0][1][1]]=destination_piece2
					self.board[aiMoves[aiMove][0][0][0]][aiMoves[aiMove][0][0][1]]=player_ai
					self.board[aiMoves[aiMove][0][1][0]][aiMoves[aiMove][0][1][1]]=destination_piece
				depth+=1
		except Exception as e:
				print(e)

board=[['BR','BH','BW','BQ','BK','BW','BH','BR'],
		['BP','BP','BP','BP','BP','BP','BP','BP'],                                                                                                                  
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		['WP','WP','WP','WP','WP','WP','WP','WP'],
		['WR','WH','WW','WQ','WK','WW','WH','WR']]
current_board=[['BR','BH','BW','BQ','BK','BW','BH','BR'],
		['BP','BP','BP','BP','BP','BP','BP','BP'],                                                                                                                  
		['WK',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		[' ',' ',' ',' ',' ',' ',' ',' '],
		['WP','WP','WP','WP','WP','WP','WP','WP'],
		['WR','WH','WW','WQ','WK','WW','WH','WR']]

play(board=board,current_board=current_board)