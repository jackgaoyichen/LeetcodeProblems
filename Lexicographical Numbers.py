__author__ = 'jackgao162'

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num = 1
        lexicalList = []
        for i in range(n):
            lexicalList.append(num)
            if num <= n:
                num *= 10
            else:






