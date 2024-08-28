class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range (len(s)):
            len1 = self.FindCenter(s, i, i)
            len2 = self.FindCenter(s, i, i+1)
            max_len = max(len1, len2)
            if end - start < max_len: 
                start = i - (max_len-1)//2
                end = i + max_len//2
        return s[start:end+1]

    def FindCenter(self, s, i, j):
        while(i>=0 and j < len(s) and s[i]==s[j]):
            i -= 1
            j += 1
        return j-i-1

sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"