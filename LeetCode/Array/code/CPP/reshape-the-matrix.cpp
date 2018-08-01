class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        int n = nums.size(), m = nums[0].size();
        if(n * m < r * c)
            return nums;
        vector<vector<int>> ans(r, vector<int>(c));
        int ni = 0, mj = 0;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                ans[i][j] = nums[ni][mj];
                mj++;
                if(mj == m)
                {
                    mj = 0;
                    ni++;
                }
            }
        }
        return ans;
    }
};