class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 1:
            return False
        pairs = {")": "(", "}": "{", "]": "["}

        setOfOpen = pairs.values()

        mystack = []
        for ch in s:
            if ch in setOfOpen:
                mystack.append(ch)
            else:
                if not mystack:
                    return False

                if mystack.pop() != pairs[ch]:
                    return False
        return not mystack
