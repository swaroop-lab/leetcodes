class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear=""
        for ch in s:
            if ch.isalnum():
                clear+= ch.lower()
        return clear == clear[::-1]




