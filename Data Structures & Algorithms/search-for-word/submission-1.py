class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        mask, idx, flag = 0, 0, False
        def backtrack(r, c):
            nonlocal mask, idx, flag

            if idx == len(word): 
                flag = True
                return

            if not flag and 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == word[idx] and not mask & 1 << (r*len(board[0])+c):
                mask |= 1 << (r*len(board[0])+c)
                idx += 1
                
                backtrack(r-1, c)
                backtrack(r+1, c)
                backtrack(r, c-1)
                backtrack(r, c+1)

                mask &= ~(1 << (r*len(board[0])+c))
                idx -= 1

            if not mask and not flag: 
                c += 1
                if c == len(board[0]):
                    if r == len(board): return
                    c = 0
                    r += 1

                backtrack(r, c)

        backtrack(0, 0)
        return flag


            

                
                
                

            