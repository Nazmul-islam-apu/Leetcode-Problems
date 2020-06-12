class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s);final=0;dic={}
        i=j=0
        while((i<length) and (j<length)):
            if(s[j] in dic):
                del dic[s[i]]
                i+=1
            else:
                dic[s[j]]=1
                j+=1
                final = max(final,j-i)
        return final