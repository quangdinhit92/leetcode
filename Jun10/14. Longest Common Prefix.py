class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        pref =strs[0]

        for word in strs[1:]:
            # compare prefix with word intill match 
            while not word.startswith(pref):
                pref=pref[:-1]
        return pref
