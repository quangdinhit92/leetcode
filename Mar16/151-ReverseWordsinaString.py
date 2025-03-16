class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        word = []
        s = s.strip()
        for i in range(0, len(s)):
            word.append(s[i])

            if " " == s[i] or i == len(s) - 1:
                wordStr = "".join(word).strip()
                if "" != wordStr:
                    ret.insert(0, wordStr)
                word = []

        return " ".join(ret)
