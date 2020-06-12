class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        string = []
        count = 0
        if (numRows == 1):
            return s
        for i in range(len(s)):
            x = i;
            temp = 0
            while (x < len(s)):
                string.append(s[x])
                count += 1
                if (i == (numRows - 1)):
                    i = 0

                if (temp % 2 == 0):
                    x = x + ((numRows - (i + 1)) * 2)
                else:
                    if (i == 0):
                        x = x + ((numRows - (i + 1)) * 2)
                    else:
                        x = x + (2 * i)

                temp += 1

                if (len(string) == len(s)):
                    break
            if (len(string) == len(s)):
                break
        return "".join(string)


