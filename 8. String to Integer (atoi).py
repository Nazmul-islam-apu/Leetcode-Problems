class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str);
        num = [];
        sign = '';
        sign_count = 0
        for i in range(length):
            if (ord(str[i]) == 45):
                if (len(num) > 0):
                    break
                else:
                    sign = '-';
                    sign_count += 1
            elif (ord(str[i]) == 43):
                if (len(num) > 0):
                    break
                else:
                    sign = '+';
                    sign_count += 1
            elif (ord(str[i]) >= 48 and ord(str[i]) <= 57):
                num.append(str[i])
            elif (ord(str[i]) == 32 and len(num) > 0):
                break
            elif (ord(str[i]) == 32 and sign_count > 0):
                break
            elif (ord(str[i]) != 32):
                break

        if (sign_count > 1):
            return 0

        if (len(num) == 0):
            return 0
        final = int(''.join(num))

        if (sign == '-'):
            final = final * (-1)

        if (final > (2 ** 31 - 1)):
            return (2 ** 31 - 1)
        elif (final < -(2 ** 31)):
            return -(2 ** 31)
        else:
            return final