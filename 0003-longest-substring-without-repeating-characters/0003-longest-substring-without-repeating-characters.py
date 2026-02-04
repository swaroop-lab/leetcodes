class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        left=0
        charset=set()
        for right in range(0,len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])
            maxl=max(maxl,right-left+1)
        return maxl    

            
