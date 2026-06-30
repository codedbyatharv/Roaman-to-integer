class Solution {
public:
    int m, n;
    int ans = 0;

    vector<pair<int, int>> dir = {
        {1, 0}, {-1, 0}, {0, 1}, {0, -1}
    };

    int dfs(vector<vector<int>>& grid, int x, int y, int remain) {

        if (x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == -1)
            return 0;

        if (grid[x][y] == 2)
            return (remain == 1);

        int temp = grid[x][y];
        grid[x][y] = -1;

        int paths = 0;

        for (auto &d : dir) {
            paths += dfs(grid, x + d.first, y + d.second, remain - 1);
        }

        grid[x][y] = temp;

        return paths;
    }

    int uniquePathsIII(vector<vector<int>>& grid) {

        m = grid.size();
        n = grid[0].size();

        int sx, sy;
        int remain = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (grid[i][j] != -1)
                    remain++;

                if (grid[i][j] == 1) {
                    sx = i;
                    sy = j;
                }
            }
        }

        return dfs(grid, sx, sy, remain);
    }
};