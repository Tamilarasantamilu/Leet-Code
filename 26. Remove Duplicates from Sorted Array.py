class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lst=nums
        for i in range(len(lst)-1):
            if lst[i]==lst[i+1]:
                lst[i]=-101
        for j in range(lst.count(-101)):
            lst.remove(-101)
        return len(lst)