class Solution(object):

    def getConcatenation(self, nums):

        ans = []

        sizee = len(nums)

        run = sizee * 2

        for i in range(run):

            if i < (sizee - 1):

                temp = nums[i]

                ans.append(temp)

            else:

                temp1 = nums[i - sizee]

                ans.append(temp1)

        return ans
