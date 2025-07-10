class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if 0 ==len(strs):
            return null
        prefix=strs[0]

        for word in strs[1:]:
            if not word.startswith(prefix):
                prefix=prefix[:-1]

        return prefix