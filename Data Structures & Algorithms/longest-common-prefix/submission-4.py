class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(len(pre)):
            for s in strs:
                if i == len(s) or s[i] != pre[i]: return pre[:i]
        return pre