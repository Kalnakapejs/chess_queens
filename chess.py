import sys

# RECURSIVE BACKTRACKING
 
# top left corner -> (1,1)
# top right corner -> (N,1)
 
class Solution():
    def next(pos:list[int], N: int)->list[int]:
    # mēģinam iet uz nākamo šūnu pa labi
    # ja tādas nav, ejam uz nākamo rindu
    if pos[0] == N: return [1,pos[1]+1]
    else: return [pos[0]+1,pos[1]]
 
    # count queen placemet nts
    def queens(self,placed:list[list[int]],pos:list[int],N:int)->int:
        if len(placed)==N:
            matrix = ["."*N]*N
            for queen in placed:
                matrix[queen[1]]=list(matrix[queen[1]])
                matrix[queen[1]][queen[0]]="q"
                matrix[queen[1]] = "".join(matrix[queen[1]])
            self.answers.append(matrix)
        if pos[1]==N+1:
            return 
 
    endangered = False
    for queen in placed:
        if queen[0] == pos[0]: endangered=True
        if queen[1] == pos[1]: endangered=True
        if abs(queen[0]-pos[0])==abs(queen[1]-pos[1]):
            endangered = True
    
    self.queens(placed,next(pos,N),N)
 
    if not endangered:
        placed.append(pos)
        queens(placed, next(pos,N),N)
        placed.pop()
 

    def solveNQueens(self, n):
        self.answers = []
        self.queens([],(1,1),n)
        return self.answers