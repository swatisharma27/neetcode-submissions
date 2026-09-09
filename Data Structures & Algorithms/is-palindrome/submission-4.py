class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        low = 0
        high = N-1

        while low < high:
            if s[low].isalnum():
                if s[high].isalnum():
                    if s[low].lower() == s[high].lower():
                        low += 1
                        high -= 1
                    else:
                        return False
                else:
                    high -= 1
            else:
                low += 1
        return True
