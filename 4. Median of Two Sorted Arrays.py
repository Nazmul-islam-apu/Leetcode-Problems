class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        final = sorted(nums1+nums2)
        l = len(final)
        if(l%2!=0):
            return float(final[l//2])
        else:
            x = final[(l//2)-1]; y = final[l//2]
            med = x+y
            return med/2.0