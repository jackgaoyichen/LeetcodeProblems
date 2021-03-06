__author__ = 'jackgao162'

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lexicalList = []
        for i in range(1,10):
            self.helper(self,i,n,lexicalList)
        return lexicalList

    def helper(self,cur, n, lexicalList):
        if cur > n:
            return
        lexicalList.append(cur)
        for i in range(0, 10):
            if cur * 10 + i <= n:
                self.helper(self,cur * 10 + i, n, lexicalList)
            else:
                break

if __name__ == '__main__':
    sol = Solution
    L = sol.lexicalOrder(sol,9)
    print(L)
    print(len(L))






