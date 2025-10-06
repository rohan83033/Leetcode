import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        seen = [[False] * n for _ in range(n)]  # faster than set()
        pq = [(grid[0][0], 0, 0)]  # (time, row, col)
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        
        while pq:
            time, r, c = heapq.heappop(pq)
            if seen[r][c]:
                continue
            seen[r][c] = True
            
            if r == n - 1 and c == n - 1:
                return time  
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    heapq.heappush(pq, (max(time, grid[nr][nc]), nr, nc))
        
        return -1  
