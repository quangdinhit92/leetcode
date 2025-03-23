class Solution:
    def compressedString(self, word: str) -> str:
        ret = []
        read = 0
        n = len(word)
        while read < n:
            count = 0
            ch = word[read]
            while read < n and ch == word[read]:
                count += 1
                read += 1

            tmp = []
            while count > 9:
                tmp.append(9)
                ret.append(f"{9}")
                ret.append(ch)

                count -= 9
            if count > 0:
                tmp.append(count)
                ret.append(f"{count}")
                ret.append(ch)

        print(ret)

        return "".join(ret)
