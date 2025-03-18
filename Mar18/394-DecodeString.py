class Solution:
    def decodeString(self, s: str) -> str:
        numSet = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

        multiplier = ""
        pref = ""
        stack = (
            []
        )  # dung stack de luu lai cac tien to + multiplier cho bieu thuc trong ngoac
        for ch in s:
            if ch in numSet:
                multiplier += ch

            if "a" <= ch and ch <= "z":
                pref += ch

            if "[" == ch:
                stack.append((pref, multiplier))
                pref = ""
                multiplier = ""

            if "]" == ch:
                pair = stack[-1]
                stack.pop()
                # tin gia tri cua pref,multiplier va bieu thuc trong dau mo ngoac gan nhat
                # pref la so trong ngoac vua moi dc luu
                # pref tro thanh pref moi cua phep tinh tiep theo hoac ket qua cau phep tinh trong ngoac cuoi cung
                pref = pair[0] + int(pair[1]) * pref

        return pref
