class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_dict = {}
        for i in nums:
            if check_dict.get(i):
                return True
            else:
                check_dict[i] = True
        return False
        