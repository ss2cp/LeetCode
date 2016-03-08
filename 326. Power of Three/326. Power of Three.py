class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1.0: return True
        if n%3!=0: return False
        if n == 3: return True
        n=n*1.0
        while n>3: 
            n=n/3
            if n == 3: return True
        return False
