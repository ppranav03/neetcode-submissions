class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_grams = {}
        for word in strs:
            word_sorted = "".join(sorted(word))
            if word_sorted in a_grams:
                a_grams[word_sorted].append(word)
            else:
                a_grams[word_sorted] = [word]
        
        values = [val for val in a_grams.values()]

        return values