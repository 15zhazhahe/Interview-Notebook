class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = list()
        n, m = len(A), len(A[0])
        for i in range(m):
            ans.append([])
            for j in range(n):
                ans[i].append(A[j][i])
        return ans