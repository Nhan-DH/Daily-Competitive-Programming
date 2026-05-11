class Solution(object):
    def separateDigits(self, nums):
        answer = []
        for i in range(len(nums)):
            cur = nums[i]
            temp = []
            while(cur > 0  ):
                temp.append(cur%10)
                cur = cur //10
            temp.reverse()
            answer.extend(temp)
        return answer

        