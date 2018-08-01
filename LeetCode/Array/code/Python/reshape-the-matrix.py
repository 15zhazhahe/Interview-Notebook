class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n, m = len(nums), len(nums[0])
        if r * c > n * m:
            return nums
        ans = list()
        ni, mj = 0, 0
        for i in range(r):
            ans.append([])
            for j in range(c):
                ans[i].append(nums[ni][mj])
                mj += 1
                if mj == m:
                    ni += 1
                    mj = 0
        return ans