class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        avg = int(sum(nums) / len(nums))
        lower_list = []
        greater_list = []
        equal_list = []
        for i in nums:
            if i < avg:
                lower_list.append(i)
            elif i > avg:
                greater_list.append(i)
            else:
                equal_list.append(i)

        return self.sortArray(lower_list) + equal_list + self.sortArray(greater_list)
        