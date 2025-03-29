class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        myMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        n = len(digits)
        results = []

        # for digit in digits:
        def traversal(curIndex, combine):
            if curIndex >= n:
                results.append(combine)
                return

            for letter in myMap[digits[curIndex]]:
                traversal(curIndex + 1, combine + letter)

        if "" != digits:
            traversal(0, "")
            return results
        else:
            return []
