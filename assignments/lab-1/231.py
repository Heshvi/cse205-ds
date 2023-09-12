class Solution(object):
    def isPowerOfTwo(self, n):

        def ipot(n):
            if n == 1:
                return True
            if n == 0 or n % 2 != 0:
                return False
            return ipot(n / 2)
        
        return ipot(n)   