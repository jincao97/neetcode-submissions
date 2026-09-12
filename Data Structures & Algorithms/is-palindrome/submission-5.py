class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join([chr.lower() for chr in s if chr.isalnum()])
        n = len(cleaned_str)
        for i in range(n//2):
            if cleaned_str[i] != cleaned_str[n-(i+1)]:
                return False
            
        return True