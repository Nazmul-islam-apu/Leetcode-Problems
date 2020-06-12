class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = list()

        num = str(x)
        length = len(num) - 1
        while (length >= 0):
            if (length == 0):
                if (num[length] == '-'):
                    final = ''.join(l)
                    reverse = int(final) * (-1)
                    if (reverse < -(2 ** 31)):
                        return 0
                    else:
                        return reverse
                else:
                    l.append(num[length])
            else:
                l.append(num[length])
            length -= 1
        final = ''.join(l)
        reverse = int(final)
        if (reverse >= (2 ** 31)):
            return 0
        else:
            return reverse

