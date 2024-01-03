from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        
        for key in ran.keys():
            if ran[key] > mag[key]:
                return False

        return True