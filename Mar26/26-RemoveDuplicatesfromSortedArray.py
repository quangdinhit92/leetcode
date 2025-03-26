class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        write = 0
        n = len(nums)
        check = set()
        for i in range(n):
            # not in -> do no thing move next
            if nums[i] not in check:
                nums[write] = nums[i]
                write += 1
                check.add(nums[i])

        # for j in range(write,n):
        #     nums[j] ="_"
        return write

        # write =0
        # n=len(nums)
        # if n<=1:
        #     return n
        # for i in range(1,n):
        #     if nums[i-1] ==nums[i]:
        #         continue
        #     write+=1
        #     nums[write] = nums[i]

        # return write+1
