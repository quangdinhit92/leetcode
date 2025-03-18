class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        check = {}
        for num in arr:
            check[num] = check.get(num, 0) + 1

        # set of value, if unique, element of set equa to element of dict other wise there us some value has same member

        return sum(set(check.values())) == sum(check.values())
