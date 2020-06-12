class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        final=[]
        integer = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i=12
        while(num):
            rem = num//integer[i]; num = num%integer[i]
            if(rem>0):
                for x in range(rem):
                    final.append(roman[i])
            i-=1
        return ''.join(final)