class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output1 = []
        output2 = []
        for i in nums:
            output1.append(i)
            output2.append(i)
        return output1 + output2
