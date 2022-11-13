class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """logical answer is return Counter(s) == Counter(t)"""
        """
        simple idea is to store the string (s) in a Counter
        Then go through the t string in a loop and counting down
        that specific char if it exists in counter.
        finally if all the vals of the dict is exactly 0, that means it is an anagram

        edge case: if len(s) and len(t) is not the same, return false at start
        """
        if (len(s) != len(t)):
            return False

        string_counter = Counter(s)

        for char in t:
            if char in string_counter:
                string_counter[char] -= 1
        """
        according to Counter docs,
        existing counter += Counter() only keeps the non-zero dict sets
        exactly what we need
        https://docs.python.org/2/library/collections.html#collections.Counter
        """
        string_counter += Counter()

        if (len(string_counter) != 0):
            return False
        else:
            return True
