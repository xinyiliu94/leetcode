'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    '''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n>0:
            remain= n%26
            if remain == 0:
                result = chr(122)+result
                n=n/26-1
            else:
                result = chr(remain+96)+result
                n=n/26
        return result.upper()

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(28)
