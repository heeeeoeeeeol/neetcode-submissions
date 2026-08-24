class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        s = s.lower()
        while start < end:
            if not s[start].isalpha() and not s[start].isdigit():
                start+=1
                continue
            if not s[end].isalpha() and not s[end].isdigit():
                end-=1
                continue
            if s[start] != s[end]: return False
            start+=1
            end-=1

        return True