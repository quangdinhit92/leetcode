class Solution:
    def countAndSay(self, n: int) -> str:

        def count(strNum):

            tmp = []
            m = len(strNum)
            read = 0
            while read < m:
                count = 0
                ch = strNum[read]

                while read < m and ch == strNum[read]:
                    count += 1
                    read += 1
                tmp.append(f"{count}")
                tmp.append(ch)

            return "".join(tmp)

        ret = "1"
        for _ in range(n - 1):
            ret = count(ret)
        return ret
