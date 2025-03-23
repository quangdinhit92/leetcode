class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        while read < n:
            count = 0
            ch = chars[read]
            while read < n and ch == chars[read]:
                read += 1
                count += 1
            chars[write] = ch
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        chars = chars[:write]
        return write
