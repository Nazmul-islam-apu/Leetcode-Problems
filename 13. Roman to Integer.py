class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        number = [1, 5, 10, 50, 100, 500, 1000]
        l = len(s) - 1;
        num = 0;
        i = 0
        while (l >= 0):
            i = roman_list.index(s[l])
            if (l == len(s) - 1):
                num += number[i]
            else:
                if (i < roman_list.index(s[l + 1])):
                    num -= number[i]
                else:
                    num += number[i]
            l -= 1
        return num
