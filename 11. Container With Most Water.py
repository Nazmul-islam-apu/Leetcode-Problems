class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        if (len(height) == 0):
            return area

        length = len(height) - 1
        i = 0;
        j = length
        while (i < j):
            small = min(height[i], height[j])
            temp = (j - i) * small
            if (temp >= area):
                area = temp

            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return area