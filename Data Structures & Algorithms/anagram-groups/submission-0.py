class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs:
            sort_str = "".join(sorted(string))
            if sort_str not in seen:
                seen[sort_str] = [string]
            else:
                seen[sort_str].append(string)

        return [val for val in seen.values()]