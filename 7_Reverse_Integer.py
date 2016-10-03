#Reverse digits of an integer.

#Example1: x = 123, return 321
#Example2: x = -123, return -321
#Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

#If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

#Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

#For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint = 2147483647
        reverse_num = 0
        if x<0:
            reverse_num = 0-int(str(x)[::-1][:-1])
        else:
            reverse_num = int(str(x)[::-1])
        print sys.maxint
        if reverse_num <-maxint-1 or reverse_num > maxint:
        
            reverse_num = 0
        
        return reverse_num
    
class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0
