class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # base case
        if len(strs) == 0:
            return ""

        # initialize longest_prefix
        longest_prefix = strs[0]

        for i in range(1, len(strs)):
            # while the current string isnt starting with the prefix, keep removing last character from the prefix
            while not strs[i].startswith(longest_prefix):
                longest_prefix = longest_prefix[:-1]

        return longest_prefix