class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        counter1 = sorted(Counter(word1).values())
        counter2 = sorted(Counter(word2).values())

        # khi swap thi tan so cua set khong thay doi
        # khu transform thi tang so cua a thang tan so bua b, tap hop cac tan so khong thay doi , nen khi sort lai thi = nhau

        return counter1 == counter2
