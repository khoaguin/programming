#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        My solution: Using 2 pointers
        Runtime beats 54.07 % of python3 submissions (O(n) because of the first loop in extracted_string)
        Mem usage beats 22.44 % of python3 submissions (O(2n) since using another variable)
        """
        extracted_string = "".join(c for c in s.lower() if c.isalnum())
        i = 0
        j = -1
        while i < (len(extracted_string) / 2):
            if extracted_string[i] != extracted_string[j]:
                return False
            i += 1
            j -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        """
        Better solution
        """
        lp = 0  # left pointer
        rp = len(s) - 1  # right pointer
        while lp < rp:
            while lp < rp and not s[lp].lower().isalnum():
                lp += 1
            while lp < rp and not s[rp].lower().isalnum():
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        """
        Even better yet solution
        Runtime beats 99.43 % of python3 submissions (O(n))
        Memory usage beats 35.57 % of python3 submissions (O(1))
        """
        lp = 0  # left pointer
        rp = len(s) - 1  # right pointer
        while lp < rp:
            if not s[lp].lower().isalnum():
                lp += 1
            elif not s[rp].lower().isalnum():
                rp -= 1
            else:
                if s[lp].lower() != s[rp].lower():
                    return False
                lp += 1
                rp -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(s.isPalindrome(s="aca"))
    print(s.isPalindrome(s="maam"))
    print(s.isPalindrome(s="race a car"))
    print(s.isPalindrome(s=" "))
    print(s.isPalindrome(s=".,"))

# @lc code=end
