class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # counting
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        # decounting
        for c in t:
            if c in d:
                d[c] -= 1
        return(not any(d.values()))