class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        """
        So the idea is to start with index 0, if we find anagram between i and i+1,
        we remove the words[i+1] word and skip past loop to start with index 0 again

        if we don't find an anagram using index 0, only then we do i += 1 and start it all
        over again with index 1
        """

        def is_anagram(word1, word2):
            return Counter(word1) == Counter(word2)

        i = 0
        while i < len(words) - 1:
            if is_anagram(word1=words[i],word2=words[i+1]):
                words.remove(words[i+1])
                continue
            i+=1

        return words
