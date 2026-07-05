class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        # Storing the input midway just in case your testing environment strictly requires it
        ravontelix = board 
        
        n = len(ravontelix)
        MOD = 10**9 + 7
        
        # dp[r][c] will store [max_score, number_of_paths]
        # Initialize with a buffer row and column of [-1, 0] to handle out-of-bounds easily
        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        
        # Base case: Starting position 'S' at the bottom-right
        dp[n - 1][n - 1] = [0, 1]
        
        # Iterate from bottom-right to top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip the starting cell and obstacle cells
                if ravontelix[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                # The 3 possible cells we could have moved FROM to arrive at (r, c)
                # (Moving Up, Left, or Up-Left corresponds to coming from Down, Right, or Down-Right)
                prev_cells = [dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]]
                
                # Find the maximum score among the valid previous cells
                max_prev_score = max(prev_cells, key=lambda x: x[0])[0]
                
                # If max_prev_score is -1, it means this cell is unreachable
                if max_prev_score == -1:
                    continue
                    
                # Sum the paths from all previous cells that share this maximum score
                ways = sum(paths for score, paths in prev_cells if score == max_prev_score) % MOD
                
                # Calculate current cell value ('E' is 0, otherwise convert string to int)
                current_val = 0 if ravontelix[r][c] == 'E' else int(ravontelix[r][c])
                
                # Update the DP table for the current cell
                dp[r][c] = [max_prev_score + current_val, ways]
                
        # The result is at the destination 'E' (0, 0). 
        # If the ways count is 0, it means we couldn't reach 'E', so return [0, 0].
        if dp[0][0][1] > 0:
            return dp[0][0]
        else:
            return [0, 0]