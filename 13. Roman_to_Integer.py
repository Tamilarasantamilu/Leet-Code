class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_dict = {1: 'I', 5:'V', 10:'X', 50:'L', 100:'C', 500 :'D', 1000:'M',4:'IV',9:'IX', 40:'XL', 90:'XC', 400: 'CD', 900:'CM'}
        roman_val = ""
        for key in reversed(sorted(list(roman_dict.keys()))):
            roman_val += roman_dict[key]*(num//key)
            num=num%key
        return roman_val
