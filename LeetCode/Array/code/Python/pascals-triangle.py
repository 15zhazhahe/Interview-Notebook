class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = list()
        for i in range(numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(ans[i-1][j] + ans[i-1][j-1])
            if i != 0:
                tmp.append(1)
            ans.append(tmp)
        return ans