class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join([chr.lower() for chr in s if chr.isalnum()])
        n = len(cleaned_str)
        for i in range(n):
            if cleaned_str[i] != cleaned_str[-(i+1)]:
                return False
            
        return True