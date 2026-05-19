class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        elif  x == 0 :
            return True
        elif  0< x < 10 :
            return True
        com = []
        while x > 0 :
            a = x % 10
            com.append(a)
            x //= 10
        n = len(com) 
        for i in range( n // 2):
            if(com[i] != com[n - 1- i]):
                return False
        return  True           