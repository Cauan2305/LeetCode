import math

class Solution(object):
    def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        if num < 0:
            return False

        numero_original = num
        numero_invertido = 0

        while num > 0:
            ultimo_digito = num % 10
            numero_invertido = numero_invertido * 10 + ultimo_digito
            num //= 10

        return numero_original == numero_invertido
    
print(Solution().isPalindrome(num=1000021))