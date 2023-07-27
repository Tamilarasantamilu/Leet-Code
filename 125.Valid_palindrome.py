class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        p = s.lower()
        special_char = "\"_-!@#$%^&*()[]{}:,./' /'?<>;~`"
        while(left <= right):
            if (p[left] == p[right]):
                # print(p[left],p[right])
                left += 1
                right -= 1
            elif p[left] in special_char:
                left += 1
            elif p[right] in special_char:
                right -= 1
            else:
                # print(p[left],p[right])
                return False
                
        return True
            
            