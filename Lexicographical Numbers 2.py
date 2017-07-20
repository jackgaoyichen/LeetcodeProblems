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
        len_n = len(str(n))
        if cur > n:
            return
        lexicalList.append(cur)
        for i in range(0,len_n):
            len_j = 10**(i+1)
            for j in range(0,len_j):
                num = cur * len_j + j
                if num > n:
                    break
                else:
                    lexicalList.append(num)

if __name__ == '__main__':
    sol = Solution
    L = sol.lexicalOrder(sol,1234)
    print(L)
    print(len(L))






